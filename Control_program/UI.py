# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SALSA_UI.ui'
#
# Created: Thu Mar  3 16:19:34 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(802, 594)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 791, 541))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox_tc = QtGui.QGroupBox(self.tab)
        self.groupBox_tc.setGeometry(QtCore.QRect(20, 30, 751, 191))
        self.groupBox_tc.setObjectName(_fromUtf8("groupBox_tc"))
        self.layoutWidget = QtGui.QWidget(self.groupBox_tc)
        self.layoutWidget.setGeometry(QtCore.QRect(17, 30, 691, 151))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.coordlabel_right = QtGui.QLabel(self.layoutWidget)
        self.coordlabel_right.setObjectName(_fromUtf8("coordlabel_right"))
        self.horizontalLayout_7.addWidget(self.coordlabel_right)
        self.inputrightcoord = QtGui.QLineEdit(self.layoutWidget)
        self.inputrightcoord.setObjectName(_fromUtf8("inputrightcoord"))
        self.horizontalLayout_7.addWidget(self.inputrightcoord)
        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 2, 1, 1)
        self.line_3 = QtGui.QFrame(self.layoutWidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 2, 2, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_cur_az = QtGui.QLabel(self.layoutWidget)
        self.label_cur_az.setObjectName(_fromUtf8("label_cur_az"))
        self.horizontalLayout_3.addWidget(self.label_cur_az)
        self.cur_az = QtGui.QLineEdit(self.layoutWidget)
        self.cur_az.setReadOnly(True)
        self.cur_az.setObjectName(_fromUtf8("cur_az"))
        self.horizontalLayout_3.addWidget(self.cur_az)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 2, 1, 1)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_13.addWidget(self.label_2)
        self.offset_right = QtGui.QLineEdit(self.layoutWidget)
        self.offset_right.setReadOnly(False)
        self.offset_right.setObjectName(_fromUtf8("offset_right"))
        self.horizontalLayout_13.addWidget(self.offset_right)
        self.gridLayout.addLayout(self.horizontalLayout_13, 1, 2, 1, 1)
        self.line = QtGui.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        self.line_2 = QtGui.QFrame(self.layoutWidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 2, 1, 1, 1)
        self.label_offset = QtGui.QLabel(self.layoutWidget)
        self.label_offset.setObjectName(_fromUtf8("label_offset"))
        self.gridLayout.addWidget(self.label_offset, 1, 0, 1, 1)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_offset_left = QtGui.QLabel(self.layoutWidget)
        self.label_offset_left.setObjectName(_fromUtf8("label_offset_left"))
        self.horizontalLayout_11.addWidget(self.label_offset_left)
        self.offset_left = QtGui.QLineEdit(self.layoutWidget)
        self.offset_left.setReadOnly(False)
        self.offset_left.setObjectName(_fromUtf8("offset_left"))
        self.horizontalLayout_11.addWidget(self.offset_left)
        self.gridLayout.addLayout(self.horizontalLayout_11, 1, 1, 1, 1)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_cur_az_2 = QtGui.QLabel(self.layoutWidget)
        self.label_cur_az_2.setObjectName(_fromUtf8("label_cur_az_2"))
        self.horizontalLayout_10.addWidget(self.label_cur_az_2)
        self.calc_des_right = QtGui.QLineEdit(self.layoutWidget)
        self.calc_des_right.setReadOnly(True)
        self.calc_des_right.setObjectName(_fromUtf8("calc_des_right"))
        self.horizontalLayout_10.addWidget(self.calc_des_right)
        self.gridLayout.addLayout(self.horizontalLayout_10, 3, 2, 1, 1)
        self.btn_track = QtGui.QPushButton(self.layoutWidget)
        self.btn_track.setObjectName(_fromUtf8("btn_track"))
        self.gridLayout.addWidget(self.btn_track, 0, 3, 1, 1)
        self.label_currentaltaz = QtGui.QLabel(self.layoutWidget)
        self.label_currentaltaz.setObjectName(_fromUtf8("label_currentaltaz"))
        self.gridLayout.addWidget(self.label_currentaltaz, 4, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.coordlabel_left = QtGui.QLabel(self.layoutWidget)
        self.coordlabel_left.setObjectName(_fromUtf8("coordlabel_left"))
        self.horizontalLayout_6.addWidget(self.coordlabel_left)
        self.inputleftcoord = QtGui.QLineEdit(self.layoutWidget)
        self.inputleftcoord.setObjectName(_fromUtf8("inputleftcoord"))
        self.horizontalLayout_6.addWidget(self.inputleftcoord)
        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 1, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_newtarget = QtGui.QLabel(self.layoutWidget)
        self.label_newtarget.setObjectName(_fromUtf8("label_newtarget"))
        self.horizontalLayout_5.addWidget(self.label_newtarget)
        self.coordselector = QtGui.QComboBox(self.layoutWidget)
        self.coordselector.setObjectName(_fromUtf8("coordselector"))
        self.coordselector.addItem(_fromUtf8(""))
        self.coordselector.addItem(_fromUtf8(""))
        self.coordselector.addItem(_fromUtf8(""))
        self.coordselector.addItem(_fromUtf8(""))
        self.coordselector.addItem(_fromUtf8(""))
        self.coordselector.addItem(_fromUtf8(""))
        self.coordselector.addItem(_fromUtf8(""))
        self.coordselector.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.coordselector)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_cur_alt = QtGui.QLabel(self.layoutWidget)
        self.label_cur_alt.setObjectName(_fromUtf8("label_cur_alt"))
        self.horizontalLayout_2.addWidget(self.label_cur_alt)
        self.cur_alt = QtGui.QLineEdit(self.layoutWidget)
        self.cur_alt.setReadOnly(True)
        self.cur_alt.setObjectName(_fromUtf8("cur_alt"))
        self.horizontalLayout_2.addWidget(self.cur_alt)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 1, 1, 1)
        self.label_currentpointing = QtGui.QLabel(self.layoutWidget)
        self.label_currentpointing.setObjectName(_fromUtf8("label_currentpointing"))
        self.gridLayout.addWidget(self.label_currentpointing, 3, 0, 1, 1)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_cur_alt_2 = QtGui.QLabel(self.layoutWidget)
        self.label_cur_alt_2.setObjectName(_fromUtf8("label_cur_alt_2"))
        self.horizontalLayout_8.addWidget(self.label_cur_alt_2)
        self.calc_des_left = QtGui.QLineEdit(self.layoutWidget)
        self.calc_des_left.setReadOnly(True)
        self.calc_des_left.setObjectName(_fromUtf8("calc_des_left"))
        self.horizontalLayout_8.addWidget(self.calc_des_left)
        self.gridLayout.addLayout(self.horizontalLayout_8, 3, 1, 1, 1)
        self.btn_reset = QtGui.QPushButton(self.layoutWidget)
        self.btn_reset.setObjectName(_fromUtf8("btn_reset"))
        self.gridLayout.addWidget(self.btn_reset, 4, 3, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 230, 721, 261))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.tabWidget_2 = QtGui.QTabWidget(self.groupBox_3)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 20, 701, 231))
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.receiver_tab_basic = QtGui.QWidget()
        self.receiver_tab_basic.setObjectName(_fromUtf8("receiver_tab_basic"))
        self.layoutWidget1 = QtGui.QWidget(self.receiver_tab_basic)
        self.layoutWidget1.setGeometry(QtCore.QRect(16, 8, 486, 29))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.IntegrationTimeLabel = QtGui.QLabel(self.layoutWidget1)
        self.IntegrationTimeLabel.setObjectName(_fromUtf8("IntegrationTimeLabel"))
        self.horizontalLayout_4.addWidget(self.IntegrationTimeLabel)
        self.IntegrationTimeInput = QtGui.QSpinBox(self.layoutWidget1)
        self.IntegrationTimeInput.setMinimum(1)
        self.IntegrationTimeInput.setMaximum(3600)
        self.IntegrationTimeInput.setSingleStep(1)
        self.IntegrationTimeInput.setProperty("value", 10)
        self.IntegrationTimeInput.setObjectName(_fromUtf8("IntegrationTimeInput"))
        self.horizontalLayout_4.addWidget(self.IntegrationTimeInput)
        self.btn_observe = QtGui.QPushButton(self.layoutWidget1)
        self.btn_observe.setObjectName(_fromUtf8("btn_observe"))
        self.horizontalLayout_4.addWidget(self.btn_observe)
        self.btn_abort = QtGui.QPushButton(self.layoutWidget1)
        self.btn_abort.setDefault(False)
        self.btn_abort.setObjectName(_fromUtf8("btn_abort"))
        self.horizontalLayout_4.addWidget(self.btn_abort)
        self.progresslabel = QtGui.QLabel(self.receiver_tab_basic)
        self.progresslabel.setGeometry(QtCore.QRect(10, 60, 171, 23))
        self.progresslabel.setObjectName(_fromUtf8("progresslabel"))
        self.progressBar = QtGui.QProgressBar(self.receiver_tab_basic)
        self.progressBar.setGeometry(QtCore.QRect(196, 60, 491, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.tabWidget_2.addTab(self.receiver_tab_basic, _fromUtf8(""))
        self.receiver_tab_advanced = QtGui.QWidget()
        self.receiver_tab_advanced.setObjectName(_fromUtf8("receiver_tab_advanced"))
        self.layoutWidget2 = QtGui.QWidget(self.receiver_tab_advanced)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 10, 671, 185))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_mode = QtGui.QLabel(self.layoutWidget2)
        self.label_mode.setObjectName(_fromUtf8("label_mode"))
        self.gridLayout_2.addWidget(self.label_mode, 8, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox = QtGui.QGroupBox(self.layoutWidget2)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.layoutWidget3 = QtGui.QWidget(self.groupBox)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 0, 164, 24))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.mode_signal = QtGui.QRadioButton(self.layoutWidget3)
        self.mode_signal.setObjectName(_fromUtf8("mode_signal"))
        self.buttonGroup = QtGui.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.mode_signal)
        self.horizontalLayout.addWidget(self.mode_signal)
        self.mode_switched = QtGui.QRadioButton(self.layoutWidget3)
        self.mode_switched.setChecked(True)
        self.mode_switched.setObjectName(_fromUtf8("mode_switched"))
        self.buttonGroup.addButton(self.mode_switched)
        self.horizontalLayout.addWidget(self.mode_switched)
        self.gridLayout_3.addWidget(self.groupBox, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 8, 1, 1, 1)
        self.BandwidthLabel = QtGui.QLabel(self.layoutWidget2)
        self.BandwidthLabel.setObjectName(_fromUtf8("BandwidthLabel"))
        self.gridLayout_2.addWidget(self.BandwidthLabel, 2, 0, 1, 1)
        self.ChannelsInput = QtGui.QLineEdit(self.layoutWidget2)
        self.ChannelsInput.setObjectName(_fromUtf8("ChannelsInput"))
        self.gridLayout_2.addWidget(self.ChannelsInput, 3, 1, 1, 1)
        self.BandwidthInput = QtGui.QLineEdit(self.layoutWidget2)
        self.BandwidthInput.setObjectName(_fromUtf8("BandwidthInput"))
        self.gridLayout_2.addWidget(self.BandwidthInput, 2, 1, 1, 1)
        self.ChannelsLabel = QtGui.QLabel(self.layoutWidget2)
        self.ChannelsLabel.setObjectName(_fromUtf8("ChannelsLabel"))
        self.gridLayout_2.addWidget(self.ChannelsLabel, 3, 0, 1, 1)
        self.RefFreqLabel = QtGui.QLabel(self.layoutWidget2)
        self.RefFreqLabel.setObjectName(_fromUtf8("RefFreqLabel"))
        self.gridLayout_2.addWidget(self.RefFreqLabel, 9, 0, 1, 1)
        self.RefFreqInput = QtGui.QLineEdit(self.layoutWidget2)
        self.RefFreqInput.setObjectName(_fromUtf8("RefFreqInput"))
        self.gridLayout_2.addWidget(self.RefFreqInput, 9, 1, 1, 1)
        self.FrequencyLabel = QtGui.QLabel(self.layoutWidget2)
        self.FrequencyLabel.setObjectName(_fromUtf8("FrequencyLabel"))
        self.gridLayout_2.addWidget(self.FrequencyLabel, 0, 0, 1, 1)
        self.FrequencyInput = QtGui.QLineEdit(self.layoutWidget2)
        self.FrequencyInput.setObjectName(_fromUtf8("FrequencyInput"))
        self.gridLayout_2.addWidget(self.FrequencyInput, 0, 1, 1, 1)
        self.vlsr_checkbox = QtGui.QCheckBox(self.layoutWidget2)
        self.vlsr_checkbox.setEnabled(True)
        self.vlsr_checkbox.setChecked(True)
        self.vlsr_checkbox.setObjectName(_fromUtf8("vlsr_checkbox"))
        self.gridLayout_2.addWidget(self.vlsr_checkbox, 0, 2, 1, 1)
        self.autoedit_bad_data_checkBox = QtGui.QCheckBox(self.layoutWidget2)
        self.autoedit_bad_data_checkBox.setEnabled(True)
        self.autoedit_bad_data_checkBox.setChecked(True)
        self.autoedit_bad_data_checkBox.setObjectName(_fromUtf8("autoedit_bad_data_checkBox"))
        self.gridLayout_2.addWidget(self.autoedit_bad_data_checkBox, 2, 2, 1, 1)
        self.LNA_checkbox = QtGui.QCheckBox(self.layoutWidget2)
        self.LNA_checkbox.setEnabled(True)
        self.LNA_checkbox.setChecked(True)
        self.LNA_checkbox.setObjectName(_fromUtf8("LNA_checkbox"))
        self.gridLayout_2.addWidget(self.LNA_checkbox, 3, 2, 1, 1)
        self.noise_checkbox = QtGui.QCheckBox(self.layoutWidget2)
        self.noise_checkbox.setEnabled(True)
        self.noise_checkbox.setChecked(False)
        self.noise_checkbox.setObjectName(_fromUtf8("noise_checkbox"))
        self.gridLayout_2.addWidget(self.noise_checkbox, 8, 2, 1, 1)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label_gain = QtGui.QLabel(self.layoutWidget2)
        self.label_gain.setObjectName(_fromUtf8("label_gain"))
        self.horizontalLayout_14.addWidget(self.label_gain)
        self.gain = QtGui.QLineEdit(self.layoutWidget2)
        self.gain.setReadOnly(False)
        self.gain.setObjectName(_fromUtf8("gain"))
        self.horizontalLayout_14.addWidget(self.gain)
        self.gridLayout_2.addLayout(self.horizontalLayout_14, 9, 2, 1, 1)
        self.tabWidget_2.addTab(self.receiver_tab_advanced, _fromUtf8(""))
        self.infolabel = QtGui.QLabel(self.tab)
        self.infolabel.setGeometry(QtCore.QRect(30, 10, 671, 16))
        self.infolabel.setObjectName(_fromUtf8("infolabel"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.groupBox_spectrum = QtGui.QGroupBox(self.tab_2)
        self.groupBox_spectrum.setGeometry(QtCore.QRect(250, 20, 521, 461))
        self.groupBox_spectrum.setObjectName(_fromUtf8("groupBox_spectrum"))
        self.listWidget_spectra = QtGui.QListWidget(self.tab_2)
        self.listWidget_spectra.setGeometry(QtCore.QRect(20, 50, 211, 331))
        self.listWidget_spectra.setObjectName(_fromUtf8("listWidget_spectra"))
        self.btn_upload = QtGui.QPushButton(self.tab_2)
        self.btn_upload.setGeometry(QtCore.QRect(20, 390, 211, 41))
        self.btn_upload.setObjectName(_fromUtf8("btn_upload"))
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(20, 20, 231, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.layoutWidget4 = QtGui.QWidget(self.tab_2)
        self.layoutWidget4.setGeometry(QtCore.QRect(600, 0, 180, 24))
        self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
        self.vel_or_freq_group = QtGui.QHBoxLayout(self.layoutWidget4)
        self.vel_or_freq_group.setMargin(0)
        self.vel_or_freq_group.setObjectName(_fromUtf8("vel_or_freq_group"))
        self.radioButton_velocity = QtGui.QRadioButton(self.layoutWidget4)
        self.radioButton_velocity.setChecked(True)
        self.radioButton_velocity.setObjectName(_fromUtf8("radioButton_velocity"))
        self.vel_or_freq_group.addWidget(self.radioButton_velocity)
        self.radioButton_frequency = QtGui.QRadioButton(self.layoutWidget4)
        self.radioButton_frequency.setObjectName(_fromUtf8("radioButton_frequency"))
        self.vel_or_freq_group.addWidget(self.radioButton_frequency)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.layoutWidget5 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget5.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget5.setObjectName(_fromUtf8("layoutWidget5"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_9.setMargin(0)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.layoutWidget6 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget6.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget6.setObjectName(_fromUtf8("layoutWidget6"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget6)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.layoutWidget7 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget7.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget7.setObjectName(_fromUtf8("layoutWidget7"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.layoutWidget7)
        self.horizontalLayout_12.setMargin(0)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "SALSA Controller", None))
        self.groupBox_tc.setTitle(_translate("MainWindow", "Telescope movement control", None))
        self.coordlabel_right.setText(_translate("MainWindow", "Latitude", None))
        self.inputrightcoord.setText(_translate("MainWindow", "0", None))
        self.label_cur_az.setText(_translate("MainWindow", "Az:", None))
        self.cur_az.setText(_translate("MainWindow", "0", None))
        self.label_2.setText(_translate("MainWindow", "Az[deg]:", None))
        self.offset_right.setText(_translate("MainWindow", "0", None))
        self.label_offset.setText(_translate("MainWindow", "Desired horisontal offset", None))
        self.label_offset_left.setText(_translate("MainWindow", "Alt[deg]:", None))
        self.offset_left.setText(_translate("MainWindow", "0", None))
        self.label_cur_az_2.setText(_translate("MainWindow", "Az:", None))
        self.calc_des_right.setText(_translate("MainWindow", "0", None))
        self.btn_track.setText(_translate("MainWindow", "Track", None))
        self.label_currentaltaz.setText(_translate("MainWindow", "Current horizontal", None))
        self.coordlabel_left.setText(_translate("MainWindow", "Longitude", None))
        self.inputleftcoord.setText(_translate("MainWindow", "120", None))
        self.label_newtarget.setText(_translate("MainWindow", "Desired", None))
        self.coordselector.setItemText(0, _translate("MainWindow", "Galactic", None))
        self.coordselector.setItemText(1, _translate("MainWindow", "Horizontal", None))
        self.coordselector.setItemText(2, _translate("MainWindow", "Eq. J2000", None))
        self.coordselector.setItemText(3, _translate("MainWindow", "Eq. B1950", None))
        self.coordselector.setItemText(4, _translate("MainWindow", "The Sun", None))
        self.coordselector.setItemText(5, _translate("MainWindow", "The Moon", None))
        self.coordselector.setItemText(6, _translate("MainWindow", "Cas. A", None))
        self.coordselector.setItemText(7, _translate("MainWindow", "Stow", None))
        self.label_cur_alt.setText(_translate("MainWindow", "Alt:", None))
        self.cur_alt.setText(_translate("MainWindow", "0", None))
        self.label_currentpointing.setText(_translate("MainWindow", "Calc. target horizontal", None))
        self.label_cur_alt_2.setText(_translate("MainWindow", "Alt:", None))
        self.calc_des_left.setText(_translate("MainWindow", "0", None))
        self.btn_reset.setText(_translate("MainWindow", "Reset", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Receiver control", None))
        self.IntegrationTimeLabel.setText(_translate("MainWindow", "Target integration time [s]", None))
        self.btn_observe.setText(_translate("MainWindow", "Measure", None))
        self.btn_abort.setText(_translate("MainWindow", "Abort measurement", None))
        self.progresslabel.setText(_translate("MainWindow", "Measurement progress:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.receiver_tab_basic), _translate("MainWindow", "Basic", None))
        self.label_mode.setText(_translate("MainWindow", "Mode", None))
        self.mode_signal.setText(_translate("MainWindow", "Signal", None))
        self.mode_switched.setText(_translate("MainWindow", "Switched", None))
        self.BandwidthLabel.setText(_translate("MainWindow", "Bandwidth [MHz]", None))
        self.ChannelsInput.setText(_translate("MainWindow", "256", None))
        self.BandwidthInput.setText(_translate("MainWindow", "2.0", None))
        self.ChannelsLabel.setText(_translate("MainWindow", "Channels [#]", None))
        self.RefFreqLabel.setText(_translate("MainWindow", "Reference freq. [MHz]", None))
        self.RefFreqInput.setText(_translate("MainWindow", "1422.4", None))
        self.FrequencyLabel.setText(_translate("MainWindow", "Frequency [MHz]", None))
        self.FrequencyInput.setText(_translate("MainWindow", "1420.4", None))
        self.vlsr_checkbox.setText(_translate("MainWindow", "Translate to VLSR frame", None))
        self.autoedit_bad_data_checkBox.setText(_translate("MainWindow", "Remove RFI", None))
        self.LNA_checkbox.setText(_translate("MainWindow", "LNA", None))
        self.noise_checkbox.setText(_translate("MainWindow", "Noise diode", None))
        self.label_gain.setText(_translate("MainWindow", "Gain factor", None))
        self.gain.setText(_translate("MainWindow", "9000", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.receiver_tab_advanced), _translate("MainWindow", "Advanced", None))
        self.infolabel.setText(_translate("MainWindow", "Please: When finished, choose Desired=Stow and press \"Track\" to put telescope in stow position. ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Observe", None))
        self.groupBox_spectrum.setTitle(_translate("MainWindow", "Plot of selected spectrum", None))
        self.btn_upload.setText(_translate("MainWindow", "Upload selected to archive", None))
        self.label.setText(_translate("MainWindow", "List of measured spectra [date-UT]", None))
        self.radioButton_velocity.setText(_translate("MainWindow", "Velocity", None))
        self.radioButton_frequency.setText(_translate("MainWindow", "Frequency", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Measured spectra", None))

