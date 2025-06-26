import PySide6.QtCore as Qc
import PySide6.QtGui as Qg
from PySide6.QtSvgWidgets import QSvgWidget
import PySide6.QtWidgets as Qw
import json

import helpers as gh
import smd_code_parser as smd_parse
from ui_generated_files.ui_resistance_calc import Ui_MainWindow
from driver_license import LicenseAgreement


class ResistanceCalc(Qw.QMainWindow, Ui_MainWindow):
    """Wrapper to handle interactions on the Unit Manager level."""

    def __init__(self):
        Qw.QMainWindow.__init__(self)
        self.setupUi(self)

        icon = Qg.QIcon()
        icon.addFile(
            ":/general/resistor_icon.svg", Qc.QSize(), Qg.QIcon.Normal, Qg.QIcon.Off
        )
        self.setWindowIcon(icon)
        self.setWindowTitle("Resistor En or Decode")

        # For the license window
        self.license_window = None
        self.icons = Qc.QJsonDocument()  # a json document with all data
        self.json = {}

        # Initialize SVG widgets
        self.svg_widget_4b = QSvgWidget(":general/resistor_4b.svg", self.tab_4b)
        self.horizontalLayout_4b_svg.insertWidget(1, self.svg_widget_4b)
        self.svg_widget_4b.renderer().setAspectRatioMode(Qc.Qt.KeepAspectRatio)
        self.svg_widget_4b.setFixedSize(Qc.QSize(445, 100))

        self.svg_widget_5b = QSvgWidget(":general/resistor_5b.svg", self.tab_5b)
        self.horizontalLayout_5b_svg.insertWidget(1, self.svg_widget_5b)
        self.svg_widget_5b.renderer().setAspectRatioMode(Qc.Qt.KeepAspectRatio)
        self.svg_widget_5b.setFixedSize(Qc.QSize(445, 100))

        self.svg_widget_6b = QSvgWidget(":general/resistor_6b.svg", self.tab_6b)
        self.horizontalLayout_6b_svg.insertWidget(1, self.svg_widget_6b)
        self.svg_widget_6b.renderer().setAspectRatioMode(Qc.Qt.KeepAspectRatio)
        self.svg_widget_6b.setFixedSize(Qc.QSize(445, 100))

        self.svg_widget_smd = QSvgWidget(self.tab_smd)
        self.horizontalLayout_smd_svg.insertWidget(1, self.svg_widget_smd)
        self.svg_widget_smd.renderer().setAspectRatioMode(Qc.Qt.KeepAspectRatio)
        self.svg_widget_smd.setFixedSize(Qc.QSize(300, 126))
        # Add the lineEdit over the smd preview
        self.smd_line_edit = Qw.QLineEdit(self.svg_widget_smd)
        self.smd_line_edit.setFixedSize(Qc.QSize(300, 126))
        self.smd_line_edit.setFrame(False)
        self.smd_line_edit.setAlignment(Qg.Qt.AlignHCenter)
        # Set a simple default smd code
        self.smd_line_edit.setText("102")
        # Set magic font size appropriate for the hard-coded size
        smd_font = Qg.QFont()
        smd_font.setPointSize(44)
        self.smd_line_edit.setFont(smd_font)
        self.smd_line_edit.setMaxLength(4)
        self.smd_line_edit.setStyleSheet("background: transparent; color: white")
        # Hide the warning and notice for smd values
        self.label_code_invalid_icon.hide()
        self.label_code_invalid_label.hide()
        self.label_tolerance_notice.hide()

        self.get_comboBox_data()
        self.initCombosR()

        # Connect license button slot
        # self.pushButton_license.clicked.connect(self.open_license)
        # Connect slots to update the output
        self.comboBox_1d_4b.currentIndexChanged.connect(self.calculate_res_4b)
        self.comboBox_2d_4b.currentIndexChanged.connect(self.calculate_res_4b)
        self.comboBox_m_4b.currentIndexChanged.connect(self.calculate_res_4b)
        self.comboBox_t_4b.currentIndexChanged.connect(self.calculate_res_4b)
        self.lineEdit_ohm_4b.editingFinished.connect(self.lineEditingFinished4b)

        self.lineEdit_ohm_4b.cursorPositionChanged.connect(self.validateLineEdit)

        self.comboBox_1d_5b.currentIndexChanged.connect(self.calculate_res_5b)
        self.comboBox_2d_5b.currentIndexChanged.connect(self.calculate_res_5b)
        self.comboBox_3d_5b.currentIndexChanged.connect(self.calculate_res_5b)
        self.comboBox_m_5b.currentIndexChanged.connect(self.calculate_res_5b)
        self.comboBox_t_5b.currentIndexChanged.connect(self.calculate_res_5b)
        self.lineEdit_ohm_5b.editingFinished.connect(self.lineEditingFinished5b)

        self.lineEdit_ohm_5b.cursorPositionChanged.connect(self.validateLineEdit)

        self.comboBox_1d_6b.currentIndexChanged.connect(self.calculate_res_6b)
        self.comboBox_2d_6b.currentIndexChanged.connect(self.calculate_res_6b)
        self.comboBox_3d_6b.currentIndexChanged.connect(self.calculate_res_6b)
        self.comboBox_m_6b.currentIndexChanged.connect(self.calculate_res_6b)
        self.comboBox_t_6b.currentIndexChanged.connect(self.calculate_res_6b)
        self.comboBox_tcr_6b.currentIndexChanged.connect(self.calculate_res_6b)

        self.radioButton_line_none.clicked.connect(self.calculate_res_smd)
        self.radioButton_line_top.clicked.connect(self.calculate_res_smd)
        self.radioButton_line_under_short.clicked.connect(self.calculate_res_smd)
        self.radioButton_line_under_long.clicked.connect(self.calculate_res_smd)
        self.smd_line_edit.textEdited.connect(self.calculate_res_smd)
        
        self.csmd_digit1.valueChanged.connect(self.setCapacityValue)
        self.csmd_digit2.currentIndexChanged.connect(self.setCapacityValue)
        self.csmd_digit3.currentIndexChanged.connect(self.setCapacityValue)
        self.csmd_digit4.currentIndexChanged.connect(self.setCapacityValue)
        self.rB_csmd.checkStateChanged.connect(self.setCapacityValue)
        self.cmb_csmb_cap.currentIndexChanged.connect(self.calculateCapacity)

        file = Qc.QFile(":general/capacitor_smd.svg")
        if not file.open(Qc.QIODevice.ReadOnly):
            print("Error: Unable to read capacitor_smd.svg")
        self.svg_data_smd_c = file.readAll()

        self.comboBox_1d_4b.setCurrentIndex(1)
        self.comboBox_1d_5b.setCurrentIndex(1)
        # Set the default tolerance to the most common band, gold
        self.comboBox_t_4b.setCurrentIndex(8)
        self.comboBox_t_5b.setCurrentIndex(8)
        self.comboBox_t_6b.setCurrentIndex(8)
        # Set the default divisor to 1
        self.comboBox_m_4b.setCurrentIndex(0)
        self.comboBox_m_5b.setCurrentIndex(0)
        self.comboBox_m_6b.setCurrentIndex(0)

        self.change_band_colors_4b()

        # Fill initial state in outputs
        self.calculate_res_4b()
        self.calculate_res_5b()
        self.calculate_res_6b()
        self.calculate_res_smd()
        self.setETable()
        self.setCapacities()
        self.insertCdigits()

    def calculateCapacity(self):
        value = self.csmd_le1.text()
        f = self.cmb_csmb_cap.currentText()
        idx = self.cmb_csmb_cap.currentIndex()
        divisor = gh.CAPACITY[idx][1]
        m = self.csmd_digit3.currentText()
        if len(m) > 0:
            multiplier = 10 ** int(m)
        else:
            multiplier = 1

        if self.csmd_digit2 == "R":
            value = value.replace("R", ".")
        else:
            value = value[:2]

        print(value[:2])

        if len(value) > 0 and len(self.csmd_digit2.currentText()) > 0:
            if divisor == 1000000 and multiplier < 10**3:
                c = f"{(int(value) * multiplier) / divisor:.6f}"
            elif divisor == 1000000000 and multiplier < 10**4:
                c = f"{(int(value) * multiplier) / divisor:.9f}"
            else:
                c = (int(value) * multiplier) / divisor
                
            if self.csmd_digit4.isEnabled():
                data = self.csmd_digit4.currentData()
                min, max = self.getC_MinMax(c,data)
                self.label_c_smd_min.setText("- "+data)
                self.lineEdit_c_smd_minval.setText(str(min))
                self.label_c_smd_max.setText("+ "+data)
                self.lineEdit_c_smd_maxval.setText(str(max))
                
            self.csmd_le_cap.setText(str(c))

    def insertCdigits(self):
        self.csmd_digit2.insertItems(
            0, ["", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "R"]
        )
        self.csmd_digit3.insertItems(
            0, ["", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        )
        self.csmd_digit4.insertItems(0, ["B", "C", "D", "E", "J", "K", "M", "Z"])
        digit4data = ["0.1pf","0.25pf","0.5pf","1%","2%","5%","10%","20%","+80/-20%"]
        for i,d in enumerate(digit4data):
            self.csmd_digit4.setItemData(i,d)
            
    def setCapacityValue(self, idx):
        c = ""
        frst = self.csmd_digit1.value()
        scnd = self.csmd_digit2.currentText()
        thrd = self.csmd_digit3.currentText()
        if len(scnd) == 0:
            scdn = "         "
        c = f"{frst}{scnd}{thrd}"
        value = c

        if self.csmd_digit4.isEnabled():
            c = f"{c}{self.csmd_digit4.currentText()}"
            data = self.csmd_digit4.currentData()
            min, max = self.getC_MinMax(value,data)
            self.label_c_smd_min.setText("- "+data)
            self.lineEdit_c_smd_minval.setText(str(min))
            self.label_c_smd_max.setText("+ "+data)
            self.lineEdit_c_smd_maxval.setText(str(max))
            
        self.csmd_le_cap.setText(str(value))
        self.csmd_le1.setText(str(c))
        self.calculateCapacity()
    
    def getC_MinMax(self,c,data):
        if data.endswith("pf"):
            min = float (int(c) - float(data.rstrip("pf")))
            max = float (int(c) + float(data.rstrip("pf")))
            
        
        return min, max

    def setETable(self):
        for i, v in enumerate(gh.E96):  # this line must be first
            itm = Qw.QTableWidgetItem(str(v))
            itm.setTextAlignment(Qc.Qt.AlignHCenter)
            self.tableWidget.insertRow(i)
            self.tableWidget.setItem(i, 3, itm)
        for i, v in enumerate(gh.E48):
            itm = Qw.QTableWidgetItem(str(v))
            itm.setTextAlignment(Qc.Qt.AlignHCenter)
            self.tableWidget.setItem(i, 2, itm)
        for i, v in enumerate(gh.E24):
            itm = Qw.QTableWidgetItem(str(v))
            itm.setTextAlignment(Qc.Qt.AlignHCenter)
            self.tableWidget.setItem(i, 1, itm)
        for i, v in enumerate(gh.LE24):
            itm = Qw.QTableWidgetItem(str(v))
            itm.setTextAlignment(Qc.Qt.AlignHCenter)
            self.tableWidget.setItem(i, 0, itm)
        for i, v in enumerate(gh.EIA198v):
            itm = Qw.QTableWidgetItem(str(v))
            itm.setTextAlignment(Qc.Qt.AlignHCenter)
            self.tableWidget.setItem(i, 5, itm)
        for i, v in enumerate(gh.EIA198):
            itm = Qw.QTableWidgetItem(str(v))
            itm.setTextAlignment(Qc.Qt.AlignHCenter)
            self.tableWidget.setItem(i, 4, itm)

    def setCapacities(self):
        for v in gh.CAPACITY:
            self.cmb_csmb_cap.addItem(v[0])

    def calculate_4b(self):
        value = self.lineEdit_resistance_4b.text()
        value = value.replace(",", ".")
        if value[0] == "0":
            return
        if value.endswith(("k", "K")):
            r = value.rstrip("kK")
            r = f"{float(r) * 1000:g}"
        elif value.endswith(("M")):
            r = value.rstrip("mM")
            r = f"{float(r) * 1000000:g}"
        else:
            r = value

        mul = gh.get_multiplier(r)
        # print(value, " :: ", r[0], " - ", r[1], " ", mul["idx"])

        if r[1] == ".":
            snd = r[2]
        else:
            snd = r[1]

        self.comboBox_1d_4b.setCurrentIndex(int(r[0]) - 1)
        self.comboBox_2d_4b.setCurrentIndex(int(snd))
        self.comboBox_m_4b.setCurrentIndex(int(mul["idx"]))


    def change_band_colors_4b(self):
        idx1 = self.comboBox_1d_4b.currentIndex()
        idx2 = self.comboBox_2d_4b.currentIndex()
        idm = self.comboBox_m_4b.currentIndex()
        idt = self.comboBox_t_4b.currentIndex()

        colors = self.json["colors"]
        tid = self.json["tolerance"][idt]["color_id"]
        # print(idx2, " : ", bytes(colors[idx2]["color"], "utf-8"))
        file = Qc.QFile(":general/resistor_4b.svg")
        if not file.open(Qc.QIODevice.ReadOnly):
            print("Error: Unable to read resistor_4b.svg")
        svg_data_4b = file.readAll()
        # Hot patch SVG file

        svg_data_4b.replace(b"#400001", bytes(colors[idx1]["color"], "utf-8")).replace(
            b"#400002", bytes(colors[idx2]["color"], "utf-8")
        ).replace(b"#400003", bytes(colors[idm]["color"], "utf-8"))

        if (
            idt == 11
        ):  # Make 4th band invisible if blank selected, otherwise apply color transform.
            svg_data_4b.replace(
                b"opacity:1;mix-blend-mode:normal;vector-effect:none;fill:#400004;",
                b"opacity:0;mix-blend-mode:normal;vector-effect:none;fill:#400004;",
            )
        else:
            svg_data_4b.replace(b"#400004", bytes(colors[tid]["color"], "utf-8"))

        self.svg_widget_4b.load(svg_data_4b)

        # change_band_colors_4b

    def change_band_colors_5b(self):
        idx1 = self.comboBox_1d_5b.currentIndex()
        idx2 = self.comboBox_2d_5b.currentIndex()
        idx3 = self.comboBox_3d_5b.currentIndex()
        idm = self.comboBox_m_5b.currentIndex()
        idt = self.comboBox_t_5b.currentIndex()
        colors = self.json["colors"]

        tid = self.json["tolerance"][idt]["color_id"]

        file = Qc.QFile(":general/resistor_5b.svg")
        if not file.open(Qc.QIODevice.ReadOnly):
            print("Error: Unable to read resistor_5b.svg")
        svg_data = file.readAll()
        # Hot patch SVG file
        svg_data.replace(b"#500001", bytes(colors[idx1]["color"], "utf-8")).replace(
            b"#500002", bytes(colors[idx2]["color"], "utf-8")
        ).replace(b"#500003", bytes(colors[idx3]["color"], "utf-8")).replace(
            b"#500004", bytes(colors[idm]["color"], "utf-8")
        ).replace(b"#500005", bytes(colors[tid]["color"], "utf-8"))
        # Update SVG
        self.svg_widget_5b.load(svg_data)
        # change_band_colors_5b

    def change_band_colors_6b(self):
        idx1 = self.comboBox_1d_6b.currentIndex()
        idx2 = self.comboBox_2d_6b.currentIndex()
        idx3 = self.comboBox_3d_6b.currentIndex()
        idm = self.comboBox_m_6b.currentIndex()
        idt = self.comboBox_t_6b.currentIndex()
        idc = self.comboBox_tcr_6b.currentIndex()

        colors = self.json["colors"]
        tid = self.json["tolerance"][idt]["color_id"]

        file = Qc.QFile(":general/resistor_6b.svg")
        if not file.open(Qc.QIODevice.ReadOnly):
            print("Error: Unable to read resistor_6b.svg")
        svg_data = file.readAll()
        # Hot patch SVG file
        svg_data.replace(b"#600001", bytes(colors[idx1]["color"], "utf-8")).replace(
            b"#600002", bytes(colors[idx2]["color"], "utf-8")
        ).replace(b"#600003", bytes(colors[idx3]["color"], "utf-8")).replace(
            b"#600004", bytes(colors[idm]["color"], "utf-8")
        ).replace(b"#600005", bytes(colors[tid]["color"], "utf-8")).replace(
            b"#600006", bytes(colors[idc]["color"], "utf-8")
        )

        # Update SVG
        self.svg_widget_6b.load(svg_data)
        # change_band_colors_6b

    def change_band_colors_smd(self):
        line_under_short = self.radioButton_line_under_short.isChecked()
        line_under_long = self.radioButton_line_under_long.isChecked()
        line_top = self.radioButton_line_top.isChecked()

        file = Qc.QFile(":general/resistor_smd.svg")
        if not file.open(Qc.QIODevice.ReadOnly):
            print("Error: Unable to read resistor_smd.svg")
        svg_data = file.readAll()

        def color_assignment(show):
            if show:
                return b"#FFFFFF"
            else:
                return b"#000000"

        def opacity_assignment(show):
            # Used to make the long bar transparent or opaque, since it overlaps the short bar.
            if show:
                return b"stroke-opacity:1"
            else:
                return b"stroke-opacity:0"

        # Hot patch SVG file by replacing these placeholder colors.
        svg_data.replace(b"#996601", color_assignment(line_under_short)).replace(
            b"#996602", color_assignment(line_under_long)
        ).replace(b"#996603", color_assignment(line_top)).replace(
            b"stroke-opacity:0.28", opacity_assignment(line_under_long)
        )

        # Update SVG
        self.svg_widget_smd.load(svg_data)
        # change_band_colors_smd

    def calculate_res_4b(self):
        self.change_band_colors_4b()  # Update svg
        digit1 = self.comboBox_1d_4b.currentText()
        digit2 = self.comboBox_2d_4b.currentText()
        divisor = self.comboBox_m_4b.currentIndex()

        tolid = self.comboBox_t_4b.currentIndex()
        tolerance = self.json["tolerance"][tolid]["value"]
        mantissa = int(digit1 + digit2)
        
        if divisor == 10:
            divisor = -2
        if divisor == 11:
            divisor = -3

        value, min_value, max_value, post_fix = gh.calculate_values(
            tolerance, mantissa, divisor
        )

        self.lineEdit_resistance_4b.setText(f"{value}")
        self.label_resistance_4b.setText(f"{post_fix}")
        self.lineEdit_resistance_min_4b.setText(str(min_value))
        self.lineEdit_resistance_max_4b.setText(str(max_value))
        self.lineEdit_ohm_4b.setText(f"{value}")
        self.label_t_min_4b.setText(f"- {tolerance}%")
        self.label_t_max_4b.setText(f"+ {tolerance}%")

        self.comboBox_ohm_4b.setCurrentIndex(
            self.comboBox_ohm_4b.findText(post_fix, Qc.Qt.MatchFixedString)
        )

        return value, min_value, max_value
        # calculate_res_4b

    def validateLineEdit(self):
        valid = self.sender().hasAcceptableInput()
        # valid = self.lineEdit_ohm_4b.hasAcceptableInput()
        # valid = self.lineEdit_ohm_4b.hasAcceptableInput()
        if valid:
            ss = "background-color: #aaff85"
        else:
            ss = "background-color: #ff8088"

        self.sender().setStyleSheet(ss)

    def lineEditingFinished4b(self):
        value = float(self.lineEdit_ohm_4b.text())
        multi = self.comboBox_ohm_4b.currentData()
        ohm = int(value**multi)
        digits = str(ohm)
        if len(digits) > 1:
            digit2 = digits[1]
        elif int(digits[0]) < 1:
            return
        else:
            digit2 = ""

        multiplier = int(ohm) / int(digits[0] + digit2)

        self.comboBox_1d_4b.currentIndexChanged.disconnect()
        self.comboBox_2d_4b.currentIndexChanged.disconnect()
        # self.comboBox_m_4b.currentIndexChanged.disconnect()

        self.comboBox_1d_4b.setCurrentIndex(int(digits[0]))

        print(
            digits[0],
            " ",
            digits[1],
            " ",
            ohm,
            " ",
            multiplier,
            " ",
            self.comboBox_m_4b.findData(
                str(int(multiplier)), flags=Qc.Qt.MatchFlag.MatchFixedString
            ),
        )

        if len(digits) > 1:
            self.comboBox_2d_4b.setCurrentIndex(int(digits[1]))
        idx = self.comboBox_m_4b.findData(
            str(int(multiplier)), flags=Qc.Qt.MatchFlag.MatchFixedString
        )
        self.comboBox_m_4b.setCurrentIndex(idx - 1)

        # self.calculate_4b()
        self.comboBox_1d_4b.currentIndexChanged.connect(self.calculate_res_4b)
        self.comboBox_2d_4b.currentIndexChanged.connect(self.calculate_res_4b)
        # self.comboBox_m_4b.currentIndexChanged.connect(self.calculate_res_4b)

    def lineEditingFinished5b(self):
        value = float(self.lineEdit_ohm_5b.text())
        multi = self.comboBox_ohm_5b.currentData()
        milli = False
        if multi == -3:
            ohm = int(value*10**3)/1000
            milli = True
        else:
            ohm = int(value*10**multi)
        digits = str(ohm)

        multiplier = self.calc_multiplier(5, digits, self.label_ohm_error_5b)

        self.comboBox_1d_5b.currentIndexChanged.disconnect()
        self.comboBox_2d_5b.currentIndexChanged.disconnect()
        self.comboBox_3d_5b.currentIndexChanged.disconnect()
        #self.comboBox_m_5b.currentIndexChanged.disconnect()
        
        self.comboBox_1d_5b.setCurrentIndex(int(digits[0]))

        print(
            value,
            " ",
            ohm,
            " ",
            int(multiplier),
            " ",
            self.comboBox_m_5b.findText(
                str(int(multiplier))+" mΩ", flags=Qc.Qt.MatchFlag.MatchExactly
            ),
        )

        if len(digits) > 1:
            self.comboBox_2d_5b.setCurrentIndex(int(digits[1]))
            self.comboBox_3d_5b.setCurrentIndex(int(digits[2]))
        if milli:
            idx = self.comboBox_m_5b.findText(
                str(int(multiplier))+" mΩ", flags=Qc.Qt.MatchFlag.MatchExactly
            )
        else:
            idx = self.comboBox_m_5b.findData(
                str(int(multiplier)), flags=Qc.Qt.MatchFlag.MatchFixedString
            )
        self.comboBox_m_5b.setCurrentIndex(idx )

        
        self.comboBox_1d_5b.currentIndexChanged.connect(self.calculate_res_5b)
        self.comboBox_2d_5b.currentIndexChanged.connect(self.calculate_res_5b)
        self.comboBox_3d_5b.currentIndexChanged.connect(self.calculate_res_5b)
        #self.comboBox_m_5b.currentIndexChanged.connect(self.calculate_res_5b)

    def initValidator(self, line):
        edit = Qg.QDoubleValidator()
        edit.setNotation(Qg.QDoubleValidator.StandardNotation)
        edit.setDecimals(2)
        edit.setLocale(Qc.QLocale.c())
        line.setValidator(edit)

    def calculate_res_5b(self):
        self.change_band_colors_5b()  # Update svg
        digit1 = self.comboBox_1d_5b.currentText()
        digit2 = self.comboBox_2d_5b.currentText()
        digit3 = self.comboBox_3d_5b.currentText()
        divisor = self.comboBox_m_5b.currentIndex()
        tolid = self.comboBox_t_5b.currentIndex()
        tolerance = self.json["tolerance"][tolid]["value"]
        mantissa = int(digit1 + digit2 + digit3)
        
        if divisor == 10:
            divisor = -2
        if divisor == 11:
            divisor = -3
            
        value, min_value, max_value, post_fix = gh.calculate_values(
            tolerance, mantissa, divisor
        )
        # r, attr = gh.edit_format_resistance(value, 3)
        self.lineEdit_resistance_5b.setText(f"{value}")
        self.label_resistance_5b.setText(f"{post_fix}")
        self.lineEdit_resistance_min_5b.setText(str(min_value))
        self.lineEdit_resistance_max_5b.setText(str(max_value))
        self.lineEdit_ohm_5b.setText(f"{value}")
        self.label_min_5b.setText(f"- {tolerance}%")
        self.label_max_5b.setText(f"+ {tolerance}%")

        self.comboBox_ohm_5b.setCurrentIndex(
            self.comboBox_ohm_5b.findText(post_fix, Qc.Qt.MatchFixedString)
        )

        return value, min_value, max_value
        # calculate_res_5b

    ####
    # calculates a multiplier from Ohm Edit input
    # @params:
    #   bands  (4 or 5)
    #   value ohm value string
    #   label where to show errors
    ####
    def calc_multiplier(self, bands, digits, label):
        if bands == 5:
            m = "1"
            if len(digits) > 3:
                # end = 3
                d = digits[2:]
                m = "1".ljust(len(d), "0")

                # end = len(digits) - 1
            # div = "".join(digits[0:end])

        # multiplier = int(int(digits) / int(div))
        # print("M: ", multiplier)
        # if "." in str(multiplier):
        #     error = "The value entered is not valid"
        #
        #     label.setText(error)
        #     m = "1".ljust(len(str(strmultiplier)) - 1, "0")
        #     print(m)
        # for i in range(len(str(int(multiplier))) - 1):
        #    m = m + "0"
        # else:
        #     m = "1".ljust(len(str(multiplier)) - 1, "0")
        #     print(m)

        return m

    def calculate_res_6b(self):
        self.change_band_colors_6b()  # Update svg
        digit1 = self.comboBox_1d_6b.currentText()
        digit2 = self.comboBox_2d_6b.currentText()
        digit3 = self.comboBox_3d_6b.currentText()
        divisor = self.comboBox_m_6b.currentIndex()
        tolid = self.comboBox_t_6b.currentIndex()
        tolerance = self.json["tolerance"][tolid]["value"]
        tcr = self.json["tolerance"][self.comboBox_tcr_6b.currentIndex()]["value"]

        mantissa = int(digit1 + digit2 + digit3)

        value, min_value, max_value, post_fix = gh.calculate_values(
            tolerance, mantissa, divisor
        )

        self.lineEdit_resistance_6b.setText(f"{value} ±{tolerance}")
        self.lineEdit_resistance_min_6b.setText(str(min_value))
        self.lineEdit_resistance_max_6b.setText(str(max_value))
        self.lineEdit_tcr_6b.setText(str(tcr) + " ppm/°C")

        return value, min_value, max_value, tcr
        # calculate_res_6b

    def calculate_res_smd(self):
        self.change_band_colors_smd()  # Update svg
        smd_code = self.smd_line_edit.text()
        line_under_short = self.radioButton_line_under_short.isChecked()
        line_under_long = self.radioButton_line_under_long.isChecked()
        # Top Line is irrelevant for the calculation and cosmetic only.
        # line_top = self.radioButton_line_top.isChecked()

        decoded = smd_parse.parse_code(smd_code, line_under_short, line_under_long)

        if decoded is not None:
            value, tolerance, is_standard_tolerance = decoded

            min_value = value * (1 - 0.01 * tolerance)
            max_value = value * (1 + 0.01 * tolerance)

            self.lineEdit_resistance_smd.setText(f"{value:.1f} ±{tolerance}%")
            self.lineEdit_resistance_min_smd.setText(f"{min_value:.1f}")
            self.lineEdit_resistance_max_smd.setText(f"{max_value:.1f}")

            # Hide notice if standardized
            self.label_tolerance_notice.setHidden(is_standard_tolerance)
            # Hide warnings
            self.label_code_invalid_icon.hide()
            self.label_code_invalid_label.hide()

            return value, min_value, max_value
        else:
            # Invalid code
            self.lineEdit_resistance_smd.clear()
            self.lineEdit_resistance_min_smd.clear()
            self.lineEdit_resistance_max_smd.clear()
            # Hide notice
            self.label_tolerance_notice.hide()
            # Show warnings
            self.label_code_invalid_icon.show()
            self.label_code_invalid_label.show()

            return None, None, None
        # calculate_res_smd

    def get_comboBox_data(self):
        err = Qc.QJsonParseError()
        jf = Qc.QFile(":/general/icon_data.json")
        jf.open(Qc.QIODevice.ReadOnly | Qc.QIODevice.Text)
        js = jf.readAll()
        self.icons = Qc.QJsonDocument.fromJson(js, error=err)

        print(err.errorString())

        self.json = self.icons.object()
        # print(self.json["digits"])

    def initCombosR(self):
        self.attachComboRs(1, self.comboBox_1d_4b, "digit")
        self.attachComboRs(2, self.comboBox_2d_4b, "digit")
        self.attachComboRs(3, self.comboBox_m_4b, "multiplier")
        self.attachComboRs(4, self.comboBox_t_4b, "tolerance")

        self.attachComboRs(1, self.comboBox_1d_5b, "digit")
        self.attachComboRs(2, self.comboBox_2d_5b, "digit")
        self.attachComboRs(3, self.comboBox_3d_5b, "digit")
        self.attachComboRs(4, self.comboBox_m_5b, "multiplier")
        self.attachComboRs(5, self.comboBox_t_5b, "tolerance")

        self.attachComboRs(1, self.comboBox_1d_6b, "digit")
        self.attachComboRs(2, self.comboBox_2d_6b, "digit")
        self.attachComboRs(3, self.comboBox_3d_6b, "digit")
        self.attachComboRs(4, self.comboBox_m_6b, "multiplier")
        self.attachComboRs(5, self.comboBox_t_6b, "tolerance")
        self.attachComboRs(6, self.comboBox_tcr_6b, "trc")

        self.comboBox_ohm_4b.addItems(["mΩ", "Ω", "kΩ", "MΩ"])
        self.comboBox_ohm_4b.setItemData(0, -3)
        self.comboBox_ohm_4b.setItemData(1, 0)
        self.comboBox_ohm_4b.setItemData(2, 3)
        self.comboBox_ohm_4b.setItemData(3, 6)
        self.comboBox_t_4b.setCurrentIndex(2)

        self.comboBox_ohm_5b.addItems(["mΩ", "Ω", "kΩ", "MΩ"])
        self.comboBox_ohm_5b.setItemData(0, -3)
        self.comboBox_ohm_5b.setItemData(1, 0)
        self.comboBox_ohm_5b.setItemData(2, 3)
        self.comboBox_ohm_5b.setItemData(3, 6)
        self.comboBox_t_5b.setCurrentIndex(2)

        self.comboBox_t_6b.setCurrentIndex(1)
        # Set the default divisor to 1
        self.comboBox_m_4b.setCurrentIndex(3)
        self.comboBox_m_5b.setCurrentIndex(3)
        self.comboBox_m_6b.setCurrentIndex(3)

        self.initValidator(self.lineEdit_ohm_4b)
        self.initValidator(self.lineEdit_ohm_5b)

    def attachComboRs(self, digit, combobox, typ):
        data = self.json["digits"]
        if typ == "digit":
            for i in range(0, len(data)):
                ico = data[i]
                combobox.addItem(Qg.QIcon(ico["icon"]), ico["idx"])

        if typ == "multiplier":
            data = self.json["multiplier"]
            for i in range(0, len(data)):
                ico = data[i]
                combobox.addItem(Qg.QIcon(ico["icon"]), ico["text"], ico["data"])
        if typ == "tolerance":
            data = self.json["tolerance"]
            for i in range(0, len(data)):
                ico = data[i]
                combobox.addItem(Qg.QIcon(ico["icon"]), ico["text"])
        if typ == "trc":
            data = self.json["trc"]
            for i in range(0, len(data)):
                ico = data[i]
                combobox.addItem(Qg.QIcon(ico["icon"]), str(ico["value"]))

    def open_license(self):
        if self.license_window is None:
            self.license_window = LicenseAgreement()
        self.license_window.show()