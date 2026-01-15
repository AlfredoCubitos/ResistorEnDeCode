import PySide6.QtCore as Qc
import PySide6.QtGui as Qg
from PySide6.QtSvgWidgets import QSvgWidget
import PySide6.QtWidgets as Qw
from PySide6.QtWidgets import QPushButton, QLabel
from PySide6.QtCore import Qt
import json
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

from PySide6.QtCore import QObject, Signal, Slot
from functools import partial


import resistorendecode.helpers as gh
import resistorendecode.smd_code_parser as smd_parse
from resistorendecode.ui_generated_files.ui_resistance_calc import Ui_MainWindow
from .license import LicenseAgreement


@dataclass
class ResistorConfig:
    """Configuration for resistor band setup"""
    bands: int
    svg_path: str
    widget_size: Tuple[int, int]
    color_placeholders: List[str]


@dataclass
class ResistorValues:
    """Container for calculated resistor values"""
    value: float
    min_value: float
    max_value: float
    tolerance: float
    post_fix: str = ""


class SVGManager:
    """Manages SVG loading and color manipulation"""
    
    def __init__(self, parent):
        self.parent = parent
        
    
    def load_svg(self, path: str) -> bytes:
        """Load SVG file and cache it"""
        svg_cache = {}
        if path not in svg_cache:
            file = Qc.QFile(path)
            if not file.open(Qc.QIODevice.ReadOnly):
                print(f"Error: Unable to read {path}")
                
            svg_cache[path] = file.readAll()
        return svg_cache[path]
    
    def apply_colors(self, svg_data: bytes, color_map: Dict[str, str]) -> bytes:
        """Apply color replacements to SVG data"""
        for placeholder, color in color_map.items():
            #svg_data = svg_data.replace(placeholder.encode(), color.encode())
            svg_data.replace(Qc.QByteArray(placeholder), Qc.QByteArray(color))
        
        return svg_data


class ResistorBandCalculator:
    """Handles resistor band calculations"""
    
    def __init__(self, json_data: dict):
        self.json_data = json_data
    
    def calculate_resistance(self, digits: List[str], multiplier_idx: int, 
                           tolerance_idx: int) -> ResistorValues:
        """Calculate resistance value from band selections"""
        mantissa = int(''.join(digits))
        tolerance = self.json_data["tolerance"][tolerance_idx]["value"]
        
        # Handle special multiplier cases
        divisor = multiplier_idx
        if multiplier_idx == 10:
            divisor = -2
        elif multiplier_idx == 11:
            divisor = -3
        
        value, min_value, max_value, post_fix = gh.calculate_values(
            tolerance, mantissa, divisor
        )
        
        return ResistorValues(value, min_value, max_value, tolerance, post_fix)
    
    def get_color_map(self, band_indices: List[int], config: ResistorConfig) -> Dict[str, str]:
        """Generate color mapping for SVG replacement"""
        colors = self.json_data["colors"]
        color_map = {}
        
        for i, (placeholder, idx) in enumerate(zip(config.color_placeholders, band_indices)):
            if i < len(config.color_placeholders) - 1:  # Regular color bands
                color_map[placeholder] = colors[idx]["color"]
            else:  # Tolerance band (special handling)
                if idx == 11:  # Blank tolerance
                    # Make invisible by setting opacity to 0
                    opacity_key = "opacity:1;mix-blend-mode:normal;vector-effect:none;fill:" + placeholder
                    color_map[opacity_key] = "opacity:0;mix-blend-mode:normal;vector-effect:none;fill:" + placeholder
                else:
                    tid = self.json_data["tolerance"][idx]["color_id"]
                    color_map[placeholder] = colors[tid]["color"]
        
        return color_map


class ComboBoxManager:
    """Manages combo box initialization and data binding"""
    
    def __init__(self, json_data: dict):
        self.json_data = json_data
    
    def setup_combo_boxes(self, combo_configs: List[Tuple[Qw.QComboBox, str]]):
        """Setup multiple combo boxes with their respective data types"""
        for combo, data_type in combo_configs:
            self.populate_combo_box(combo, data_type)
    
    def populate_combo_box(self, combo: Qw.QComboBox, data_type: str):
        """Populate a combo box with data of specified type"""
        data_map = {
            "digit": self.json_data["digits"],
            "multiplier": self.json_data["multiplier"],
            "tolerance": self.json_data["tolerance"],
            "trc": self.json_data["trc"]
        }
        
        if data_type not in data_map:
            return
        
        data = data_map[data_type]
        
        for item in data:
            if data_type == "digit":
                combo.addItem(Qg.QIcon(item["icon"]), item["idx"])
            elif data_type == "multiplier":
                combo.addItem(Qg.QIcon(item["icon"]), item["text"], item["data"])
            elif data_type == "tolerance":
                combo.addItem(Qg.QIcon(item["icon"]), item["text"])
            elif data_type == "trc":
                combo.addItem(Qg.QIcon(item["icon"]), str(item["value"]))


class ResistanceCalc(Qw.QMainWindow, Ui_MainWindow):
    """Main resistance calculator window"""
    
    # Configuration for different resistor types
    RESISTOR_CONFIGS = {
        '4b': ResistorConfig(4, ":general/resistor_4b.svg", (445, 100), 
                            ["#400001", "#400002", "#400003", "#400004"]),
        '5b': ResistorConfig(5, ":general/resistor_5b.svg", (445, 100),
                            ["#500001", "#500002", "#500003", "#500004", "#500005"]),
        '6b': ResistorConfig(6, ":general/resistor_6b.svg", (445, 100),
                            ["#600001", "#600002", "#600003", "#600004", "#600005", "#600006"])
    }
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Initialize managers
        self.svg_manager = SVGManager(self)
        self.combo_manager = None  # Will be initialized after loading JSON
        self.band_calculator = None  # Will be initialized after loading JSON
        self.e_multi = 0 # multiplier for E-Button values
        self.band_label = None
        self.band_type = "4b"
        self.svg_widgets = {}
        self.capdigits = 3
        self.capeia = False
        self.EIA = dict(zip(gh.ESeries["EIA198"],gh.ESeries["EIA198v"]))
        
        # Load JSON data first
        self.load_json_data()
        
        # Initialize managers that depend on JSON data
        self.combo_manager = ComboBoxManager(self.json_data)
        self.band_calculator = ResistorBandCalculator(self.json_data)
        
        # Setup UI components
        self.setup_window()
        self.setup_svg_widgets()
        self.setup_combo_boxes()
        self.setup_validators()
        self.setup_connections()
        self.setup_initial_values()
        
        self.setup_table_data(self.tableWidget,gh.ESeries)

        #self.gridLayout_2.addWidget(QToggleSwitch("5 Band"),1,3)
        
        # Initialize displays
        self.update_all_displays()
        self.verticalSlider.valueChanged.emit(0)
    
    def load_json_data(self):
        """Load JSON configuration data"""
        try:
            jf = Qc.QFile(":/general/icon_data.json")
            jf.open(Qc.QIODevice.ReadOnly | Qc.QIODevice.Text)
            js = jf.readAll()
            err = Qc.QJsonParseError()
            icons = Qc.QJsonDocument.fromJson(js, error=err)
            
            if err.error != Qc.QJsonParseError.NoError:
                print(f"JSON Parse Error: {err.errorString()}")
                
            self.json_data = icons.object()
        except Exception as e:
            print(f"Error loading JSON data: {e}")
            self.json_data = {}
    
    def setup_window(self):
        """Setup main window properties"""
        icon = Qg.QIcon()
        icon.addFile(":/general/resistor_icon.svg", Qc.QSize(), 
                    Qg.QIcon.Normal, Qg.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowTitle("Resistor En or Decode")
        self.license_window = None
    
    def setup_svg_widgets(self):
        """Setup SVG widgets for all resistor types"""

        svg_widget = QSvgWidget(self.RESISTOR_CONFIGS["4b"].svg_path)
        svg_widget.renderer().setAspectRatioMode(Qc.Qt.KeepAspectRatio)
        svg_widget.setFixedSize(Qc.QSize(*self.RESISTOR_CONFIGS["4b"].widget_size))

            # Add to layout

        self.horizontalLayout_4b_svg.addWidget(svg_widget)
            
        self.svg_widgets["4b"] = svg_widget
        
        # Setup SMD widget separately (has different requirements)
        self.setup_smd_widget()

    def change_svg_widget(self,value: str)->None:
        #widget = self.horizontalLayout_4b_svg.parentWidget().findChild(QSvgWidget)
        print("Items: ",self.horizontalLayout_4b_svg.count())
        widget = self.horizontalLayout_4b_svg.itemAt(0).widget()

        widget.load(self.RESISTOR_CONFIGS[value].svg_path)
        self.calculate_resistance()
        pass


    
    def setup_smd_widget(self):
        """Setup SMD resistor widget with text overlay"""
        self.svg_widgets['smd'] = QSvgWidget(self.tab_smd)
        self.horizontalLayout_smd_svg.insertWidget(1, self.svg_widgets['smd'])
        self.svg_widgets['smd'].renderer().setAspectRatioMode(Qc.Qt.KeepAspectRatio)
        self.svg_widgets['smd'].setFixedSize(Qc.QSize(300, 126))
        
        # Setup text overlay
        self.smd_line_edit = Qw.QLineEdit(self.svg_widgets['smd'])
        self.smd_line_edit.setFixedSize(Qc.QSize(300, 126))
        self.smd_line_edit.setFrame(False)
        self.smd_line_edit.setAlignment(Qg.Qt.AlignHCenter)
        self.smd_line_edit.setText("102")
        self.smd_line_edit.setMaxLength(4)
        self.smd_line_edit.setStyleSheet("background: transparent; color: white")
        
        # Setup font
        smd_font = Qg.QFont()
        smd_font.setPointSize(44)
        self.smd_line_edit.setFont(smd_font)
        
        # Hide warning labels initially
        self.label_code_invalid_icon.hide()
        self.label_code_invalid_label.hide()
        self.label_tolerance_notice.hide()
    
    def setup_combo_boxes(self):
        """Setup all combo boxes with their respective data"""
        # Define combo box configurations
        combo_configs = [
            # 4-band resistor
            (self.comboBox_1d, "digit"),
            (self.comboBox_2d, "digit"),
            (self.comboBox_3d, "digit"),
            (self.comboBox_m, "multiplier"),
            (self.comboBox_t, "tolerance"),
            (self.comboBox_trc, "trc"),

        ]
        
        self.combo_manager.setup_combo_boxes(combo_configs)
        
        # Setup unit combo boxes
        self.setup_unit_combo_boxes()
    
    def setup_unit_combo_boxes(self):
        """Setup unit selection combo boxes"""
        units = ["mΩ", "Ω", "kΩ", "MΩ"]
        unit_data = [-3, 0, 3, 6]
        
        self.comboBox_ohm_4b.addItems(units)
        for i, data in enumerate(unit_data):
            self.comboBox_ohm_4b.setItemData(i, data)
    
    def setup_validators(self):
        """Setup input validators for line edits"""
        validator = Qg.QDoubleValidator()
        validator.setNotation(Qg.QDoubleValidator.StandardNotation)
        validator.setDecimals(2)
        validator.setLocale(Qc.QLocale.c())
        
        self.lineEdit_ohm_4b.setValidator(validator)
    
    def setup_connections(self):
        """Setup signal-slot connections"""
        # 4-band connections
        self.comboBox_1d.currentIndexChanged.connect(self.calculate_resistance)
        self.comboBox_2d.currentIndexChanged.connect(self.calculate_resistance)
        self.comboBox_3d.currentIndexChanged.connect(self.calculate_resistance)
        self.comboBox_m.currentIndexChanged.connect(self.calculate_resistance)
        self.comboBox_t.currentIndexChanged.connect(self.calculate_resistance)
        self.comboBox_trc.currentIndexChanged.connect(self.calculate_resistance)

        
        # SMD connections
        self.connect_smd_signals()

        # Slider
        self.verticalSlider.valueChanged.connect(self.sliderPos)
        # Line edit connections
        self.lineEdit_ohm_4b.editingFinished.connect(self.on_line_edit_finished_4b)

        self.lineEdit_ohm_4b.cursorPositionChanged.connect(self.validate_line_edit)
        #self.lineEdit_ohm_5b.cursorPositionChanged.connect(self.validate_line_edit)

        # E-Buttons
        self.pB_E24_Min.clicked.connect(partial(self.eButton,self.pB_E24_Min))
        self.pB_48_Min.clicked.connect(partial(self.eButton,self.pB_48_Min))
        self.pB_E96_Min.clicked.connect(partial(self.eButton,self.pB_E96_Min))

        # Capacity EIA Checkbox
        self.cb_csmd_198.checkStateChanged.connect(self.capacity_eia)
        # Capacity 4 Digits
        self.rB_csmd.checkStateChanged.connect(self.capacity_digits)
        # Capacity
        self.csmd_digit1.currentIndexChanged.connect(self.capacity_setter)
        self.csmd_digit2.currentIndexChanged.connect(self.capacity_setter)
        self.csmd_digit3.currentIndexChanged.connect(self.capacity_setter)
        self.csmd_digit4.currentIndexChanged.connect(self.capacity_setter)
        self.cmb_csmb_cap.currentIndexChanged.connect(self.capacity_setter)
        self.cmb_csmb198_1.currentIndexChanged.connect(self.capacity_setter)
        self.cmb_csmb198_2.currentIndexChanged.connect(self.capacity_setter)

    @Slot(QPushButton)
    def eButton(self,button):
        print(button.text())
        val = float(button.text()) * pow(10,self.e_multi-1)
        self.lineEdit_ohm_4b.setText(str(val))
        pass

    @Slot(int)
    def sliderPos(self,value):
        print("Slider: ", value)
        match(value):
           case 0:
               self.band_type = "4b"
               self.change_svg_widget("4b")
               self.label_50.setEnabled(False)
               self.comboBox_3d.setEnabled(False)
           case 1:
               self.band_type = "5b"
               self.change_svg_widget("5b")
               self.label_50.setEnabled(True)
               self.comboBox_3d.setEnabled(True)
               self.label_53.setEnabled(False)
               self.comboBox_trc.setEnabled(False)
               self.label_trc.setEnabled(False)
               self.lineEdit_6b.setEnabled(False)
           case 2:
               self.band_type = "6b"
               self.change_svg_widget("6b")
               self.label_53.setEnabled(True)
               self.comboBox_trc.setEnabled(True)
               self.label_trc.setEnabled(True)
               self.lineEdit_6b.setEnabled(True)

        pass

    
    def connect_smd_signals(self):
        """Connect SMD resistor signals"""
        smd_controls = [
            self.radioButton_line_none,
            self.radioButton_line_top,
            self.radioButton_line_under_short,
            self.radioButton_line_under_long
        ]
        
        for control in smd_controls:
            control.clicked.connect(self.calculate_resistance_smd)
        
        self.smd_line_edit.textEdited.connect(self.calculate_resistance_smd)

    @Slot(int)
    def capacity_eia(self,value):
        if value == Qt.CheckState.Checked:
            self.capeia = True
            self.rB_csmd.setCheckState(Qt.CheckState.Unchecked)
        else:
            self.capeia = False

    @Slot(int)
    def capacity_digits(self, value):
        if value == Qt.CheckState.Checked:
            self.capdigits = 4
        else:
            self.capdigits = 3

    @Slot()
    def capacity_setter(self):
        if self.capeia:
            self.capacity_setEiaValue()
        else:
            self.capacity_setValue()

    def capacity_setValue(self):

        v = self.csmd_digit1.currentText()
        v = v + self.csmd_digit2.currentText()
        v = v + self.csmd_digit3.currentText()

        if self.capdigits == 4:
            v = v + self.csmd_digit4.currentText()
            l = gh.CAPACITY["tolerance"][self.csmd_digit4.currentText()]


        self.csmd_le1.setText(v)
        if len(v) == 3:
            self.capacity_calc(v)
        if len(v) == 4:
            self.le_c_smd_tolerance.setText(str(l[0]))
            self.label_c_tolerance.setText(l[1])


    def capacity_setEiaValue(self):

        v = self.cmb_csmb198_1.currentText() + self.cmb_csmb198_2.currentText()
        self.csmd_le1.setText(v)
        if len(v) == 2:
            self.capacity_EiaCalc(v)


    def capacity_EiaCalc(self,value: str)->None:
        v1 = self.EIA[value[0]]
        v2 = "1" if value[1] == "0" else  "1"+"".zfill(int(value[1]))

        v = (int(v1) * int(v2)) / int(gh.CAPACITY[self.cmb_csmb_cap.currentText()])

        print("Cap: ",v1," ",v2," ",v, " ",len(str(v)))

        if "e-" in str(v):

            #self.csmd_le_cap.setText(f'{v:f} or {v}')
            #print("Exp: ",str(v)[len(str(v))-1])
            e = str(v)[len(str(v))-1]
            self.csmd_le_cap.setText(f'{v:.{e}f} or {v}')
        else:
            self.csmd_le_cap.setText(str(v))

    def capacity_calc(self,value: str)->None:

        z = "." if value[1] == "R" else value[1]
        v = value[0] + z
        v = v + "".zfill(int(value[2]))
        ## get rid of the trailing .0
        if v.isdigit():
            v = int(v) // int(gh.CAPACITY[self.cmb_csmb_cap.currentText()])
        else:
            v = float(v) / int(gh.CAPACITY[self.cmb_csmb_cap.currentText()])
        self.csmd_le_cap.setText(str(v))



    def setup_initial_values(self)->None:
        """Setup initial values for combo boxes"""
        # Set meaningful defaults
        self.comboBox_1d.setCurrentIndex(1)
        # Set tolerance to gold (most common)
        self.comboBox_t.setCurrentIndex(8)
        # Set multiplier to 1 (index 3 typically)
        self.comboBox_m.setCurrentIndex(3)
    
    def calculate_resistance(self):
        match(self.band_type):
            case "4b":
                self.calculate_resistance_4b()
            case "5b":
                self.calculate_resistance_5b()
            case "6b":
                self.calculate_resistance_6b()

    def calculate_resistance_4b(self):
        """Calculate 4-band resistance"""
        digits = [
            self.comboBox_1d.currentText(),
            self.comboBox_2d.currentText()
        ]
        multiplier_idx = self.comboBox_m.currentIndex()
        tolerance_idx = self.comboBox_t.currentIndex()
        
        values = self.band_calculator.calculate_resistance(
            digits, multiplier_idx, tolerance_idx
        )
        
        self.update_resistance_display('4b', values)
        self.update_svg_colors('4b')
        
        return values.value, values.min_value, values.max_value


    def calculate_resistance_5b(self):
        """Calculate 5-band resistance"""

        digits = [
            self.comboBox_1d.currentText(),
            self.comboBox_2d.currentText(),
            self.comboBox_3d.currentText()
        ]
        multiplier_idx = self.comboBox_m.currentIndex()
        tolerance_idx = self.comboBox_t.currentIndex()
        
        values = self.band_calculator.calculate_resistance(
            digits, multiplier_idx, tolerance_idx
        )
        
        self.update_resistance_display('5b', values)
        self.update_svg_colors('5b')
        
        return values.value, values.min_value, values.max_value
    
    def calculate_resistance_6b(self):
        """Calculate 6-band resistance"""
        digits = [
            self.comboBox_1d.currentText(),
            self.comboBox_2d.currentText(),
            self.comboBox_3d.currentText()
        ]
        multiplier_idx = self.comboBox_m.currentIndex()
        tolerance_idx = self.comboBox_t.currentIndex()
        
        values = self.band_calculator.calculate_resistance(
            digits, multiplier_idx, tolerance_idx
        )
        
        # Get TCR value
        trc = self.json_data["tolerance"][self.comboBox_trc.currentIndex()]["value"]
        
        self.update_resistance_display('6b', values, trc)
        self.update_svg_colors('6b')
        
        return values.value, values.min_value, values.max_value, trc
    
    def calculate_resistance_smd(self):
        """Calculate SMD resistance"""
        smd_code = self.smd_line_edit.text()
        line_under_short = self.radioButton_line_under_short.isChecked()
        line_under_long = self.radioButton_line_under_long.isChecked()
        
        decoded = smd_parse.parse_code(smd_code, line_under_short, line_under_long)
        
        if decoded is not None:
            value, tolerance, is_standard_tolerance = decoded
            min_value = value * (1 - 0.01 * tolerance)
            max_value = value * (1 + 0.01 * tolerance)
            
            self.lineEdit_resistance_smd.setText(f"{value:.1f} ±{tolerance}%")
            self.lineEdit_resistance_min_smd.setText(f"{min_value:.1f}")
            self.lineEdit_resistance_max_smd.setText(f"{max_value:.1f}")
            
            # Hide/show notices
            self.label_tolerance_notice.setHidden(is_standard_tolerance)
            self.label_code_invalid_icon.hide()
            self.label_code_invalid_label.hide()
            
            self.update_smd_svg_colors()
            
            return value, min_value, max_value
        else:
            # Invalid code
            self.clear_smd_display()
            self.show_smd_error()
            return None, None, None

    def update_resistance_display(self, resistor_type: str, values: ResistorValues, tcr: float = None):
        # Update values
        if tcr is not None:  # 6-band has TCR
            self.lineEdit_resistance_4b.setText(f"{values.value} ±{values.tolerance}")
            self.lineEdit_6b.setText(f"{tcr} ppm/°C")

        else:
            self.lineEdit_resistance_4b.setText(f"{values.value}")
            self.label_resistance_4b.setText(f"{values.post_fix}")

            # Update ohm line edit and combo box

            self.lineEdit_ohm_4b.setText(f"{values.value}")
            self.comboBox_ohm_4b.setCurrentIndex(self.comboBox_ohm_4b.findText(values.post_fix, Qc.Qt.MatchFixedString))

            # Update tolerance labels

            self.label_t_min_4b.setText(f"- {values.tolerance}%")
            self.label_t_min_4b.setText(f"+ {values.tolerance}%")
            self.lineEdit_resistance_min_4b.setText(str(values.min_value))
            self.lineEdit_resistance_max_4b.setText(str(values.max_value))


    def update_svg_colors(self, resistor_type: str):
        """Update SVG colors for a resistor type"""
        if resistor_type not in self.RESISTOR_CONFIGS:
            return
        
        config = self.RESISTOR_CONFIGS[resistor_type]
        
        # Get current selections
        band_indices = []
        
        # Digit bands - abhängig vom Resistor-Typ
        if resistor_type == '4b':
            # 4-Band: nur 2 Ziffern (1d, 2d)
            band_indices.append(self.comboBox_1d.currentIndex())
            band_indices.append(self.comboBox_2d.currentIndex())
            band_indices.append(self.comboBox_m.currentIndex())    # Multiplier
            band_indices.append(self.comboBox_t.currentIndex())    # Tolerance

            
        elif resistor_type == '5b':
            # 5-Band: 3 Ziffern (1d, 2d, 3d)
            band_indices.append(self.comboBox_1d.currentIndex())
            band_indices.append(self.comboBox_2d.currentIndex())
            band_indices.append(self.comboBox_3d.currentIndex())
            band_indices.append(self.comboBox_m.currentIndex())    # Multiplier
            band_indices.append(self.comboBox_t.currentIndex())    # Tolerance
            
        elif resistor_type == '6b':
            # 6-Band: 3 Ziffern + TCR
            band_indices.append(self.comboBox_1d.currentIndex())
            band_indices.append(self.comboBox_2d.currentIndex())
            band_indices.append(self.comboBox_3d.currentIndex())
            band_indices.append(self.comboBox_m.currentIndex())    # Multiplier
            band_indices.append(self.comboBox_t.currentIndex())    # Tolerance
            band_indices.append(self.comboBox_trc.currentIndex())  # TCR
        
        print(f"Band indices for {resistor_type}: {band_indices}")
        
        # Generate color map and apply
        color_map = self.band_calculator.get_color_map(band_indices, config)
        svg_data = self.svg_manager.load_svg(config.svg_path)
        colored_svg = self.svg_manager.apply_colors(svg_data, color_map)
        
        #self.svg_widgets[resistor_type].load(colored_svg)
        self.svg_widgets["4b"].load(colored_svg)
    
    def update_smd_svg_colors(self):
        """Update SMD SVG colors based on line selections"""
        line_under_short = self.radioButton_line_under_short.isChecked()
        line_under_long = self.radioButton_line_under_long.isChecked()
        line_top = self.radioButton_line_top.isChecked()
        
        color_map = {
            "#996601": "#FFFFFF" if line_under_short else "#000000",
            "#996602": "#FFFFFF" if line_under_long else "#000000",
            "#996603": "#FFFFFF" if line_top else "#000000",
            "stroke-opacity:0.28": "stroke-opacity:1" if line_under_long else "stroke-opacity:0"
        }
        
        svg_data = self.svg_manager.load_svg(":general/resistor_smd.svg")
        colored_svg = self.svg_manager.apply_colors(svg_data, color_map)
        self.svg_widgets['smd'].load(colored_svg)
    
    def clear_smd_display(self):
        """Clear SMD display fields"""
        self.lineEdit_resistance_smd.clear()
        self.lineEdit_resistance_min_smd.clear()
        self.lineEdit_resistance_max_smd.clear()
    
    def show_smd_error(self):
        """Show SMD error indicators"""
        self.label_tolerance_notice.hide()
        self.label_code_invalid_icon.show()
        self.label_code_invalid_label.show()
    
    def validate_line_edit(self):
        """Validate line edit input and update styling"""
        sender = self.sender()
        valid = sender.hasAcceptableInput()
        
        if valid:
            sender.setStyleSheet("background-color: #aaff85")
        else:
            sender.setStyleSheet("background-color: #ff8088")
    
    def on_line_edit_finished_4b(self):
        """Handle 4-band line edit finished"""
        value = self.lineEdit_ohm_4b.text()
        self.process_line_edit_input(value)
    

    def process_line_edit_input(self, r_value: str):
        """Process line edit input and update combo boxes"""
        # This would contain the logic to reverse-calculate combo box values
        # from the entered resistance value
        # Implementation depends on the specific requirements
        pass

        val = float(r_value)
        lv = round(float(r_value))
        self.e_multi = len(str(lv))
        sv = val / (pow(10,self.e_multi-1))
        self.pB_E24_Min.setText(str( min(gh.ESeries["E24"],key=lambda x:abs(x-float(sv)))))
        self.pB_48_Min.setText(str(min(gh.ESeries["E48"],key=lambda x:abs(x-float(sv)))))
        self.pB_E96_Min.setText(str( min(gh.ESeries["E96"],key=lambda x:abs(x-float(sv)))))
        print(sv)
        print(min(gh.ESeries["E24"],key=lambda x:abs(x-float(sv))))
    
    def update_all_displays(self):
        """Update all resistance displays"""
        self.calculate_resistance_4b()
        self.calculate_resistance_5b()
        self.calculate_resistance_6b()
        self.calculate_resistance_smd()
    
    def open_license(self):
        """Open license agreement window"""
        if self.license_window is None:
            self.license_window = LicenseAgreement()
        self.license_window.show()


    # Additional utility functions that were in the original code
    # but can be simplified or moved to helper modules

    def setup_table_data(self,table_widget, data_sets):
        
        for col, k in enumerate(list(data_sets)):
            print("col: ",col," val: ",k)
            table_widget.insertColumn(col)
            table_widget.setHorizontalHeaderItem(int(col),Qw.QTableWidgetItem(str(k)))
            for row, value in enumerate(data_sets[k]):
                if row >= table_widget.rowCount():
                    table_widget.insertRow(row)
                
                item = Qw.QTableWidgetItem(str(value))
                item.setTextAlignment(Qc.Qt.AlignHCenter)
                table_widget.setItem(row, col, item)
