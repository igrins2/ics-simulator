# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ICSnBplmM.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGroupBox,
    QLabel, QLineEdit, QProgressBar, QPushButton,
    QRadioButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(638, 494)
        self.groupBox_5 = QGroupBox(Dialog)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(460, 120, 121, 201))
        self.chk_ROI_mode = QCheckBox(self.groupBox_5)
        self.chk_ROI_mode.setObjectName(u"chk_ROI_mode")
        self.chk_ROI_mode.setGeometry(QRect(20, 30, 85, 21))
        self.label_10 = QLabel(self.groupBox_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 160, 51, 21))
        self.label_10.setLayoutDirection(Qt.LeftToRight)
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.e_x_stop = QLineEdit(self.groupBox_5)
        self.e_x_stop.setObjectName(u"e_x_stop")
        self.e_x_stop.setGeometry(QRect(70, 100, 41, 23))
        self.e_x_stop.setAlignment(Qt.AlignCenter)
        self.label_11 = QLabel(self.groupBox_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 130, 51, 21))
        self.label_11.setLayoutDirection(Qt.LeftToRight)
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_12 = QLabel(self.groupBox_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 100, 51, 21))
        self.label_12.setLayoutDirection(Qt.LeftToRight)
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_14 = QLabel(self.groupBox_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 70, 51, 21))
        self.label_14.setLayoutDirection(Qt.LeftToRight)
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.e_y_stop = QLineEdit(self.groupBox_5)
        self.e_y_stop.setObjectName(u"e_y_stop")
        self.e_y_stop.setGeometry(QRect(70, 160, 41, 23))
        self.e_y_stop.setAlignment(Qt.AlignCenter)
        self.e_y_start = QLineEdit(self.groupBox_5)
        self.e_y_start.setObjectName(u"e_y_start")
        self.e_y_start.setGeometry(QRect(70, 130, 41, 23))
        self.e_y_start.setAlignment(Qt.AlignCenter)
        self.e_x_start = QLineEdit(self.groupBox_5)
        self.e_x_start.setObjectName(u"e_x_start")
        self.e_x_start.setGeometry(QRect(70, 70, 41, 23))
        self.e_x_start.setAlignment(Qt.AlignCenter)
        self.groupBox_4 = QGroupBox(Dialog)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(160, 120, 291, 151))
        self.e_reads = QLineEdit(self.groupBox_4)
        self.e_reads.setObjectName(u"e_reads")
        self.e_reads.setGeometry(QRect(90, 50, 41, 23))
        font = QFont()
        font.setPointSize(10)
        self.e_reads.setFont(font)
        self.e_reads.setAlignment(Qt.AlignCenter)
        self.e_resets = QLineEdit(self.groupBox_4)
        self.e_resets.setObjectName(u"e_resets")
        self.e_resets.setGeometry(QRect(40, 50, 41, 23))
        self.e_resets.setFont(font)
        self.e_resets.setAlignment(Qt.AlignCenter)
        self.e_groups = QLineEdit(self.groupBox_4)
        self.e_groups.setObjectName(u"e_groups")
        self.e_groups.setGeometry(QRect(140, 50, 41, 23))
        self.e_groups.setFont(font)
        self.e_groups.setAlignment(Qt.AlignCenter)
        self.e_drops = QLineEdit(self.groupBox_4)
        self.e_drops.setObjectName(u"e_drops")
        self.e_drops.setGeometry(QRect(190, 50, 41, 23))
        self.e_drops.setFont(font)
        self.e_drops.setAlignment(Qt.AlignCenter)
        self.e_ramps = QLineEdit(self.groupBox_4)
        self.e_ramps.setObjectName(u"e_ramps")
        self.e_ramps.setGeometry(QRect(240, 50, 41, 23))
        self.e_ramps.setFont(font)
        self.e_ramps.setAlignment(Qt.AlignCenter)
        self.btn_set_param = QPushButton(self.groupBox_4)
        self.btn_set_param.setObjectName(u"btn_set_param")
        self.btn_set_param.setGeometry(QRect(200, 90, 81, 51))
        self.e_fowler_number = QLineEdit(self.groupBox_4)
        self.e_fowler_number.setObjectName(u"e_fowler_number")
        self.e_fowler_number.setGeometry(QRect(130, 120, 61, 23))
        self.e_fowler_number.setAlignment(Qt.AlignCenter)
        self.e_exp_time = QLineEdit(self.groupBox_4)
        self.e_exp_time.setObjectName(u"e_exp_time")
        self.e_exp_time.setGeometry(QRect(130, 90, 61, 23))
        self.e_exp_time.setAlignment(Qt.AlignCenter)
        self.label_fowler_number = QLabel(self.groupBox_4)
        self.label_fowler_number.setObjectName(u"label_fowler_number")
        self.label_fowler_number.setGeometry(QRect(30, 120, 91, 21))
        self.label_fowler_number.setLayoutDirection(Qt.LeftToRight)
        self.label_fowler_number.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_13 = QLabel(self.groupBox_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(30, 90, 91, 21))
        self.label_13.setLayoutDirection(Qt.LeftToRight)
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_19 = QLabel(self.groupBox_4)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(35, 30, 51, 21))
        self.label_19.setFont(font)
        self.label_19.setLayoutDirection(Qt.LeftToRight)
        self.label_19.setAlignment(Qt.AlignCenter)
        self.label_20 = QLabel(self.groupBox_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(84, 30, 51, 21))
        self.label_20.setFont(font)
        self.label_20.setLayoutDirection(Qt.LeftToRight)
        self.label_20.setAlignment(Qt.AlignCenter)
        self.label_groups = QLabel(self.groupBox_4)
        self.label_groups.setObjectName(u"label_groups")
        self.label_groups.setGeometry(QRect(135, 30, 51, 21))
        self.label_groups.setFont(font)
        self.label_groups.setLayoutDirection(Qt.LeftToRight)
        self.label_groups.setAlignment(Qt.AlignCenter)
        self.label_drops = QLabel(self.groupBox_4)
        self.label_drops.setObjectName(u"label_drops")
        self.label_drops.setGeometry(QRect(185, 30, 51, 21))
        self.label_drops.setFont(font)
        self.label_drops.setLayoutDirection(Qt.LeftToRight)
        self.label_drops.setAlignment(Qt.AlignCenter)
        self.label_ramps = QLabel(self.groupBox_4)
        self.label_ramps.setObjectName(u"label_ramps")
        self.label_ramps.setGeometry(QRect(235, 30, 51, 21))
        self.label_ramps.setFont(font)
        self.label_ramps.setLayoutDirection(Qt.LeftToRight)
        self.label_ramps.setAlignment(Qt.AlignCenter)
        self.radio_exp_time = QRadioButton(self.groupBox_4)
        self.radio_exp_time.setObjectName(u"radio_exp_time")
        self.radio_exp_time.setGeometry(QRect(10, 90, 21, 25))
        self.radio_fowler_number = QRadioButton(self.groupBox_4)
        self.radio_fowler_number.setObjectName(u"radio_fowler_number")
        self.radio_fowler_number.setGeometry(QRect(10, 120, 21, 25))
        self.groupBox_6 = QGroupBox(Dialog)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(20, 330, 561, 141))
        self.label_18 = QLabel(self.groupBox_6)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 40, 181, 21))
        self.label_18.setLayoutDirection(Qt.LeftToRight)
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_measured_time = QLabel(self.groupBox_6)
        self.label_measured_time.setObjectName(u"label_measured_time")
        self.label_measured_time.setGeometry(QRect(200, 70, 191, 21))
        self.label_17 = QLabel(self.groupBox_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 70, 181, 21))
        self.label_17.setLayoutDirection(Qt.LeftToRight)
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_calculated_time = QLabel(self.groupBox_6)
        self.label_calculated_time.setObjectName(u"label_calculated_time")
        self.label_calculated_time.setGeometry(QRect(200, 40, 191, 21))
        self.prog_sts = QProgressBar(self.groupBox_6)
        self.prog_sts.setObjectName(u"prog_sts")
        self.prog_sts.setGeometry(QRect(20, 100, 521, 23))
        self.prog_sts.setValue(24)
        self.btn_stop = QPushButton(Dialog)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setGeometry(QRect(390, 280, 51, 41))
        self.btn_acquireramp = QPushButton(Dialog)
        self.btn_acquireramp.setObjectName(u"btn_acquireramp")
        self.btn_acquireramp.setGeometry(QRect(280, 280, 101, 41))
        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(20, 120, 131, 201))
        self.radio_UTR = QRadioButton(self.groupBox_3)
        self.radio_UTR.setObjectName(u"radio_UTR")
        self.radio_UTR.setGeometry(QRect(10, 40, 111, 21))
        self.radio_CDS = QRadioButton(self.groupBox_3)
        self.radio_CDS.setObjectName(u"radio_CDS")
        self.radio_CDS.setGeometry(QRect(10, 80, 100, 21))
        self.radio_CDSNoise = QRadioButton(self.groupBox_3)
        self.radio_CDSNoise.setObjectName(u"radio_CDSNoise")
        self.radio_CDSNoise.setGeometry(QRect(10, 120, 100, 21))
        self.radio_Fowler = QRadioButton(self.groupBox_3)
        self.radio_Fowler.setObjectName(u"radio_Fowler")
        self.radio_Fowler.setGeometry(QRect(10, 160, 100, 21))
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 10, 561, 101))
        self.btn_initialize1 = QPushButton(self.groupBox)
        self.btn_initialize1.setObjectName(u"btn_initialize1")
        self.btn_initialize1.setGeometry(QRect(120, 40, 81, 41))
        self.btn_download_MCD = QPushButton(self.groupBox)
        self.btn_download_MCD.setObjectName(u"btn_download_MCD")
        self.btn_download_MCD.setGeometry(QRect(320, 40, 111, 41))
        self.btn_initialize2 = QPushButton(self.groupBox)
        self.btn_initialize2.setObjectName(u"btn_initialize2")
        self.btn_initialize2.setGeometry(QRect(220, 40, 81, 41))
        self.btn_set_detector = QPushButton(self.groupBox)
        self.btn_set_detector.setObjectName(u"btn_set_detector")
        self.btn_set_detector.setGeometry(QRect(450, 40, 91, 41))
        self.label_connection_sts = QLabel(self.groupBox)
        self.label_connection_sts.setObjectName(u"label_connection_sts")
        self.label_connection_sts.setGeometry(QRect(30, 50, 51, 21))
        self.label_connection_sts.setLayoutDirection(Qt.LeftToRight)
        self.label_connection_sts.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Dialog", u"Window Mode", None))
        self.chk_ROI_mode.setText(QCoreApplication.translate("Dialog", u"ROI Mode", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Y stop:", None))
        self.e_x_stop.setText(QCoreApplication.translate("Dialog", u"2047", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Y start:", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"X stop:", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"X start:", None))
        self.e_y_stop.setText(QCoreApplication.translate("Dialog", u"2047", None))
        self.e_y_start.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.e_x_start.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog", u"Sampling Parameters", None))
        self.e_reads.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.e_resets.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.e_groups.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.e_drops.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.e_ramps.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.btn_set_param.setText(QCoreApplication.translate("Dialog", u"Set\n"
"Parameters", None))
        self.e_fowler_number.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.e_exp_time.setText(QCoreApplication.translate("Dialog", u"1.63", None))
        self.label_fowler_number.setText(QCoreApplication.translate("Dialog", u"N. Fowler:", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Exp. Time (s):", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"Resets", None))
        self.label_20.setText(QCoreApplication.translate("Dialog", u"Reads", None))
        self.label_groups.setText(QCoreApplication.translate("Dialog", u"Groups", None))
        self.label_drops.setText(QCoreApplication.translate("Dialog", u"Drops", None))
        self.label_ramps.setText(QCoreApplication.translate("Dialog", u"Ramps", None))
        self.radio_exp_time.setText("")
        self.radio_fowler_number.setText("")
        self.groupBox_6.setTitle(QCoreApplication.translate("Dialog", u"Acquiring Status", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"Calculated waiting time (s):", None))
        self.label_measured_time.setText(QCoreApplication.translate("Dialog", u"0.0", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"Measured waiting time (s):", None))
        self.label_calculated_time.setText(QCoreApplication.translate("Dialog", u"0.0", None))
        self.btn_stop.setText(QCoreApplication.translate("Dialog", u"Stop", None))
        self.btn_acquireramp.setText(QCoreApplication.translate("Dialog", u"AcquireRamp", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Sampling Mode", None))
        self.radio_UTR.setText(QCoreApplication.translate("Dialog", u"Up-The-Ramp", None))
        self.radio_CDS.setText(QCoreApplication.translate("Dialog", u"CDS", None))
        self.radio_CDSNoise.setText(QCoreApplication.translate("Dialog", u"CDS Noise", None))
        self.radio_Fowler.setText(QCoreApplication.translate("Dialog", u"Fowler", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Initializing", None))
        self.btn_initialize1.setText(QCoreApplication.translate("Dialog", u"Initialize1", None))
        self.btn_download_MCD.setText(QCoreApplication.translate("Dialog", u"DownloadMCD", None))
        self.btn_initialize2.setText(QCoreApplication.translate("Dialog", u"Initialize2", None))
        self.btn_set_detector.setText(QCoreApplication.translate("Dialog", u"SetDetector", None))
        self.label_connection_sts.setText(QCoreApplication.translate("Dialog", u"DCS", None))
    # retranslateUi
