# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'resistance_calccKFwyu.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resource_base_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(642, 420)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_5 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setDocumentMode(True)
        self.tab_4b = QWidget()
        self.tab_4b.setObjectName(u"tab_4b")
        self.verticalLayout_2 = QVBoxLayout(self.tab_4b)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4b_svg = QHBoxLayout()
        self.horizontalLayout_4b_svg.setObjectName(u"horizontalLayout_4b_svg")
        self.horizontalLayout_4b_svg.setContentsMargins(-1, -1, -1, 20)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4b_svg.addItem(self.horizontalSpacer_4)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4b_svg.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4b_svg)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(3)
        self.comboBox_m_4b = QComboBox(self.tab_4b)
        self.comboBox_m_4b.setObjectName(u"comboBox_m_4b")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox_m_4b.sizePolicy().hasHeightForWidth())
        self.comboBox_m_4b.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.comboBox_m_4b, 1, 2, 1, 1)

        self.label_4 = QLabel(self.tab_4b)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setTextFormat(Qt.TextFormat.RichText)

        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1)

        self.label_5 = QLabel(self.tab_4b)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 3, 1, 1)

        self.label_12 = QLabel(self.tab_4b)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 0, 2, 1, 1)

        self.comboBox_2d_4b = QComboBox(self.tab_4b)
        self.comboBox_2d_4b.setObjectName(u"comboBox_2d_4b")
        sizePolicy1.setHeightForWidth(self.comboBox_2d_4b.sizePolicy().hasHeightForWidth())
        self.comboBox_2d_4b.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.comboBox_2d_4b, 1, 1, 1, 1)

        self.comboBox_t_4b = QComboBox(self.tab_4b)
        self.comboBox_t_4b.setObjectName(u"comboBox_t_4b")
        sizePolicy1.setHeightForWidth(self.comboBox_t_4b.sizePolicy().hasHeightForWidth())
        self.comboBox_t_4b.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.comboBox_t_4b, 1, 3, 1, 1)

        self.label_3 = QLabel(self.tab_4b)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setTextFormat(Qt.TextFormat.RichText)

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.comboBox_1d_4b = QComboBox(self.tab_4b)
        self.comboBox_1d_4b.setObjectName(u"comboBox_1d_4b")
        sizePolicy1.setHeightForWidth(self.comboBox_1d_4b.sizePolicy().hasHeightForWidth())
        self.comboBox_1d_4b.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.comboBox_1d_4b, 1, 0, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 10)
        self.gridLayout_2.setColumnStretch(1, 10)
        self.gridLayout_2.setColumnStretch(2, 20)
        self.gridLayout_2.setColumnStretch(3, 20)

        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(6)
        self.lineEdit_resistance_4b = QLineEdit(self.tab_4b)
        self.lineEdit_resistance_4b.setObjectName(u"lineEdit_resistance_4b")
        self.lineEdit_resistance_4b.setStyleSheet(u"background-color: rgb(234, 234, 234);")
        self.lineEdit_resistance_4b.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_resistance_4b.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_resistance_4b, 1, 2, 1, 1)

        self.checkBox = QCheckBox(self.tab_4b)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 1, 1, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 1, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_7, 0, 0, 1, 1)

        self.label_2 = QLabel(self.tab_4b)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label = QLabel(self.tab_4b)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.lineEdit_resistance_max_4b = QLineEdit(self.tab_4b)
        self.lineEdit_resistance_max_4b.setObjectName(u"lineEdit_resistance_max_4b")
        self.lineEdit_resistance_max_4b.setStyleSheet(u"background-color: rgb(234, 234, 234);")
        self.lineEdit_resistance_max_4b.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_resistance_max_4b.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_resistance_max_4b, 3, 2, 1, 1)

        self.lineEdit_resistance_min_4b = QLineEdit(self.tab_4b)
        self.lineEdit_resistance_min_4b.setObjectName(u"lineEdit_resistance_min_4b")
        self.lineEdit_resistance_min_4b.setStyleSheet(u"background-color: rgb(234, 234, 234);")
        self.lineEdit_resistance_min_4b.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_resistance_min_4b.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_resistance_min_4b, 2, 2, 1, 1)

        self.label_11 = QLabel(self.tab_4b)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 1)

        self.label_resistance_4b = QLabel(self.tab_4b)
        self.label_resistance_4b.setObjectName(u"label_resistance_4b")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_resistance_4b.sizePolicy().hasHeightForWidth())
        self.label_resistance_4b.setSizePolicy(sizePolicy2)
        self.label_resistance_4b.setMinimumSize(QSize(100, 0))
        self.label_resistance_4b.setTextFormat(Qt.TextFormat.PlainText)

        self.gridLayout.addWidget(self.label_resistance_4b, 1, 3, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.tab_4b, "")
        self.tab_5b = QWidget()
        self.tab_5b.setObjectName(u"tab_5b")
        self.verticalLayout_12 = QVBoxLayout(self.tab_5b)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_5b_svg = QHBoxLayout()
        self.horizontalLayout_5b_svg.setObjectName(u"horizontalLayout_5b_svg")
        self.horizontalLayout_5b_svg.setContentsMargins(-1, -1, -1, 20)
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5b_svg.addItem(self.horizontalSpacer_6)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5b_svg.addItem(self.horizontalSpacer_7)


        self.verticalLayout_12.addLayout(self.horizontalLayout_5b_svg)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(10)
        self.gridLayout_4.setVerticalSpacing(3)
        self.label_8 = QLabel(self.tab_5b)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 0, 4, 1, 1)

        self.comboBox_1d_5b = QComboBox(self.tab_5b)
        self.comboBox_1d_5b.setObjectName(u"comboBox_1d_5b")
        sizePolicy1.setHeightForWidth(self.comboBox_1d_5b.sizePolicy().hasHeightForWidth())
        self.comboBox_1d_5b.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.comboBox_1d_5b, 1, 0, 1, 1)

        self.label_6 = QLabel(self.tab_5b)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setTextFormat(Qt.TextFormat.RichText)

        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_25 = QLabel(self.tab_5b)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setTextFormat(Qt.TextFormat.RichText)

        self.gridLayout_4.addWidget(self.label_25, 0, 2, 1, 1)

        self.label_7 = QLabel(self.tab_5b)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setTextFormat(Qt.TextFormat.RichText)

        self.gridLayout_4.addWidget(self.label_7, 0, 1, 1, 1)

        self.label_13 = QLabel(self.tab_5b)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_4.addWidget(self.label_13, 0, 3, 1, 1)

        self.comboBox_t_5b = QComboBox(self.tab_5b)
        self.comboBox_t_5b.setObjectName(u"comboBox_t_5b")
        sizePolicy1.setHeightForWidth(self.comboBox_t_5b.sizePolicy().hasHeightForWidth())
        self.comboBox_t_5b.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.comboBox_t_5b, 1, 4, 1, 1)

        self.comboBox_2d_5b = QComboBox(self.tab_5b)
        self.comboBox_2d_5b.setObjectName(u"comboBox_2d_5b")
        sizePolicy1.setHeightForWidth(self.comboBox_2d_5b.sizePolicy().hasHeightForWidth())
        self.comboBox_2d_5b.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.comboBox_2d_5b, 1, 1, 1, 1)

        self.comboBox_3d_5b = QComboBox(self.tab_5b)
        self.comboBox_3d_5b.setObjectName(u"comboBox_3d_5b")
        sizePolicy1.setHeightForWidth(self.comboBox_3d_5b.sizePolicy().hasHeightForWidth())
        self.comboBox_3d_5b.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.comboBox_3d_5b, 1, 2, 1, 1)

        self.comboBox_m_5b = QComboBox(self.tab_5b)
        self.comboBox_m_5b.setObjectName(u"comboBox_m_5b")
        sizePolicy1.setHeightForWidth(self.comboBox_m_5b.sizePolicy().hasHeightForWidth())
        self.comboBox_m_5b.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.comboBox_m_5b, 1, 3, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 10)
        self.gridLayout_4.setColumnStretch(1, 10)
        self.gridLayout_4.setColumnStretch(2, 10)
        self.gridLayout_4.setColumnStretch(3, 20)
        self.gridLayout_4.setColumnStretch(4, 20)

        self.verticalLayout_12.addLayout(self.gridLayout_4)

        self.verticalSpacer_4 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(10)
        self.gridLayout_3.setVerticalSpacing(6)
        self.label_9 = QLabel(self.tab_5b)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 1, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 1, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_8, 0, 0, 1, 1)

        self.lineEdit_resistance_max_5b = QLineEdit(self.tab_5b)
        self.lineEdit_resistance_max_5b.setObjectName(u"lineEdit_resistance_max_5b")
        self.lineEdit_resistance_max_5b.setStyleSheet(u"background-color: rgb(234, 234, 234);")
        self.lineEdit_resistance_max_5b.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_resistance_max_5b.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_resistance_max_5b, 3, 2, 1, 1)

        self.lineEdit_resistance_min_5b = QLineEdit(self.tab_5b)
        self.lineEdit_resistance_min_5b.setObjectName(u"lineEdit_resistance_min_5b")
        self.lineEdit_resistance_min_5b.setStyleSheet(u"background-color: rgb(234, 234, 234);")
        self.lineEdit_resistance_min_5b.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_resistance_min_5b.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_resistance_min_5b, 2, 2, 1, 1)

        self.lineEdit_resistance_5b = QLineEdit(self.tab_5b)
        self.lineEdit_resistance_5b.setObjectName(u"lineEdit_resistance_5b")
        self.lineEdit_resistance_5b.setStyleSheet(u"background-color: rgb(234, 234, 234);")
        self.lineEdit_resistance_5b.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_resistance_5b.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_resistance_5b, 1, 2, 1, 1)

        self.label_14 = QLabel(self.tab_5b)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_3.addWidget(self.label_14, 3, 0, 1, 1)

        self.label_10 = QLabel(self.tab_5b)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 2, 0, 1, 1)

        self.checkBox_5b = QCheckBox(self.tab_5b)
        self.checkBox_5b.setObjectName(u"checkBox_5b")

        self.gridLayout_3.addWidget(self.checkBox_5b, 1, 1, 1, 1)

        self.label_resistance_5b = QLabel(self.tab_5b)
        self.label_resistance_5b.setObjectName(u"label_resistance_5b")
        sizePolicy2.setHeightForWidth(self.label_resistance_5b.sizePolicy().hasHeightForWidth())
        self.label_resistance_5b.setSizePolicy(sizePolicy2)
        self.label_resistance_5b.setMinimumSize(QSize(100, 0))

        self.gridLayout_3.addWidget(self.label_resistance_5b, 1, 3, 1, 1)


        self.horizontalLayout_6.addLayout(self.gridLayout_3)

        self.horizontalSpacer_14 = QSpacerItem(53, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_14)


        self.verticalLayout_12.addLayout(self.horizontalLayout_6)

        self.tabWidget.addTab(self.tab_5b, "")
        self.tab_6b = QWidget()
        self.tab_6b.setObjectName(u"tab_6b")
        self.verticalLayout_7 = QVBoxLayout(self.tab_6b)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(9, 26, 9, 9)
        self.horizontalLayout_6b_svg = QHBoxLayout()
        self.horizontalLayout_6b_svg.setObjectName(u"horizontalLayout_6b_svg")
        self.horizontalLayout_6b_svg.setContentsMargins(-1, -1, -1, 20)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6b_svg.addItem(self.horizontalSpacer_8)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6b_svg.addItem(self.horizontalSpacer_9)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6b_svg)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(10)
        self.gridLayout_6.setVerticalSpacing(3)
        self.comboBox_m_6b = QComboBox(self.tab_6b)
        self.comboBox_m_6b.setObjectName(u"comboBox_m_6b")
        sizePolicy1.setHeightForWidth(self.comboBox_m_6b.sizePolicy().hasHeightForWidth())
        self.comboBox_m_6b.setSizePolicy(sizePolicy1)

        self.gridLayout_6.addWidget(self.comboBox_m_6b, 1, 3, 1, 1)

        self.comboBox_tcr_6b = QComboBox(self.tab_6b)
        self.comboBox_tcr_6b.setObjectName(u"comboBox_tcr_6b")
        sizePolicy1.setHeightForWidth(self.comboBox_tcr_6b.sizePolicy().hasHeightForWidth())
        self.comboBox_tcr_6b.setSizePolicy(sizePolicy1)

        self.gridLayout_6.addWidget(self.comboBox_tcr_6b, 1, 5, 1, 1)

        self.comboBox_2d_6b = QComboBox(self.tab_6b)
        self.comboBox_2d_6b.setObjectName(u"comboBox_2d_6b")
        sizePolicy1.setHeightForWidth(self.comboBox_2d_6b.sizePolicy().hasHeightForWidth())
        self.comboBox_2d_6b.setSizePolicy(sizePolicy1)

        self.gridLayout_6.addWidget(self.comboBox_2d_6b, 1, 1, 1, 1)

        self.label_18 = QLabel(self.tab_6b)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setTextFormat(Qt.TextFormat.RichText)

        self.gridLayout_6.addWidget(self.label_18, 0, 0, 1, 1)

        self.label_26 = QLabel(self.tab_6b)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setTextFormat(Qt.TextFormat.RichText)

        self.gridLayout_6.addWidget(self.label_26, 0, 2, 1, 1)

        self.label_20 = QLabel(self.tab_6b)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_6.addWidget(self.label_20, 0, 4, 1, 1)

        self.label_17 = QLabel(self.tab_6b)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_6.addWidget(self.label_17, 0, 3, 1, 1)

        self.comboBox_3d_6b = QComboBox(self.tab_6b)
        self.comboBox_3d_6b.setObjectName(u"comboBox_3d_6b")
        sizePolicy1.setHeightForWidth(self.comboBox_3d_6b.sizePolicy().hasHeightForWidth())
        self.comboBox_3d_6b.setSizePolicy(sizePolicy1)

        self.gridLayout_6.addWidget(self.comboBox_3d_6b, 1, 2, 1, 1)

        self.label_19 = QLabel(self.tab_6b)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setTextFormat(Qt.TextFormat.RichText)

        self.gridLayout_6.addWidget(self.label_19, 0, 1, 1, 1)

        self.comboBox_1d_6b = QComboBox(self.tab_6b)
        self.comboBox_1d_6b.setObjectName(u"comboBox_1d_6b")
        sizePolicy1.setHeightForWidth(self.comboBox_1d_6b.sizePolicy().hasHeightForWidth())
        self.comboBox_1d_6b.setSizePolicy(sizePolicy1)

        self.gridLayout_6.addWidget(self.comboBox_1d_6b, 1, 0, 1, 1)

        self.label_27 = QLabel(self.tab_6b)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_6.addWidget(self.label_27, 0, 5, 1, 1)

        self.comboBox_t_6b = QComboBox(self.tab_6b)
        self.comboBox_t_6b.setObjectName(u"comboBox_t_6b")
        sizePolicy1.setHeightForWidth(self.comboBox_t_6b.sizePolicy().hasHeightForWidth())
        self.comboBox_t_6b.setSizePolicy(sizePolicy1)

        self.gridLayout_6.addWidget(self.comboBox_t_6b, 1, 4, 1, 1)

        self.gridLayout_6.setColumnStretch(0, 10)
        self.gridLayout_6.setColumnStretch(1, 10)
        self.gridLayout_6.setColumnStretch(2, 10)
        self.gridLayout_6.setColumnStretch(3, 20)
        self.gridLayout_6.setColumnStretch(4, 20)
        self.gridLayout_6.setColumnStretch(5, 20)

        self.verticalLayout_7.addLayout(self.gridLayout_6)

        self.verticalSpacer_6 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setHorizontalSpacing(10)
        self.formLayout_3.setVerticalSpacing(6)
        self.verticalSpacer_12 = QSpacerItem(20, 1, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_3.setItem(0, QFormLayout.ItemRole.LabelRole, self.verticalSpacer_12)

        self.label_21 = QLabel(self.tab_6b)
        self.label_21.setObjectName(u"label_21")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_21)

        self.lineEdit_resistance_6b = QLineEdit(self.tab_6b)
        self.lineEdit_resistance_6b.setObjectName(u"lineEdit_resistance_6b")
        self.lineEdit_resistance_6b.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_resistance_6b.setReadOnly(True)

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEdit_resistance_6b)

        self.label_22 = QLabel(self.tab_6b)
        self.label_22.setObjectName(u"label_22")

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_22)

        self.lineEdit_resistance_min_6b = QLineEdit(self.tab_6b)
        self.lineEdit_resistance_min_6b.setObjectName(u"lineEdit_resistance_min_6b")
        self.lineEdit_resistance_min_6b.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_resistance_min_6b.setReadOnly(True)

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lineEdit_resistance_min_6b)

        self.label_23 = QLabel(self.tab_6b)
        self.label_23.setObjectName(u"label_23")

        self.formLayout_3.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_23)

        self.lineEdit_resistance_max_6b = QLineEdit(self.tab_6b)
        self.lineEdit_resistance_max_6b.setObjectName(u"lineEdit_resistance_max_6b")
        self.lineEdit_resistance_max_6b.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_resistance_max_6b.setReadOnly(True)

        self.formLayout_3.setWidget(3, QFormLayout.ItemRole.FieldRole, self.lineEdit_resistance_max_6b)

        self.label_28 = QLabel(self.tab_6b)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setTextFormat(Qt.TextFormat.RichText)
        self.label_28.setWordWrap(False)

        self.formLayout_3.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_28)

        self.lineEdit_tcr_6b = QLineEdit(self.tab_6b)
        self.lineEdit_tcr_6b.setObjectName(u"lineEdit_tcr_6b")
        self.lineEdit_tcr_6b.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_tcr_6b.setReadOnly(True)

        self.formLayout_3.setWidget(4, QFormLayout.ItemRole.FieldRole, self.lineEdit_tcr_6b)


        self.horizontalLayout_7.addLayout(self.formLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.tabWidget.addTab(self.tab_6b, "")
        self.tab_smd = QWidget()
        self.tab_smd.setObjectName(u"tab_smd")
        self.verticalLayout = QVBoxLayout(self.tab_smd)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 26, 9, 9)
        self.horizontalLayout_smd_svg = QHBoxLayout()
        self.horizontalLayout_smd_svg.setObjectName(u"horizontalLayout_smd_svg")
        self.horizontalLayout_smd_svg.setContentsMargins(-1, -1, -1, 20)
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_smd_svg.addItem(self.horizontalSpacer_10)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_smd_svg.addItem(self.horizontalSpacer_11)


        self.verticalLayout.addLayout(self.horizontalLayout_smd_svg)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.radioButton_line_none = QRadioButton(self.tab_smd)
        self.radioButton_line_none.setObjectName(u"radioButton_line_none")
        self.radioButton_line_none.setChecked(True)

        self.horizontalLayout_4.addWidget(self.radioButton_line_none)

        self.radioButton_line_under_short = QRadioButton(self.tab_smd)
        self.radioButton_line_under_short.setObjectName(u"radioButton_line_under_short")

        self.horizontalLayout_4.addWidget(self.radioButton_line_under_short)

        self.radioButton_line_under_long = QRadioButton(self.tab_smd)
        self.radioButton_line_under_long.setObjectName(u"radioButton_line_under_long")

        self.horizontalLayout_4.addWidget(self.radioButton_line_under_long)

        self.radioButton_line_top = QRadioButton(self.tab_smd)
        self.radioButton_line_top.setObjectName(u"radioButton_line_top")

        self.horizontalLayout_4.addWidget(self.radioButton_line_top)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_11 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_11)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_code_invalid_icon = QLabel(self.tab_smd)
        self.label_code_invalid_icon.setObjectName(u"label_code_invalid_icon")
        self.label_code_invalid_icon.setPixmap(QPixmap(u":/general/exclamation_red.png"))

        self.horizontalLayout_8.addWidget(self.label_code_invalid_icon)

        self.label_code_invalid_label = QLabel(self.tab_smd)
        self.label_code_invalid_label.setObjectName(u"label_code_invalid_label")
        self.label_code_invalid_label.setEnabled(True)

        self.horizontalLayout_8.addWidget(self.label_code_invalid_label)

        self.label_tolerance_notice = QLabel(self.tab_smd)
        self.label_tolerance_notice.setObjectName(u"label_tolerance_notice")
        self.label_tolerance_notice.setTextFormat(Qt.TextFormat.RichText)

        self.horizontalLayout_8.addWidget(self.label_tolerance_notice)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_12)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setHorizontalSpacing(10)
        self.formLayout_4.setVerticalSpacing(6)
        self.label_35 = QLabel(self.tab_smd)
        self.label_35.setObjectName(u"label_35")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_35)

        self.lineEdit_resistance_smd = QLineEdit(self.tab_smd)
        self.lineEdit_resistance_smd.setObjectName(u"lineEdit_resistance_smd")
        self.lineEdit_resistance_smd.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_resistance_smd.setReadOnly(True)

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEdit_resistance_smd)

        self.label_36 = QLabel(self.tab_smd)
        self.label_36.setObjectName(u"label_36")

        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_36)

        self.lineEdit_resistance_min_smd = QLineEdit(self.tab_smd)
        self.lineEdit_resistance_min_smd.setObjectName(u"lineEdit_resistance_min_smd")
        self.lineEdit_resistance_min_smd.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_resistance_min_smd.setReadOnly(True)

        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lineEdit_resistance_min_smd)

        self.label_37 = QLabel(self.tab_smd)
        self.label_37.setObjectName(u"label_37")

        self.formLayout_4.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_37)

        self.lineEdit_resistance_max_smd = QLineEdit(self.tab_smd)
        self.lineEdit_resistance_max_smd.setObjectName(u"lineEdit_resistance_max_smd")
        self.lineEdit_resistance_max_smd.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_resistance_max_smd.setReadOnly(True)

        self.formLayout_4.setWidget(3, QFormLayout.ItemRole.FieldRole, self.lineEdit_resistance_max_smd)

        self.verticalSpacer_9 = QSpacerItem(20, 1, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_4.setItem(0, QFormLayout.ItemRole.LabelRole, self.verticalSpacer_9)


        self.horizontalLayout.addLayout(self.formLayout_4)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_15)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.tab_smd, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tableWidget = QTableWidget(self.tab)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        font = QFont()
        font.setPointSize(14)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(110, 10, 351, 361))
        self.tabWidget.addTab(self.tab, "")
        self.about = QWidget()
        self.about.setObjectName(u"about")
        self.verticalLayout_5 = QVBoxLayout(self.about)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_about_title = QHBoxLayout()
        self.horizontalLayout_about_title.setSpacing(14)
        self.horizontalLayout_about_title.setObjectName(u"horizontalLayout_about_title")
        self.label_32 = QLabel(self.about)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setPixmap(QPixmap(u":/general/resistor_icon.svg"))

        self.horizontalLayout_about_title.addWidget(self.label_32)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_16 = QLabel(self.about)
        self.label_16.setObjectName(u"label_16")
        font1 = QFont()
        font1.setPointSize(16)
        self.label_16.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_16)

        self.label_24 = QLabel(self.about)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_3.addWidget(self.label_24)


        self.horizontalLayout_about_title.addLayout(self.verticalLayout_3)

        self.horizontalLayout_about_title.setStretch(1, 1)

        self.verticalLayout_5.addLayout(self.horizontalLayout_about_title)

        self.label_15 = QLabel(self.about)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setTextFormat(Qt.TextFormat.RichText)
        self.label_15.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_15)

        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_29 = QLabel(self.about)
        self.label_29.setObjectName(u"label_29")

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_29)

        self.label_30 = QLabel(self.about)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setTextFormat(Qt.TextFormat.RichText)

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.FieldRole, self.label_30)

        self.label_31 = QLabel(self.about)
        self.label_31.setObjectName(u"label_31")

        self.formLayout_5.setWidget(1, QFormLayout.ItemRole.FieldRole, self.label_31)

        self.label_38 = QLabel(self.about)
        self.label_38.setObjectName(u"label_38")

        self.formLayout_5.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_38)

        self.label_34 = QLabel(self.about)
        self.label_34.setObjectName(u"label_34")

        self.formLayout_5.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_34)

        self.label_39 = QLabel(self.about)
        self.label_39.setObjectName(u"label_39")

        self.formLayout_5.setWidget(2, QFormLayout.ItemRole.FieldRole, self.label_39)

        self.label_33 = QLabel(self.about)
        self.label_33.setObjectName(u"label_33")

        self.formLayout_5.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_33)

        self.label_40 = QLabel(self.about)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setTextFormat(Qt.TextFormat.RichText)
        self.label_40.setOpenExternalLinks(True)
        self.label_40.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.formLayout_5.setWidget(3, QFormLayout.ItemRole.FieldRole, self.label_40)


        self.verticalLayout_5.addLayout(self.formLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_license = QPushButton(self.about)
        self.pushButton_license.setObjectName(u"pushButton_license")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_license.sizePolicy().hasHeightForWidth())
        self.pushButton_license.setSizePolicy(sizePolicy3)

        self.horizontalLayout_2.addWidget(self.pushButton_license)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_13)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.about, "")

        self.horizontalLayout_5.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>2<span style=\" vertical-align:super;\">nd</span> Digit</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Tolerance", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Multiplier", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>1<span style=\" vertical-align:super;\">st</span> Digit</p></body></html>", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"edit", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Minimum", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Resistance", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Maximum", None))
        self.label_resistance_4b.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4b), QCoreApplication.translate("MainWindow", u"4 Band", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Tolerance", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>1<span style=\" vertical-align:super;\">st</span> Digit</p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>3<span style=\" vertical-align:super;\">rd</span> Digit</p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>2<span style=\" vertical-align:super;\">nd</span> Digit</p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Multiplier", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Resistance", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Maximum", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Minimum", None))
        self.checkBox_5b.setText(QCoreApplication.translate("MainWindow", u"edit", None))
        self.label_resistance_5b.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5b), QCoreApplication.translate("MainWindow", u"5 Band", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>1<span style=\" vertical-align:super;\">st</span> Digit</p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>3<span style=\" vertical-align:super;\">rd</span> Digit</p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Tolerance", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Multiplier", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>2<span style=\" vertical-align:super;\">nd</span> Digit</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.label_27.setToolTip(QCoreApplication.translate("MainWindow", u"Temperature Coefficient of Resistance", None))
#endif // QT_CONFIG(tooltip)
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"TCR", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Resistance", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Minimum", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Maximum", None))
#if QT_CONFIG(tooltip)
        self.label_28.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Temperature Coefficient of Resistance</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>TCR</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6b), QCoreApplication.translate("MainWindow", u"6 Band", None))
        self.radioButton_line_none.setText(QCoreApplication.translate("MainWindow", u"No line", None))
        self.radioButton_line_under_short.setText(QCoreApplication.translate("MainWindow", u"Short underline", None))
        self.radioButton_line_under_long.setText(QCoreApplication.translate("MainWindow", u"Long underline", None))
        self.radioButton_line_top.setText(QCoreApplication.translate("MainWindow", u"Long top bar", None))
        self.label_code_invalid_icon.setText("")
        self.label_code_invalid_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-style:italic; color:#ff0000;\">Invalid SMD code!</span></p></body></html>", None))
        self.label_tolerance_notice.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-style:italic;\">Notice: The tolerance value is only an estimate.</span></p></body></html>", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Resistance", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Minimum", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Maximum", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_smd), QCoreApplication.translate("MainWindow", u"SMD", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"E24", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"E48", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"E96", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"E-Series", None))
        self.label_32.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"ResistorEnDecode", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Version 1.1 2025", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>This is a standalone tool to decode the color bands on through-hole resistors and number codes on SMD parts. It supports 3, 4, 5, and 6 band resistors, as well as standard SMD codes, including the EIA-96 standard.</p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Libraries: ", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Qt 6.1.2 using PySide6</p></body></html>", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Python >=3.9.5", None))
        self.label_38.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Author:", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Voxel, AC", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Source:", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://github.com/AlfredoCubitos/ResistorEnDeCode\"><span style=\" text-decoration: underline; color:#2980b9;\">https://github.com/AlfredoCubitos/ResistorEnDeCode</span></a></p></body></html>", None))
        self.pushButton_license.setText(QCoreApplication.translate("MainWindow", u"License: GNU General Public License Version 3 and later", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.about), QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

