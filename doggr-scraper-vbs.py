# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doggr_scraper_2.ui'
#
# Created: Wed Aug 31 14:27:10 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

import pandas as pd
import numpy as np
from PyQt4 import QtCore, QtGui
import glob
import os
from matplotlibwidget import MatplotlibWidget
import warnings
import datetime as dt
import sys
from multiprocessing.dummy import Pool
from subprocess import call, Popen
from functools import partial

warnings.filterwarnings("ignore")

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

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(1261, 899)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 351, 771))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.layoutWidget = QtGui.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 479, 331, 16))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_32 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_32.setMargin(0)
        self.horizontalLayout_32.setObjectName(_fromUtf8("horizontalLayout_32"))
        self.label_30 = QtGui.QLabel(self.layoutWidget)
        self.label_30.setText(_fromUtf8(""))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.horizontalLayout_32.addWidget(self.label_30)
        self.label_31 = QtGui.QLabel(self.layoutWidget)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.horizontalLayout_32.addWidget(self.label_31)
        self.label_32 = QtGui.QLabel(self.layoutWidget)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.horizontalLayout_32.addWidget(self.label_32)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(11, 24, 33, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.comboBox_districtNumber = QtGui.QComboBox(self.groupBox)
        self.comboBox_districtNumber.setGeometry(QtCore.QRect(60, 24, 281, 20))
        self.comboBox_districtNumber.setObjectName(_fromUtf8("comboBox_districtNumber"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(11, 53, 22, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.comboBox_field = QtGui.QComboBox(self.groupBox)
        self.comboBox_field.setGeometry(QtCore.QRect(50, 53, 291, 20))
        self.comboBox_field.setObjectName(_fromUtf8("comboBox_field"))
        self.comboBox_fieldCode = QtGui.QComboBox(self.groupBox)
        self.comboBox_fieldCode.setGeometry(QtCore.QRect(80, 81, 261, 20))
        self.comboBox_fieldCode.setObjectName(_fromUtf8("comboBox_fieldCode"))
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(11, 81, 50, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.comboBox_operatorName = QtGui.QComboBox(self.groupBox)
        self.comboBox_operatorName.setGeometry(QtCore.QRect(100, 110, 241, 20))
        self.comboBox_operatorName.setObjectName(_fromUtf8("comboBox_operatorName"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(11, 110, 74, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.comboBox_operatorCode = QtGui.QComboBox(self.groupBox)
        self.comboBox_operatorCode.setGeometry(QtCore.QRect(99, 138, 241, 20))
        self.comboBox_operatorCode.setObjectName(_fromUtf8("comboBox_operatorCode"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(11, 138, 72, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.comboBox_sec = QtGui.QComboBox(self.groupBox)
        self.comboBox_sec.setGeometry(QtCore.QRect(60, 167, 281, 20))
        self.comboBox_sec.setObjectName(_fromUtf8("comboBox_sec"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(11, 167, 35, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.comboBox_twn = QtGui.QComboBox(self.groupBox)
        self.comboBox_twn.setGeometry(QtCore.QRect(71, 195, 271, 20))
        self.comboBox_twn.setObjectName(_fromUtf8("comboBox_twn"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(11, 195, 44, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.comboBox_rge = QtGui.QComboBox(self.groupBox)
        self.comboBox_rge.setGeometry(QtCore.QRect(60, 224, 281, 20))
        self.comboBox_rge.setObjectName(_fromUtf8("comboBox_rge"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(11, 224, 31, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.comboBox_apiNum = QtGui.QComboBox(self.groupBox)
        self.comboBox_apiNum.setGeometry(QtCore.QRect(50, 252, 291, 20))
        self.comboBox_apiNum.setObjectName(_fromUtf8("comboBox_apiNum"))
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(11, 252, 17, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.comboBox_lease = QtGui.QComboBox(self.groupBox)
        self.comboBox_lease.setGeometry(QtCore.QRect(60, 281, 281, 20))
        self.comboBox_lease.setObjectName(_fromUtf8("comboBox_lease"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(11, 281, 28, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.comboBox_wellName = QtGui.QComboBox(self.groupBox)
        self.comboBox_wellName.setGeometry(QtCore.QRect(50, 309, 291, 20))
        self.comboBox_wellName.setObjectName(_fromUtf8("comboBox_wellName"))
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(11, 309, 20, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(11, 338, 31, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.comboBox_status = QtGui.QComboBox(self.groupBox)
        self.comboBox_status.setGeometry(QtCore.QRect(60, 338, 281, 20))
        self.comboBox_status.setObjectName(_fromUtf8("comboBox_status"))
        self.label_13 = QtGui.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(11, 366, 23, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.comboBox_type = QtGui.QComboBox(self.groupBox)
        self.comboBox_type.setGeometry(QtCore.QRect(50, 366, 291, 20))
        self.comboBox_type.setObjectName(_fromUtf8("comboBox_type"))
        self.label_14 = QtGui.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(11, 395, 66, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.comboBox_bm = QtGui.QComboBox(self.groupBox)
        self.comboBox_bm.setGeometry(QtCore.QRect(90, 395, 251, 20))
        self.comboBox_bm.setObjectName(_fromUtf8("comboBox_bm"))
        self.label_15 = QtGui.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(11, 423, 56, 16))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.comboBox_areaName = QtGui.QComboBox(self.groupBox)
        self.comboBox_areaName.setGeometry(QtCore.QRect(80, 423, 261, 20))
        self.comboBox_areaName.setObjectName(_fromUtf8("comboBox_areaName"))
        self.label_16 = QtGui.QLabel(self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(11, 452, 54, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.comboBox_areaCode = QtGui.QComboBox(self.groupBox)
        self.comboBox_areaCode.setGeometry(QtCore.QRect(81, 452, 261, 20))
        self.comboBox_areaCode.setObjectName(_fromUtf8("comboBox_areaCode"))
        self.label_18 = QtGui.QLabel(self.groupBox)
        self.label_18.setGeometry(QtCore.QRect(10, 500, 39, 21))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.layoutWidget1 = QtGui.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(70, 500, 271, 22))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_17 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_17.setMargin(0)
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.lineEdit_latMin = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEdit_latMin.setObjectName(_fromUtf8("lineEdit_latMin"))
        self.horizontalLayout_17.addWidget(self.lineEdit_latMin)
        self.lineEdit_latMax = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEdit_latMax.setObjectName(_fromUtf8("lineEdit_latMax"))
        self.horizontalLayout_17.addWidget(self.lineEdit_latMax)
        self.label_19 = QtGui.QLabel(self.groupBox)
        self.label_19.setGeometry(QtCore.QRect(11, 529, 47, 20))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.layoutWidget2 = QtGui.QWidget(self.groupBox)
        self.layoutWidget2.setGeometry(QtCore.QRect(70, 530, 271, 22))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_18 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_18.setMargin(0)
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.lineEdit_lonMin = QtGui.QLineEdit(self.layoutWidget2)
        self.lineEdit_lonMin.setObjectName(_fromUtf8("lineEdit_lonMin"))
        self.horizontalLayout_18.addWidget(self.lineEdit_lonMin)
        self.lineEdit_lonMax = QtGui.QLineEdit(self.layoutWidget2)
        self.lineEdit_lonMax.setObjectName(_fromUtf8("lineEdit_lonMax"))
        self.horizontalLayout_18.addWidget(self.lineEdit_lonMax)
        self.label_20 = QtGui.QLabel(self.groupBox)
        self.label_20.setGeometry(QtCore.QRect(11, 558, 17, 16))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.comboBox_gis = QtGui.QComboBox(self.groupBox)
        self.comboBox_gis.setGeometry(QtCore.QRect(50, 558, 291, 20))
        self.comboBox_gis.setObjectName(_fromUtf8("comboBox_gis"))
        self.label_21 = QtGui.QLabel(self.groupBox)
        self.label_21.setGeometry(QtCore.QRect(11, 586, 31, 16))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.comboBox_datum = QtGui.QComboBox(self.groupBox)
        self.comboBox_datum.setGeometry(QtCore.QRect(60, 586, 281, 20))
        self.comboBox_datum.setObjectName(_fromUtf8("comboBox_datum"))
        self.label_22 = QtGui.QLabel(self.groupBox)
        self.label_22.setGeometry(QtCore.QRect(11, 615, 24, 16))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.comboBox_blm = QtGui.QComboBox(self.groupBox)
        self.comboBox_blm.setGeometry(QtCore.QRect(51, 615, 291, 20))
        self.comboBox_blm.setObjectName(_fromUtf8("comboBox_blm"))
        self.label_23 = QtGui.QLabel(self.groupBox)
        self.label_23.setGeometry(QtCore.QRect(11, 643, 22, 16))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.comboBox_dry = QtGui.QComboBox(self.groupBox)
        self.comboBox_dry.setGeometry(QtCore.QRect(50, 643, 291, 20))
        self.comboBox_dry.setObjectName(_fromUtf8("comboBox_dry"))
        self.label_25 = QtGui.QLabel(self.groupBox)
        self.label_25.setGeometry(QtCore.QRect(11, 700, 26, 16))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.comboBox_frac = QtGui.QComboBox(self.groupBox)
        self.comboBox_frac.setGeometry(QtCore.QRect(50, 700, 291, 20))
        self.comboBox_frac.setObjectName(_fromUtf8("comboBox_frac"))
        self.label_24 = QtGui.QLabel(self.groupBox)
        self.label_24.setGeometry(QtCore.QRect(11, 672, 55, 16))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.comboBox_direc = QtGui.QComboBox(self.groupBox)
        self.comboBox_direc.setGeometry(QtCore.QRect(80, 672, 261, 20))
        self.comboBox_direc.setObjectName(_fromUtf8("comboBox_direc"))
        self.label_17 = QtGui.QLabel(self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(11, 740, 82, 16))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_wellsSelected = QtGui.QLabel(self.groupBox)
        self.label_wellsSelected.setGeometry(QtCore.QRect(99, 740, 241, 16))
        self.label_wellsSelected.setObjectName(_fromUtf8("label_wellsSelected"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 790, 351, 81))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.layoutWidget3 = QtGui.QWidget(self.groupBox_2)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 10, 331, 66))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_33 = QtGui.QHBoxLayout()
        self.horizontalLayout_33.setObjectName(_fromUtf8("horizontalLayout_33"))
        self.label_33 = QtGui.QLabel(self.layoutWidget3)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.horizontalLayout_33.addWidget(self.label_33)
        self.lineEdit_filename = QtGui.QLineEdit(self.layoutWidget3)
        self.lineEdit_filename.setObjectName(_fromUtf8("lineEdit_filename"))
        self.horizontalLayout_33.addWidget(self.lineEdit_filename)
        self.verticalLayout_2.addLayout(self.horizontalLayout_33)
        self.horizontalLayout_47 = QtGui.QHBoxLayout()
        self.horizontalLayout_47.setObjectName(_fromUtf8("horizontalLayout_47"))
        self.pushButton_update = QtGui.QPushButton(self.layoutWidget3)
        self.pushButton_update.setObjectName(_fromUtf8("pushButton_update"))
        self.horizontalLayout_47.addWidget(self.pushButton_update)
        self.pushButton_process = QtGui.QPushButton(self.layoutWidget3)
        self.pushButton_process.setObjectName(_fromUtf8("pushButton_process"))
        self.horizontalLayout_47.addWidget(self.pushButton_process)
        self.pushButton_export = QtGui.QPushButton(self.layoutWidget3)
        self.pushButton_export.setObjectName(_fromUtf8("pushButton_export"))
        self.horizontalLayout_47.addWidget(self.pushButton_export)
        self.verticalLayout_2.addLayout(self.horizontalLayout_47)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(370, 10, 881, 861))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_mapsel = QtGui.QWidget()
        self.tab_mapsel.setObjectName(_fromUtf8("tab_mapsel"))
        self.matplotlibwidget_mapsel = MatplotlibWidget(self.tab_mapsel)
        self.matplotlibwidget_mapsel.setGeometry(QtCore.QRect(10, 10, 861, 791))
        self.matplotlibwidget_mapsel.setObjectName(_fromUtf8("matplotlibwidget_mapsel"))
        self.layoutWidget4 = QtGui.QWidget(self.tab_mapsel)
        self.layoutWidget4.setGeometry(QtCore.QRect(10, 810, 851, 24))
        self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
        self.horizontalLayout_38 = QtGui.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_38.setMargin(0)
        self.horizontalLayout_38.setObjectName(_fromUtf8("horizontalLayout_38"))
        self.horizontalLayout_31 = QtGui.QHBoxLayout()
        self.horizontalLayout_31.setObjectName(_fromUtf8("horizontalLayout_31"))
        self.label_41 = QtGui.QLabel(self.layoutWidget4)
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.horizontalLayout_31.addWidget(self.label_41)
        self.lineEdit_maplatMin_sel = QtGui.QLineEdit(self.layoutWidget4)
        self.lineEdit_maplatMin_sel.setObjectName(_fromUtf8("lineEdit_maplatMin_sel"))
        self.horizontalLayout_31.addWidget(self.lineEdit_maplatMin_sel)
        self.horizontalLayout_38.addLayout(self.horizontalLayout_31)
        self.horizontalLayout_35 = QtGui.QHBoxLayout()
        self.horizontalLayout_35.setObjectName(_fromUtf8("horizontalLayout_35"))
        self.label_39 = QtGui.QLabel(self.layoutWidget4)
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.horizontalLayout_35.addWidget(self.label_39)
        self.lineEdit_maplatMax_sel = QtGui.QLineEdit(self.layoutWidget4)
        self.lineEdit_maplatMax_sel.setObjectName(_fromUtf8("lineEdit_maplatMax_sel"))
        self.horizontalLayout_35.addWidget(self.lineEdit_maplatMax_sel)
        self.horizontalLayout_38.addLayout(self.horizontalLayout_35)
        self.horizontalLayout_36 = QtGui.QHBoxLayout()
        self.horizontalLayout_36.setObjectName(_fromUtf8("horizontalLayout_36"))
        self.label_29 = QtGui.QLabel(self.layoutWidget4)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.horizontalLayout_36.addWidget(self.label_29)
        self.lineEdit_maplonMin_sel = QtGui.QLineEdit(self.layoutWidget4)
        self.lineEdit_maplonMin_sel.setText(_fromUtf8(""))
        self.lineEdit_maplonMin_sel.setObjectName(_fromUtf8("lineEdit_maplonMin_sel"))
        self.horizontalLayout_36.addWidget(self.lineEdit_maplonMin_sel)
        self.horizontalLayout_38.addLayout(self.horizontalLayout_36)
        self.horizontalLayout_37 = QtGui.QHBoxLayout()
        self.horizontalLayout_37.setObjectName(_fromUtf8("horizontalLayout_37"))
        self.label_40 = QtGui.QLabel(self.layoutWidget4)
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.horizontalLayout_37.addWidget(self.label_40)
        self.lineEdit_maplonMax_sel = QtGui.QLineEdit(self.layoutWidget4)
        self.lineEdit_maplonMax_sel.setObjectName(_fromUtf8("lineEdit_maplonMax_sel"))
        self.horizontalLayout_37.addWidget(self.lineEdit_maplonMax_sel)
        self.horizontalLayout_38.addLayout(self.horizontalLayout_37)
        self.tabWidget.addTab(self.tab_mapsel, _fromUtf8(""))
        self.tab_plotsprod = QtGui.QWidget()
        self.tab_plotsprod.setObjectName(_fromUtf8("tab_plotsprod"))
        self.matplotlibwidget_rate = MatplotlibWidget(self.tab_plotsprod)
        self.matplotlibwidget_rate.setGeometry(QtCore.QRect(10, 70, 861, 371))
        self.matplotlibwidget_rate.setObjectName(_fromUtf8("matplotlibwidget_rate"))
        self.matplotlibwidget_cum = MatplotlibWidget(self.tab_plotsprod)
        self.matplotlibwidget_cum.setGeometry(QtCore.QRect(10, 450, 861, 371))
        self.matplotlibwidget_cum.setObjectName(_fromUtf8("matplotlibwidget_cum"))
        self.checkBox_ratePlot = QtGui.QCheckBox(self.tab_plotsprod)
        self.checkBox_ratePlot.setGeometry(QtCore.QRect(40, 40, 91, 21))
        self.checkBox_ratePlot.setObjectName(_fromUtf8("checkBox_ratePlot"))
        self.checkBox_cumPlot = QtGui.QCheckBox(self.tab_plotsprod)
        self.checkBox_cumPlot.setGeometry(QtCore.QRect(140, 40, 121, 21))
        self.checkBox_cumPlot.setObjectName(_fromUtf8("checkBox_cumPlot"))
        self.label_48 = QtGui.QLabel(self.tab_plotsprod)
        self.label_48.setGeometry(QtCore.QRect(250, 13, 43, 21))
        self.label_48.setObjectName(_fromUtf8("label_48"))
        self.pushButton_selectFile = QtGui.QPushButton(self.tab_plotsprod)
        self.pushButton_selectFile.setGeometry(QtCore.QRect(25, 13, 61, 23))
        self.pushButton_selectFile.setObjectName(_fromUtf8("pushButton_selectFile"))
        self.label_46 = QtGui.QLabel(self.tab_plotsprod)
        self.label_46.setGeometry(QtCore.QRect(90, 13, 43, 21))
        self.label_46.setObjectName(_fromUtf8("label_46"))
        self.comboBox_groupingPlot = QtGui.QComboBox(self.tab_plotsprod)
        self.comboBox_groupingPlot.setGeometry(QtCore.QRect(140, 14, 101, 20))
        self.comboBox_groupingPlot.setObjectName(_fromUtf8("comboBox_groupingPlot"))
        self.comboBox_selectionPlot = QtGui.QComboBox(self.tab_plotsprod)
        self.comboBox_selectionPlot.setGeometry(QtCore.QRect(300, 14, 181, 20))
        self.comboBox_selectionPlot.setObjectName(_fromUtf8("comboBox_selectionPlot"))
        self.label_50 = QtGui.QLabel(self.tab_plotsprod)
        self.label_50.setGeometry(QtCore.QRect(495, 13, 21, 21))
        self.label_50.setObjectName(_fromUtf8("label_50"))
        self.dateEdit_dateminPlot = QtGui.QDateEdit(self.tab_plotsprod)
        self.dateEdit_dateminPlot.setGeometry(QtCore.QRect(520, 14, 71, 20))
        self.dateEdit_dateminPlot.setObjectName(_fromUtf8("dateEdit_dateminPlot"))
        self.label_47 = QtGui.QLabel(self.tab_plotsprod)
        self.label_47.setGeometry(QtCore.QRect(600, 13, 31, 21))
        self.label_47.setObjectName(_fromUtf8("label_47"))
        self.dateEdit_datemaxPlot = QtGui.QDateEdit(self.tab_plotsprod)
        self.dateEdit_datemaxPlot.setGeometry(QtCore.QRect(630, 14, 71, 20))
        self.dateEdit_datemaxPlot.setObjectName(_fromUtf8("dateEdit_datemaxPlot"))
        self.pushButton_exportPlot = QtGui.QPushButton(self.tab_plotsprod)
        self.pushButton_exportPlot.setGeometry(QtCore.QRect(780, 13, 81, 23))
        self.pushButton_exportPlot.setObjectName(_fromUtf8("pushButton_exportPlot"))
        self.checkBox_oil = QtGui.QCheckBox(self.tab_plotsprod)
        self.checkBox_oil.setGeometry(QtCore.QRect(280, 40, 41, 21))
        self.checkBox_oil.setStyleSheet(_fromUtf8("background-color:#228B22;"))
        self.checkBox_oil.setObjectName(_fromUtf8("checkBox_oil"))
        self.checkBox_wtr = QtGui.QCheckBox(self.tab_plotsprod)
        self.checkBox_wtr.setGeometry(QtCore.QRect(330, 40, 51, 21))
        self.checkBox_wtr.setStyleSheet(_fromUtf8("background-color:#1E90FF;"))
        self.checkBox_wtr.setObjectName(_fromUtf8("checkBox_wtr"))
        self.checkBox_gas = QtGui.QCheckBox(self.tab_plotsprod)
        self.checkBox_gas.setGeometry(QtCore.QRect(390, 40, 41, 21))
        self.checkBox_gas.setStyleSheet(_fromUtf8("background-color:#FF6347"))
        self.checkBox_gas.setObjectName(_fromUtf8("checkBox_gas"))
        self.checkBox_stm = QtGui.QCheckBox(self.tab_plotsprod)
        self.checkBox_stm.setGeometry(QtCore.QRect(440, 40, 81, 21))
        self.checkBox_stm.setStyleSheet(_fromUtf8("background-color:#FF1493"))
        self.checkBox_stm.setObjectName(_fromUtf8("checkBox_stm"))
        self.checkBox_con = QtGui.QCheckBox(self.tab_plotsprod)
        self.checkBox_con.setGeometry(QtCore.QRect(530, 40, 111, 21))
        self.checkBox_con.setStyleSheet(_fromUtf8("background-color:#DC143C"))
        self.checkBox_con.setObjectName(_fromUtf8("checkBox_con"))
        self.checkBox_cyc = QtGui.QCheckBox(self.tab_plotsprod)
        self.checkBox_cyc.setGeometry(QtCore.QRect(650, 40, 81, 21))
        self.checkBox_cyc.setStyleSheet(_fromUtf8("background-color:#FFD700\n"
""))
        self.checkBox_cyc.setObjectName(_fromUtf8("checkBox_cyc"))
        self.checkBox_win = QtGui.QCheckBox(self.tab_plotsprod)
        self.checkBox_win.setGeometry(QtCore.QRect(740, 40, 101, 21))
        self.checkBox_win.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_win.setStyleSheet(_fromUtf8("background-color:#48D1CC;\n"
"text: center"))
        self.checkBox_win.setObjectName(_fromUtf8("checkBox_win"))
        self.tabWidget.addTab(self.tab_plotsprod, _fromUtf8(""))
        self.tab_mapprod = QtGui.QWidget()
        self.tab_mapprod.setObjectName(_fromUtf8("tab_mapprod"))
        self.matplotlibwidget_mapprod = MatplotlibWidget(self.tab_mapprod)
        self.matplotlibwidget_mapprod.setGeometry(QtCore.QRect(10, 10, 861, 791))
        self.matplotlibwidget_mapprod.setObjectName(_fromUtf8("matplotlibwidget_mapprod"))
        self.layoutWidget_5 = QtGui.QWidget(self.tab_mapprod)
        self.layoutWidget_5.setGeometry(QtCore.QRect(10, 810, 851, 24))
        self.layoutWidget_5.setObjectName(_fromUtf8("layoutWidget_5"))
        self.horizontalLayout_43 = QtGui.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_43.setMargin(0)
        self.horizontalLayout_43.setObjectName(_fromUtf8("horizontalLayout_43"))
        self.horizontalLayout_57 = QtGui.QHBoxLayout()
        self.horizontalLayout_57.setObjectName(_fromUtf8("horizontalLayout_57"))
        self.label_45 = QtGui.QLabel(self.layoutWidget_5)
        self.label_45.setObjectName(_fromUtf8("label_45"))
        self.horizontalLayout_57.addWidget(self.label_45)
        self.lineEdit_maplatMin_prod = QtGui.QLineEdit(self.layoutWidget_5)
        self.lineEdit_maplatMin_prod.setObjectName(_fromUtf8("lineEdit_maplatMin_prod"))
        self.horizontalLayout_57.addWidget(self.lineEdit_maplatMin_prod)
        self.horizontalLayout_43.addLayout(self.horizontalLayout_57)
        self.horizontalLayout_58 = QtGui.QHBoxLayout()
        self.horizontalLayout_58.setObjectName(_fromUtf8("horizontalLayout_58"))
        self.label_54 = QtGui.QLabel(self.layoutWidget_5)
        self.label_54.setObjectName(_fromUtf8("label_54"))
        self.horizontalLayout_58.addWidget(self.label_54)
        self.lineEdit_maplatMax_prod = QtGui.QLineEdit(self.layoutWidget_5)
        self.lineEdit_maplatMax_prod.setObjectName(_fromUtf8("lineEdit_maplatMax_prod"))
        self.horizontalLayout_58.addWidget(self.lineEdit_maplatMax_prod)
        self.horizontalLayout_43.addLayout(self.horizontalLayout_58)
        self.horizontalLayout_59 = QtGui.QHBoxLayout()
        self.horizontalLayout_59.setObjectName(_fromUtf8("horizontalLayout_59"))
        self.label_35 = QtGui.QLabel(self.layoutWidget_5)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.horizontalLayout_59.addWidget(self.label_35)
        self.lineEdit_maplonMin_prod = QtGui.QLineEdit(self.layoutWidget_5)
        self.lineEdit_maplonMin_prod.setText(_fromUtf8(""))
        self.lineEdit_maplonMin_prod.setObjectName(_fromUtf8("lineEdit_maplonMin_prod"))
        self.horizontalLayout_59.addWidget(self.lineEdit_maplonMin_prod)
        self.horizontalLayout_43.addLayout(self.horizontalLayout_59)
        self.horizontalLayout_60 = QtGui.QHBoxLayout()
        self.horizontalLayout_60.setObjectName(_fromUtf8("horizontalLayout_60"))
        self.label_55 = QtGui.QLabel(self.layoutWidget_5)
        self.label_55.setObjectName(_fromUtf8("label_55"))
        self.horizontalLayout_60.addWidget(self.label_55)
        self.lineEdit_maplonMax_prod = QtGui.QLineEdit(self.layoutWidget_5)
        self.lineEdit_maplonMax_prod.setObjectName(_fromUtf8("lineEdit_maplonMax_prod"))
        self.horizontalLayout_60.addWidget(self.lineEdit_maplonMax_prod)
        self.horizontalLayout_43.addLayout(self.horizontalLayout_60)
        self.tabWidget.addTab(self.tab_mapprod, _fromUtf8(""))
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "DOGGR Production Tool", None))
        self.groupBox.setTitle(_translate("mainWindow", "DOGGR Criteria", None))
        self.label_31.setText(_translate("mainWindow", "Min", None))
        self.label_32.setText(_translate("mainWindow", "         Max", None))
        self.label.setText(_translate("mainWindow", "District", None))
        self.label_2.setText(_translate("mainWindow", "Field", None))
        self.label_9.setText(_translate("mainWindow", "Field Code", None))
        self.label_4.setText(_translate("mainWindow", "Operator Name", None))
        self.label_5.setText(_translate("mainWindow", "Operator Code", None))
        self.label_6.setText(_translate("mainWindow", "Section", None))
        self.label_7.setText(_translate("mainWindow", "Township", None))
        self.label_8.setText(_translate("mainWindow", "Range", None))
        self.label_10.setText(_translate("mainWindow", "API", None))
        self.label_3.setText(_translate("mainWindow", "Lease", None))
        self.label_11.setText(_translate("mainWindow", "Well", None))
        self.label_12.setText(_translate("mainWindow", "Status", None))
        self.label_13.setText(_translate("mainWindow", "Type", None))
        self.label_14.setText(_translate("mainWindow", "Base Meridian", None))
        self.label_15.setText(_translate("mainWindow", "Area  Name", None))
        self.label_16.setText(_translate("mainWindow", "Area  Code", None))
        self.label_18.setText(_translate("mainWindow", "Latitude", None))
        self.label_19.setText(_translate("mainWindow", "Longitude", None))
        self.label_20.setText(_translate("mainWindow", "GIS", None))
        self.label_21.setText(_translate("mainWindow", "Datum", None))
        self.label_22.setText(_translate("mainWindow", "BLM?", None))
        self.label_23.setText(_translate("mainWindow", "Dry?", None))
        self.label_25.setText(_translate("mainWindow", "Frac?", None))
        self.label_24.setText(_translate("mainWindow", "Directional?", None))
        self.label_17.setText(_translate("mainWindow", "Wells in Selection", None))
        self.label_wellsSelected.setText(_translate("mainWindow", "replace!", None))
        self.label_33.setText(_translate("mainWindow", "File Name Appendix", None))
        self.pushButton_update.setText(_translate("mainWindow", "Update DOGGR\n"
"Selections", None))
        self.pushButton_process.setText(_translate("mainWindow", "Process\n"
"Selections", None))
        self.pushButton_export.setText(_translate("mainWindow", "Export Selection\n"
"Map", None))
        self.label_41.setText(_translate("mainWindow", "Latitude Min", None))
        self.label_39.setText(_translate("mainWindow", "Latitude Max", None))
        self.label_29.setText(_translate("mainWindow", "Longitude Min", None))
        self.label_40.setText(_translate("mainWindow", "Longitude Max", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_mapsel), _translate("mainWindow", "Selection Map", None))
        self.checkBox_ratePlot.setText(_translate("mainWindow", "Rate Log Scale", None))
        self.checkBox_cumPlot.setText(_translate("mainWindow", "Cumulative Log Scale", None))
        self.label_48.setText(_translate("mainWindow", "Selection", None))
        self.pushButton_selectFile.setText(_translate("mainWindow", "Select File", None))
        self.label_46.setText(_translate("mainWindow", "Grouping", None))
        self.label_50.setText(_translate("mainWindow", "Min", None))
        self.label_47.setText(_translate("mainWindow", "Max", None))
        self.pushButton_exportPlot.setText(_translate("mainWindow", "Export Plots", None))
        self.checkBox_oil.setText(_translate("mainWindow", "Oil", None))
        self.checkBox_wtr.setText(_translate("mainWindow", "Water", None))
        self.checkBox_gas.setText(_translate("mainWindow", "Gas", None))
        self.checkBox_stm.setText(_translate("mainWindow", "Total Steam", None))
        self.checkBox_con.setText(_translate("mainWindow", "Continuous Steam", None))
        self.checkBox_cyc.setText(_translate("mainWindow", "Cyclic Steam", None))
        self.checkBox_win.setText(_translate("mainWindow", "Water Injection", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_plotsprod), _translate("mainWindow", "Production Plots", None))
        self.label_45.setText(_translate("mainWindow", "Latitude Min", None))
        self.label_54.setText(_translate("mainWindow", "Latitude Max", None))
        self.label_35.setText(_translate("mainWindow", "Longitude Min", None))
        self.label_55.setText(_translate("mainWindow", "Longitude Max", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_mapprod), _translate("mainWindow", "Cumulative Production Map", None))
        
##########################  FUNCTIONAL CODE BELOW HERE  #############################
        
        print('#############################################################################')
        print('#-----------------------      DOGGR SCRAPER TOOL       ---------------------#')
        print('#----------------------------      CHEVRON       ---------------------------#')
        print('#############################################################################')
        print('#--- Updated: 09-13-16 --------------------- Questions: bvjs@chevron.com ---#')
        print('#############################################################################')
        print('#                     Loading GUI... Please be patient!                     #')
        print('#             *** Closing this window will shut down tool! ***              #')
        print('#                          *** SSL not verified ***                         #')
        print('#############################################################################')
        print('#                            Checking directories                           #')
        print('#---------------------------------------------------------------------------#')
        if not os.path.exists('sys/'):
            os.makedirs('sys/')    
            print('#                              -sys/ created                                #')
        else:
            print('#                              -sys/ exists                                 #')
        if not os.path.exists('wells/'):
            os.makedirs('wells/')    
            print('#                              -wells/ created                              #')
        else:
            print('#                              -wells/ exists                               #')
        if not os.path.exists('exports/'):
            os.makedirs('exports/')    
            print('#                              -exports/ created                            #')
        else:
            print('#                              -exports/ exists                             #')
        if not os.path.exists('plots/'):
            os.makedirs('plots/')    
            print('#                              -plots/ created                              #')
        else:
            print('#                              -plots/ exists                               #')    
        print('#############################################################################')
        print('#                           Checking selection files                        #')
        if len(glob.glob('selections/*.csv')) == 0:   
            print('#    No selection files found...  Creating selection file... Be patient!    #')
            print('#############################################################################')
            self.updateDoggrSelections()
        else:
            print('#                             Selection files found                         #')
            
        print('#############################################################################')
        print('#                            Choose selection file                          #')
        print('#############################################################################')

        self.readSelections()
        self.selections = self.results.copy(deep=True)
        self.apilist = self.selections['API #'].unique()
        self.label_wellsSelected.setText(_translate("MainWindow", str(len(self.selections)), None))
        self.lineEdit_filename.setText('default')
        self.fileName = 'test'
        self.districtNumber_idx = 'All'
        self.field_idx = 'All'
        self.fieldCode_idx = 'All'
        self.operatorName_idx = 'All'
        self.operatorCode_idx = 'All'
        self.sec_idx = 'All'
        self.twn_idx = 'All'
        self.rge_idx = 'All'
        self.apiNum_idx = 'All'
        self.lease_idx = 'All'
        self.wellName_idx = 'All'
        self.status_idx = 'All'
        self.type_idx = 'All'
        self.bm_idx = 'All'
        self.areaName_idx = 'All'
        self.areaCode_idx = 'All'
        self.latMin_idx = ''
        self.latMax_idx = ''
        self.lonMin_idx = ''
        self.lonMax_idx = ''
        self.gis_idx = 'All'
        self.datum_idx = 'All'
        self.blm_idx = 'All'
        self.dry_idx = 'All'
        self.direc_idx = 'All'
        self.frac_idx = 'All'
        self.groupingPlot_idx = 'None'
        self.selectionPlot_idx = 'None'
        self.selectionPlot_idx = 'None'
        self.checkBox_ratePlot.setChecked(True)
        self.checkBox_cumPlot.setChecked(True)
        self.checkBox_oil.setChecked(True)
        self.checkBox_wtr.setChecked(True)
        self.checkBox_gas.setChecked(True)
        self.checkBox_stm.setChecked(True)
        self.checkBox_con.setChecked(True)
        self.checkBox_cyc.setChecked(True)
        self.checkBox_win.setChecked(True)
        self.comboBox_groupingPlot.addItem('None')
        for idx, val in enumerate(['Field Name','Section','Township','Range','Operator Name','Lease Name','API10','Well','Spud Year','Pool Code']):
            self.comboBox_groupingPlot.addItem(val)
        self.makeMapSel()
        self.buildComboboxes()
        self.comboBox_districtNumber.activated[str].connect(self.updateSelection)
        self.comboBox_field.activated[str].connect(self.updateSelection)
        self.comboBox_fieldCode.activated[str].connect(self.updateSelection)
        self.comboBox_operatorName.activated[str].connect(self.updateSelection)
        self.comboBox_operatorCode.activated[str].connect(self.updateSelection)
        self.comboBox_sec.activated[str].connect(self.updateSelection)
        self.comboBox_twn.activated[str].connect(self.updateSelection)
        self.comboBox_rge.activated[str].connect(self.updateSelection)
        self.comboBox_apiNum.activated[str].connect(self.updateSelection)
        self.comboBox_lease.activated[str].connect(self.updateSelection)
        self.comboBox_wellName.activated[str].connect(self.updateSelection)
        self.comboBox_status.activated[str].connect(self.updateSelection)
        self.comboBox_type.activated[str].connect(self.updateSelection)
        self.comboBox_bm.activated[str].connect(self.updateSelection)
        self.comboBox_areaName.activated[str].connect(self.updateSelection)
        self.comboBox_areaCode.activated[str].connect(self.updateSelection)
        self.lineEdit_latMin.editingFinished.connect(self.updateSelection)
        self.lineEdit_latMax.editingFinished.connect(self.updateSelection)
        self.lineEdit_lonMin.editingFinished.connect(self.updateSelection)
        self.lineEdit_lonMax.editingFinished.connect(self.updateSelection)
        self.comboBox_gis.activated[str].connect(self.updateSelection)
        self.comboBox_datum.activated[str].connect(self.updateSelection)
        self.comboBox_blm.activated[str].connect(self.updateSelection)
        self.comboBox_dry.activated[str].connect(self.updateSelection)
        self.comboBox_direc.activated[str].connect(self.updateSelection)
        self.comboBox_frac.activated[str].connect(self.updateSelection)
        self.pushButton_update.clicked.connect(self.updateDoggrSelections)
        self.pushButton_process.clicked.connect(self.processSelections)
        self.lineEdit_maplatMin_sel.editingFinished.connect(self.makeMapSel)
        self.lineEdit_maplatMax_sel.editingFinished.connect(self.makeMapSel)
        self.lineEdit_maplonMin_sel.editingFinished.connect(self.makeMapSel)
        self.lineEdit_maplonMax_sel.editingFinished.connect(self.makeMapSel)
        self.comboBox_groupingPlot.activated[str].connect(self.updateProdSelections)
        self.comboBox_selectionPlot.activated[str].connect(self.updateProdData)
        self.dateEdit_dateminPlot.dateChanged.connect(self.updateProdData)
        self.dateEdit_datemaxPlot.dateChanged.connect(self.updateProdData)
        self.checkBox_ratePlot.stateChanged.connect(self.updateProdData)
        self.checkBox_cumPlot.stateChanged.connect(self.updateProdData)
        self.checkBox_oil.stateChanged.connect(self.updateProdData)
        self.checkBox_wtr.stateChanged.connect(self.updateProdData)
        self.checkBox_gas.stateChanged.connect(self.updateProdData)
        self.checkBox_stm.stateChanged.connect(self.updateProdData)
        self.checkBox_con.stateChanged.connect(self.updateProdData)
        self.checkBox_cyc.stateChanged.connect(self.updateProdData)
        self.checkBox_win.stateChanged.connect(self.updateProdData)
        self.pushButton_selectFile.clicked.connect(self.selectFile)
        self.pushButton_export.clicked.connect(self.exportSelections)
        self.pushButton_exportPlot.clicked.connect(self.exportPlots)
        self.lineEdit_maplatMin_prod.editingFinished.connect(self.updateProdData)
        self.lineEdit_maplatMax_prod.editingFinished.connect(self.updateProdData)
        self.lineEdit_maplonMin_prod.editingFinished.connect(self.updateProdData)
        self.lineEdit_maplonMax_prod.editingFinished.connect(self.updateProdData)
        self.lineEdit_filename.editingFinished.connect(self.updatePlotNames)
        
    def updatePlotNames(self):
        self.matplotlibwidget_mapprod.axes.set_title('Cumulative Production / Injection Map (bbls / Mcf) - '+self.lineEdit_filename.text())        
        self.matplotlibwidget_rate.axes.set_title('Production / Injection Rate Plot - '+self.lineEdit_filename.text())
        self.matplotlibwidget_cum.axes.set_title('Production / Injection Cumulative Plot - '+self.lineEdit_filename.text())
        self.matplotlibwidget_mapsel.axes.set_title('Selection Map - '+self.lineEdit_filename.text())
        self.matplotlibwidget_mapprod.axes.figure.canvas.draw()
        self.matplotlibwidget_rate.axes.figure.canvas.draw()
        self.matplotlibwidget_cum.axes.figure.canvas.draw()
        self.matplotlibwidget_mapsel.axes.figure.canvas.draw()
        print('Plot names changed')
        print('#############################################################################')
        
    def exportPlots(self):
        try:
            self.matplotlibwidget_mapprod.axes.figure.savefig('plots/doggrScraper_'+self.lineEdit_filename.text()+'_mapprod.png', facecolor='azure', bbox_inches='tight', dpi=300)
        except:
            pass
        try:
            self.matplotlibwidget_rate.axes.figure.savefig('plots/doggrScraper_'+self.lineEdit_filename.text()+'_plotrate.png', facecolor='azure', bbox_inches='tight', dpi=300)
        except:
            pass
        try:
            self.matplotlibwidget_cum.axes.figure.savefig('plots/doggrScraper_'+self.lineEdit_filename.text()+'_plotcum.png', facecolor='azure', bbox_inches='tight', dpi=300)
        except:
            pass
        print('Production / cumulative plots exported')
        print('#############################################################################')
        
    def exportSelections(self):
        try:
            self.matplotlibwidget_mapsel.axes.figure.savefig('plots/doggrScraper_'+self.lineEdit_filename.text()+'_mapsel.png', facecolor='azure', bbox_inches='tight', dpi=300)
        except:
            pass
        self.selections.to_csv('selections/doggrScraper_'+self.lineEdit_filename.text()+'_selections.csv', index=False)
        print('Selection map / csv exported')
        print('#############################################################################')

    def selectFile(self):
        file_selected = QtGui.QFileDialog.getOpenFileName()
        self.prod_data = pd.read_csv(file_selected)
        self.prod_data_lim = self.prod_data.copy(deep=True)
        self.dateMin = pd.to_datetime(self.prod_data_lim['Month']).min()
        self.dateMax = pd.to_datetime(self.prod_data_lim['Month']).max()
        self.dateEdit_dateminPlot.setDate(QtCore.QDate(self.dateMin.year, self.dateMin.month, self.dateMin.day))
        self.dateEdit_datemaxPlot.setDate(QtCore.QDate(self.dateMax.year, self.dateMax.month, self.dateMax.day))
        if len(file_selected) > 77:            
            print(file_selected[:20]+' ... '+file_selected[-52:])
        else:
            print(file_selected)        
        print('Production file loaded')
        self.updateProdSelections()

    def updateDoggrSelections(self):
        self.label_wellsSelected.setText(_translate("MainWindow", 'Updating selections from DOGGR...', None))
        print('Updating well selections from DOGGR...')
        print('Please be patient, updating can take up to 5 min...')
        Popen("sys\\fetch_MASTER_selections.vbs", shell=True)
        self.results = pd.ExcelFile('selections/doggrScraper_MASTER_selections.xlsx')\
        .parse('CA DOGGR Wells', header=None)
        self.results.columns = self.results.iloc[3]
        self.results = self.results.reindex(self.results.index.drop([0,1,2,3]))
        self.results = self.results.astype(str)
        self.results.to_csv('selections/doggrScraper_MASTER_selections.csv', encoding='utf-8', index=False)
        os.remove('selections/doggrScraper_MASTER_selections.xlsx')
        self.readSelections()
        self.updateComboboxes()
        print('Selections updated!')
        print('#############################################################################')

    def readSelections(self):
        file_selected = QtGui.QFileDialog.getOpenFileName()
        self.results = pd.read_csv(file_selected, index_col=False)
        self.results = self.results.astype(str)
        self.results['API #'] = self.results['API #'].map(lambda x: '0'+str(x) if len(str(x)) < 8 else str(x))
        self.results['SPUD Date'] = pd.to_datetime(self.results['SPUD Date'])
        self.results['Completion Date'] = pd.to_datetime(self.results['Completion Date'])
        self.results['Abandoned Date'] = pd.to_datetime(self.results['Abandoned Date'])
        self.results['Latitude'] = self.results['Latitude'].astype(float)
        self.results['Longitude'] = self.results['Longitude'].astype(float)
        print('Selections loaded')

    def updateProdSelections(self):
        self.groupingPlot_idx = self.comboBox_groupingPlot.currentText()
        if self.groupingPlot_idx != 'None':
            self.comboBox_selectionPlot.clear()
            self.comboBox_selectionPlot.addItem('None')
            if self.groupingPlot_idx == 'Spud Year':
                for idx, val in enumerate(sorted(self.prod_data['Spud'].map(lambda x: str(x[:4])).unique())):
                    self.comboBox_selectionPlot.addItem(str(val))
            else:
                for idx, val in enumerate(sorted(self.prod_data[self.groupingPlot_idx].unique())):
                    self.comboBox_selectionPlot.addItem(str(val))
        else:
            self.comboBox_selectionPlot.clear()
            self.comboBox_selectionPlot.addItem('None')
        print('Production selections loaded / updated')
        self.updateProdData()

    def updateProdData(self):
        self.selectionPlot_idx = self.comboBox_selectionPlot.currentText()
        if self.comboBox_selectionPlot.currentText() == 'None':
            self.prod_data_lim = self.prod_data
        if self.comboBox_selectionPlot.currentText() != 'None':
            if self.groupingPlot_idx == 'Spud Year':
                self.prod_data_lim = self.prod_data[self.prod_data['Spud'].map(lambda x: str(x[:4])) == str(self.selectionPlot_idx)]
            else:
                self.prod_data_lim = self.prod_data[self.prod_data[self.groupingPlot_idx].map(lambda x: str(x)) == str(self.selectionPlot_idx)]
        self.dateMin = pd.to_datetime(self.dateEdit_dateminPlot.date().toPyDate())
        self.dateMax = pd.to_datetime(self.dateEdit_datemaxPlot.date().toPyDate())        
        if self.lineEdit_maplatMin_prod.text() != '':
            self.prod_data_lim = self.prod_data_lim[self.prod_data_lim['Latitude'] >= float(self.lineEdit_maplatMin_prod.text())]
        if self.lineEdit_maplatMax_prod.text() != '':
            self.prod_data_lim = self.prod_data_lim[self.prod_data_lim['Latitude'] <= float(self.lineEdit_maplatMax_prod.text())]
        if self.lineEdit_maplonMin_prod.text() != '':
            self.prod_data_lim = self.prod_data_lim[self.prod_data_lim['Longitude'] >= float(self.lineEdit_maplonMin_prod.text())]
        if self.lineEdit_maplonMax_prod.text() != '':
            self.prod_data_lim = self.prod_data_lim[self.prod_data_lim['Longitude'] <= float(self.lineEdit_maplonMax_prod.text())]
        self.prod_data_lim['date'] = pd.to_datetime(self.prod_data_lim['Month'])
        self.prod_data_lim = self.prod_data_lim[(self.prod_data_lim['date'] >= self.dateMin) & (self.prod_data_lim['date'] <= self.dateMax)]
        self.dateEdit_dateminPlot.setDate(QtCore.QDate(self.dateMin.year, self.dateMin.month, self.dateMin.day))
        self.dateEdit_datemaxPlot.setDate(QtCore.QDate(self.dateMax.year, self.dateMax.month, self.dateMax.day))
        print('Production data updated')
        self.makeProdPlot()

    def makeMapSel(self):
        self.matplotlibwidget_mapsel.axes.cla()
        self.matplotlibwidget_mapsel.axes.hold(True)
        try:
            self.wells_ai = self.selections[self.selections['Pool WellTypes'] == 'AI']
            if len(self.wells_ai) > 0:
                self.coords_ai = self.getCoords(self.wells_ai)
                self.matplotlibwidget_mapsel.axes.scatter(self.coords_ai['Longitude'], self.coords_ai['Latitude'], marker='v', alpha=0.5, color='lightblue', label='AI')
        except:
            pass
        try:
            self.wells_dg = self.selections[self.selections['Pool WellTypes'] == 'DG']
            if len(self.wells_dg) > 0:
                self.coords_dg = self.getCoords(self.wells_dg)
                self.matplotlibwidget_mapsel.axes.scatter(self.coords_dg['Longitude'], self.coords_dg['Latitude'], marker='^', alpha=0.5, color='tomato', label='DG')
        except:
            pass
        try:
            self.wells_gd = self.selections[self.selections['Pool WellTypes'] == 'GD']
            if len(self.wells_gd) > 0:
                self.coords_gd = self.getCoords(self.wells_gd)
                self.matplotlibwidget_mapsel.axes.scatter(self.coords_gd['Longitude'], self.coords_gd['Latitude'], marker='v', alpha=0.5, color='tomato', label='GD')
        except:
            pass
        try:
            self.wells_gs = self.selections[self.selections['Pool WellTypes'] == 'GS']
            if len(self.wells_gs) > 0:
                self.coords_gs = self.getCoords(self.wells_gs)
                self.matplotlibwidget_mapsel.axes.scatter(self.coords_gs['Longitude'], self.coords_gs['Latitude'], marker='D', alpha=0.5, color='firebrick', label='GS')
        except:
            pass
        try:
            self.wells_lg = self.selections[self.selections['Pool WellTypes'] == 'LG']
            if len(self.wells_lg) > 0:
                self.coords_lg = self.getCoords(self.wells_lg)
                self.matplotlibwidget_mapsel.axes.scatter(self.coords_lg['Longitude'], self.coords_lg['Latitude'], marker='D', alpha=0.5, color='greenyellow', label='LG')
        except:
            pass
        try:
            self.wells_ob = self.selections[self.selections['Pool WellTypes'] == 'OB']
            if len(self.wells_ob) > 0:
                self.coords_ob = self.getCoords(self.wells_ob)
                self.matplotlibwidget_mapsel.axes.scatter(self.coords_ob['Longitude'], self.coords_ob['Latitude'], marker='+', alpha=0.5, color='darkorchid', label='OB')
        except:
            pass
        try:
            self.wells_og = self.selections[self.selections['Pool WellTypes'].isin(['OG','OG, SC'])]
            if len(self.wells_og) > 0:
                self.coords_og = self.getCoords(self.wells_og)
                self.matplotlibwidget_mapsel.axes.scatter(self.coords_og['Longitude'], self.coords_og['Latitude'], marker='^', alpha=0.5, color='forestgreen', label='OG')
        except:
            pass
        try:
            self.wells_pm = self.selections[self.selections['Pool WellTypes'] == 'PM']
            if len(self.wells_pm) > 0:
                self.coords_pm = self.getCoords(self.wells_pm)
                self.matplotlibwidget_mapsel.axes.scatter(self.coords_pm['Longitude'], self.coords_pm['Latitude'], marker='+', alpha=0.5, color='purple', label='PM')
        except:
            pass
        try:
            self.wells_sf = self.selections[self.selections['Pool WellTypes'] == 'SF']
            if len(self.wells_sf) > 0:
                self.coords_sf = self.getCoords(self.wells_sf)
                self.matplotlibwidget_mapsel.axes.scatter(self.coords_sf['Longitude'], self.coords_sf['Latitude'], marker='v', alpha=0.5, color='crimson', label='SF')
        except:
            pass
        try:
            self.wells_wd = self.selections[self.selections['Pool WellTypes'] == 'WD']
            if len(self.wells_wd) > 0:
                self.coords_wd = self.getCoords(self.wells_wd)
                self.matplotlibwidget_mapsel.axes.scatter(self.coords_wd['Longitude'], self.coords_wd['Latitude'], marker='v', alpha=0.5, color='midnightblue', label='WD')
        except:
            pass
        try:
            self.wells_wf = self.selections[self.selections['Pool WellTypes'] == 'WF']
            if len(self.wells_wf) > 0:
                self.coords_wf = self.getCoords(self.wells_wf)
                self.matplotlibwidget_mapsel.axes.scatter(self.coords_wf['Longitude'], self.coords_wf['Latitude'], marker='v', alpha=0.5, color='mediumturquoise', label='WF')
        except:
            pass
        try:
            self.wells_ws = self.selections[self.selections['Pool WellTypes'] == 'WS']
            if len(self.wells_ws) > 0:
                self.coords_ws = self.getCoords(self.wells_ws)
                self.matplotlibwidget_mapsel.axes.scatter(self.coords_ws['Longitude'], self.coords_ws['Latitude'], marker='v', alpha=0.5, color='dodgerblue', label='WS')
        except:
            pass
        try:
            self.wells_sc = self.selections[self.selections['Pool WellTypes'] == 'SC']
            if len(self.wells_sc) > 0:
                self.coords_sc = self.getCoords(self.wells_sc)
                self.matplotlibwidget_mapsel.axes.scatter(self.coords_sc['Longitude'], self.coords_sc['Latitude'], marker='D', alpha=0.5, color='gold', label='SC')
        except:
            pass
        try:
            self.wells_mix = self.selections[~self.selections['Pool WellTypes'].isin(['AI','DG','GD','GS','LG','OB','OG','PM','SF','WD','WF','WS','OG, SC','SC'])]
            if len(self.wells_mix) > 0:
                self.coords_mix = self.getCoords(self.wells_mix)
                self.matplotlibwidget_mapsel.axes.scatter(self.coords_mix['Longitude'], self.coords_mix['Latitude'], marker='x', alpha=0.5, color='dimgray', label='Var')
        except:
            pass
        self.matplotlibwidget_mapsel.axes.set_ylabel('Latitude')
        self.matplotlibwidget_mapsel.axes.set_xlabel('Longitude')
        self.matplotlibwidget_mapsel.axes.set_title('Selection Map - '+self.lineEdit_filename.text())
        self.matplotlibwidget_mapsel.axes.grid(True)
        self.matplotlibwidget_mapsel.axes.legend(loc='upper right', shadow=False, scatterpoints=1)
        self.matplotlibwidget_mapsel.axes.get_xaxis().get_major_formatter().set_useOffset(False)
        self.matplotlibwidget_mapsel.axes.get_yaxis().get_major_formatter().set_useOffset(False)
        self.matplotlibwidget_mapsel.axes.set_aspect('equal', 'datalim')
        self.matplotlibwidget_mapsel.axes.figure.canvas.draw()
        print('Selection map updated')
        print('#############################################################################')

    def makeProdPlot(self):
        self.prod_pivot = pd.DataFrame(index=self.prod_data_lim['Month'].sort(['Month'], inplace=False).unique())
        self.matplotlibwidget_rate.axes.cla()
        self.matplotlibwidget_rate.axes.hold(True)
        if self.checkBox_oil.isChecked():
            try:
                self.prod_pivot['oil'] = pd.pivot_table(self.prod_data_lim, values=['Oil Produced (bbl)'], index=['Month'], aggfunc=np.sum)
                self.matplotlibwidget_rate.axes.plot_date(pd.to_datetime(self.prod_pivot.index),self.prod_pivot['oil'] / 30.45, '-', color='forestgreen', label='Oil')
            except:
                pass
        if self.checkBox_wtr.isChecked():
            try:
                self.prod_pivot['wtr'] = pd.pivot_table(self.prod_data_lim, values=['Water Produced (bbl)'], index=['Month'], aggfunc=np.sum)
                self.matplotlibwidget_rate.axes.plot_date(pd.to_datetime(self.prod_pivot.index),self.prod_pivot['wtr'] / 30.45, '-', color='dodgerblue', label='Wtr')
            except:
                pass
        if self.checkBox_gas.isChecked():
            try:
                self.prod_pivot['gas'] = pd.pivot_table(self.prod_data_lim, values=['Gas Produced (Mcf)'], index=['Month'], aggfunc=np.sum)
                self.matplotlibwidget_rate.axes.plot_date(pd.to_datetime(self.prod_pivot.index),self.prod_pivot['gas'] / 30.45, '-', color='tomato', label='Gas')
            except:
                pass
        if self.checkBox_stm.isChecked():
            try:
                self.prod_pivot['stm'] = pd.pivot_table(self.prod_data_lim, values=['Total Steam Injected (bbl)'], index=['Month'], aggfunc=np.sum)
                self.matplotlibwidget_rate.axes.plot_date(pd.to_datetime(self.prod_pivot.index),self.prod_pivot['stm'] / 30.45, '-', color='deeppink', label='Stm')
            except:
                pass
        if self.checkBox_con.isChecked():
            try:
                self.prod_pivot['con'] = pd.pivot_table(self.prod_data_lim, values=['Continous Injected (bbl)'], index=['Month'], aggfunc=np.sum)
                self.matplotlibwidget_rate.axes.plot_date(pd.to_datetime(self.prod_pivot.index),self.prod_pivot['con'] / 30.45, '-', color='crimson', label='Cont')
            except:
                pass
        if self.checkBox_cyc.isChecked():
            try:
                self.prod_pivot['cyc'] = pd.pivot_table(self.prod_data_lim, values=['Cyclic Injected (bbl)'], index=['Month'], aggfunc=np.sum)
                self.matplotlibwidget_rate.axes.plot_date(pd.to_datetime(self.prod_pivot.index),self.prod_pivot['cyc'] / 30.45, '-', color='gold', label='Cyc')
            except:
                pass
        if self.checkBox_win.isChecked():
            try:
                self.prod_pivot['win'] = pd.pivot_table(self.prod_data_lim, values=['Water Injected (bbl)'], index=['Month'], aggfunc=np.sum)
                self.matplotlibwidget_rate.axes.plot_date(pd.to_datetime(self.prod_pivot.index),self.prod_pivot['win'] / 30.45, '-', color='mediumturquoise', label='WInj')
            except:
                pass
        try:
            self.prod_pivot['cnt'] = pd.pivpivottable(self.prod_data_lim, values=['API10'], index=['Month'], aggfunc=pd.Series.nunique)
            self.matplotlibwidget_rate.axes.plot_date(pd.to_datetime(self.prod_pivot.index),self.prod_pivot['cnt'], '-', color='black', label='#')
        except:
            pass
        self.prod_pivot = self.prod_pivot.fillna(0)
        self.matplotlibwidget_rate.axes.set_ylabel('Prod / Inj (Mcf/d or bbls/d), Wellcount')
        self.matplotlibwidget_rate.axes.set_xlabel('Month')
        self.matplotlibwidget_rate.axes.set_title('Production / Injection Rate Plot - '+self.lineEdit_filename.text())
        if self.checkBox_ratePlot.isChecked():
            self.matplotlibwidget_rate.axes.set_yscale('log')
        self.matplotlibwidget_rate.axes.grid(b=True, which='minor', color='slategrey', linestyle='--')
        self.matplotlibwidget_rate.axes.grid(b=True, which='major', color='slategrey', linestyle='--')
        self.matplotlibwidget_rate.axes.legend(loc='lower left', shadow=False)
        self.matplotlibwidget_rate.axes.figure.canvas.draw()
        self.matplotlibwidget_cum.axes.cla()
        self.matplotlibwidget_cum.axes.hold(True)
        if self.checkBox_oil.isChecked():
            try:
                self.prod_pivot['oil_cum'] = self.prod_pivot['oil'].cumsum()
                self.matplotlibwidget_cum.axes.plot_date(pd.to_datetime(self.prod_pivot.index),self.prod_pivot['oil_cum'], '-', color='forestgreen', label='Oil')
            except:
                pass
        if self.checkBox_wtr.isChecked():
            try:
                self.prod_pivot['wtr_cum'] = self.prod_pivot['wtr'].cumsum()
                self.matplotlibwidget_cum.axes.plot_date(pd.to_datetime(self.prod_pivot.index),self.prod_pivot['wtr_cum'], '-', color='dodgerblue', label='Wtr')
            except:
                pass
        if self.checkBox_gas.isChecked():
            try:
                self.prod_pivot['gas_cum'] = self.prod_pivot['gas'].cumsum()
                self.matplotlibwidget_cum.axes.plot_date(pd.to_datetime(self.prod_pivot.index),self.prod_pivot['gas_cum'], '-', color='tomato', label='Gas')
            except:
                pass
        if self.checkBox_stm.isChecked():
            try:
               self. prod_pivot['stm_cum'] = self.prod_pivot['stm'].cumsum()
               self.matplotlibwidget_cum.axes.plot_date(pd.to_datetime(self.prod_pivot.index),self.prod_pivot['stm_cum'], '-', color='deeppink', label='Stm')
            except:
                pass
        if self.checkBox_con.isChecked():
            try:
                self.prod_pivot['con_cum'] = self.prod_pivot['con'].cumsum()
                self.matplotlibwidget_cum.axes.plot_date(pd.to_datetime(self.prod_pivot.index),self.prod_pivot['con_cum'], '-', color='crimson', label='Cont')
            except:
                pass
        if self.checkBox_cyc.isChecked():
            try:
                self.prod_pivot['cyc_cum'] = self.prod_pivot['cyc'].cumsum()
                self.matplotlibwidget_cum.axes.plot_date(pd.to_datetime(self.prod_pivot.index),self.prod_pivot['cyc_cum'], '-', color='gold', label='Cyc')
            except:
                pass
        if self.checkBox_win.isChecked():
            try:
                self.prod_pivot['win_cum'] = self.prod_pivot['win'].cumsum()
                self.matplotlibwidget_cum.axes.plot_date(pd.to_datetime(self.prod_pivot.index),self.prod_pivot['win_cum'], '-', color='mediumturquoise', label='WInj')
            except:
                pass
        self.matplotlibwidget_cum.axes.set_ylabel('Cumulative Prod / Inj (Mcf or bbls)')
        self.matplotlibwidget_cum.axes.set_xlabel('Month')
        self.matplotlibwidget_cum.axes.set_title('Production / Injection Cumulative Plot - '+self.lineEdit_filename.text())
        if self.checkBox_cumPlot.isChecked():
            self.matplotlibwidget_cum.axes.set_yscale('log')
        self.matplotlibwidget_cum.axes.grid(b=True, which='minor', color='slategrey', linestyle='--')
        self.matplotlibwidget_cum.axes.grid(b=True, which='major', color='slategrey', linestyle='--')
        self.matplotlibwidget_cum.axes.legend(loc='lower left', shadow=False)
        self.matplotlibwidget_cum.axes.figure.canvas.draw()
        print('Production plots updated')
        self.makeMapProd()

    def makeMapProd(self):
        self.prod_data_lim_prod = self.prod_data_lim.copy(deep=True)
        self.prod_data_lim_prod = self.prod_data_lim_prod[self.prod_data_lim_prod['Latitude'] != 0]
        self.prod_data_lim_prod = self.prod_data_lim_prod[self.prod_data_lim_prod['Longitude'] != 0]
        if self.lineEdit_maplatMin_prod.text() != '':
            self.prod_data_lim_prod = self.prod_data_lim_prod[self.prod_data_lim_prod['Latitude'] >= float(self.lineEdit_maplatMin_prod.text())]
        if self.lineEdit_maplatMax_prod.text() != '':
            self.prod_data_lim_prod = self.prod_data_lim_prod[self.prod_data_lim_prod['Latitude'] <= float(self.lineEdit_maplatMax_prod.text())]
        if self.lineEdit_maplonMin_prod.text() != '':
            self.prod_data_lim_prod = self.prod_data_lim_prod[self.prod_data_lim_prod['Longitude'] >= float(self.lineEdit_maplonMin_prod.text())]
        if self.lineEdit_maplonMax_prod.text() != '':
            self.prod_data_lim_prod = self.prod_data_lim_prod[self.prod_data_lim_prod['Longitude'] <= float(self.lineEdit_maplonMax_prod.text())]
        latMin = self.prod_data_lim_prod['Latitude'].min()
        latMax = self.prod_data_lim_prod['Latitude'].max()
        lonMin = self.prod_data_lim_prod['Longitude'].min()
        lonMax = self.prod_data_lim_prod['Longitude'].max()
        self.selections_prod = self.results.copy(deep=True)
        self.selections_prod = self.selections_prod[(self.selections_prod['Latitude'] >= latMin) & (self.selections_prod['Latitude'] <= latMax)]
        self.selections_prod = self.selections_prod[(self.selections_prod['Longitude'] >= lonMin) & (self.selections_prod['Longitude'] <= lonMax)]
        oil_pivot = pd.pivot_table(self.prod_data_lim_prod, values=['Oil Produced (bbl)'], index=['Well','Latitude','Longitude'], aggfunc=np.sum).reset_index().fillna(0)
        wtr_pivot = pd.pivot_table(self.prod_data_lim_prod, values=['Water Produced (bbl)'], index=['Well','Latitude','Longitude'], aggfunc=np.sum).reset_index().fillna(0)
        gas_pivot = pd.pivot_table(self.prod_data_lim_prod, values=['Gas Produced (Mcf)'], index=['Well','Latitude','Longitude'], aggfunc=np.sum).reset_index().fillna(0)
        stm_pivot = pd.pivot_table(self.prod_data_lim_prod, values=['Total Steam Injected (bbl)'], index=['Well','Latitude','Longitude'], aggfunc=np.sum).reset_index().fillna(0)
        con_pivot = pd.pivot_table(self.prod_data_lim_prod, values=['Continous Injected (bbl)'], index=['Well','Latitude','Longitude'], aggfunc=np.sum).reset_index().fillna(0)
        cyc_pivot = pd.pivot_table(self.prod_data_lim_prod, values=['Cyclic Injected (bbl)'], index=['Well','Latitude','Longitude'], aggfunc=np.sum).reset_index().fillna(0)
        win_pivot = pd.pivot_table(self.prod_data_lim_prod, values=['Water Injected (bbl)'], index=['Well','Latitude','Longitude'], aggfunc=np.sum).reset_index().fillna(0)
        self.matplotlibwidget_mapprod.axes.cla()
        self.matplotlibwidget_mapprod.axes.hold(True)
        if self.checkBox_wtr.isChecked():
            self.matplotlibwidget_mapprod.axes.scatter(wtr_pivot['Longitude'], wtr_pivot['Latitude'], s=np.pi / 10000 * wtr_pivot['Water Produced (bbl)'], c='dodgerblue', alpha=0.5, label='Wtr/10k')
        if self.checkBox_stm.isChecked():
            self.matplotlibwidget_mapprod.axes.scatter(stm_pivot['Longitude'], stm_pivot['Latitude'], s=np.pi / 10000 * stm_pivot['Total Steam Injected (bbl)'], c='deeppink', alpha=0.5, label='Stm/10k')
        if self.checkBox_con.isChecked():
            self.matplotlibwidget_mapprod.axes.scatter(con_pivot['Longitude'], con_pivot['Latitude'], s=np.pi / 10000 * con_pivot['Continous Injected (bbl)'], c='crimson', alpha=0.5, label='Cont/10k')
        if self.checkBox_cyc.isChecked():
            self.matplotlibwidget_mapprod.axes.scatter(cyc_pivot['Longitude'], cyc_pivot['Latitude'], s=np.pi / 100 * cyc_pivot['Cyclic Injected (bbl)'], c='gold', alpha=0.5, label='Cyc/100')
        if self.checkBox_win.isChecked():
            self.matplotlibwidget_mapprod.axes.scatter(win_pivot['Longitude'], win_pivot['Latitude'], s=np.pi / 10000 * win_pivot['Water Injected (bbl)'], c='mediumturquoise', alpha=0.5, label='WInj/10k')
        if self.checkBox_gas.isChecked():
            self.matplotlibwidget_mapprod.axes.scatter(gas_pivot['Longitude'], gas_pivot['Latitude'], s=np.pi / 1000 * gas_pivot['Gas Produced (Mcf)'], c='tomato', alpha=0.5, label='Gas/1k')
        if self.checkBox_oil.isChecked():
            self.matplotlibwidget_mapprod.axes.scatter(oil_pivot['Longitude'], oil_pivot['Latitude'], s=np.pi / 1000 * oil_pivot['Oil Produced (bbl)'], c='forestgreen', alpha=0.5, label='Oil/1k')
        try:
            self.wells_ai = self.selections_prod[self.selections_prod['Pool WellTypes'] == 'AI']
            if len(self.wells_ai) > 0:
                self.coords_ai = self.getCoords(self.wells_ai)
                self.matplotlibwidget_mapprod.axes.scatter(self.coords_ai['Longitude'], self.coords_ai['Latitude'], marker='v', alpha=0.5, color='lightblue', label='AI')
        except:
            pass
        try:
            self.wells_dg = self.selections_prod[self.selections_prod['Pool WellTypes'] == 'DG']
            if len(self.wells_dg) > 0:
                self.coords_dg = self.getCoords(self.wells_dg)
                self.matplotlibwidget_mapprod.axes.scatter(self.coords_dg['Longitude'], self.coords_dg['Latitude'], marker='^', alpha=0.5, color='tomato', label='DG')
        except:
            pass
        try:
            self.wells_gd = self.selections_prod[self.selections_prod['Pool WellTypes'] == 'GD']
            if len(self.wells_gd) > 0:
                self.coords_gd = self.getCoords(self.wells_gd)
                self.matplotlibwidget_mapprod.axes.scatter(self.coords_gd['Longitude'], self.coords_gd['Latitude'], marker='v', alpha=0.5, color='tomato', label='GD')
        except:
            pass
        try:
            self.wells_gs = self.selections_prod[self.selections_prod['Pool WellTypes'] == 'GS']
            if len(self.wells_gs) > 0:
                self.coords_gs = self.getCoords(self.wells_gs)
                self.matplotlibwidget_mapprod.axes.scatter(self.coords_gs['Longitude'], self.coords_gs['Latitude'], marker='D', alpha=0.5, color='firebrick', label='GS')
        except:
            pass
        try:
            self.wells_lg = self.selections_prod[self.selections_prod['Pool WellTypes'] == 'LG']
            if len(self.wells_lg) > 0:
                self.coords_lg = self.getCoords(self.wells_lg)
                self.matplotlibwidget_mapprod.axes.scatter(self.coords_lg['Longitude'], self.coords_lg['Latitude'], marker='D', alpha=0.5, color='greenyellow', label='LG')
        except:
            pass
        try:
            self.wells_ob = self.selections_prod[self.selections_prod['Pool WellTypes'] == 'OB']
            if len(self.wells_ob) > 0:
                self.coords_ob = self.getCoords(self.wells_ob)
                self.matplotlibwidget_mapprod.axes.scatter(self.coords_ob['Longitude'], self.coords_ob['Latitude'], marker='+', alpha=0.5, color='darkorchid', label='OB')
        except:
            pass
        try:
            self.wells_og = self.selections_prod[self.selections_prod['Pool WellTypes'].isin(['OG','OG, SC'])]
            if len(self.wells_og) > 0:
                self.coords_og = self.getCoords(self.wells_og)
                self.matplotlibwidget_mapprod.axes.scatter(self.coords_og['Longitude'], self.coords_og['Latitude'], marker='^', alpha=0.5, color='forestgreen', label='OG')
        except:
            pass
        try:
            self.wells_pm = self.selections_prod[self.selections_prod['Pool WellTypes'] == 'PM']
            if len(self.wells_pm) > 0:
                self.coords_pm = self.getCoords(self.wells_pm)
                self.matplotlibwidget_mapprod.axes.scatter(self.coords_pm['Longitude'], self.coords_pm['Latitude'], marker='+', alpha=0.5, color='purple', label='PM')
        except:
            pass
        try:
            self.wells_sf = self.selections_prod[self.selections_prod['Pool WellTypes'] == 'SF']
            if len(self.wells_sf) > 0:
                self.coords_sf = self.getCoords(self.wells_sf)
                self.matplotlibwidget_mapprod.axes.scatter(self.coords_sf['Longitude'], self.coords_sf['Latitude'], marker='v', alpha=0.5, color='crimson', label='SF')
        except:
            pass
        try:
            self.wells_wd = self.selections_prod[self.selections_prod['Pool WellTypes'] == 'WD']
            if len(self.wells_wd) > 0:
                self.coords_wd = self.getCoords(self.wells_wd)
                self.matplotlibwidget_mapprod.axes.scatter(self.coords_wd['Longitude'], self.coords_wd['Latitude'], marker='v', alpha=0.5, color='midnightblue', label='WD')
        except:
            pass
        try:
            self.wells_wf = self.selections_prod[self.selections_prod['Pool WellTypes'] == 'WF']
            if len(self.wells_wf) > 0:
                self.coords_wf = self.getCoords(self.wells_wf)
                self.matplotlibwidget_mapprod.axes.scatter(self.coords_wf['Longitude'], self.coords_wf['Latitude'], marker='v', alpha=0.5, color='mediumturquoise', label='WF')
        except:
            pass
        try:
            self.wells_ws = self.selections_prod[self.selections_prod['Pool WellTypes'] == 'WS']
            if len(self.wells_ws) > 0:
                self.coords_ws = self.getCoords(self.wells_ws)
                self.matplotlibwidget_mapprod.axes.scatter(self.coords_ws['Longitude'], self.coords_ws['Latitude'], marker='v', alpha=0.5, color='dodgerblue', label='WS')
        except:
            pass
        try:
            self.wells_sc = self.selections_prod[self.selections_prod['Pool WellTypes'] == 'SC']
            if len(self.wells_sc) > 0:
                self.coords_sc = self.getCoords(self.wells_sc)
                self.matplotlibwidget_mapprod.axes.scatter(self.coords_sc['Longitude'], self.coords_sc['Latitude'], marker='D', alpha=0.5, color='gold', label='SC')
        except:
            pass
        try:
            self.wells_mix = self.selections_prod[~self.selections_prod['Pool WellTypes'].isin(['AI','DG','GD','GS','LG','OB','OG','PM','SF','WD','WF','WS','OG, SC','SC'])]
            if len(self.wells_mix) > 0:
                self.coords_mix = self.getCoords(self.wells_mix)
                self.matplotlibwidget_mapprod.axes.scatter(self.coords_mix['Longitude'], self.coords_mix['Latitude'], marker='x', alpha=0.5, color='dimgray', label='Var')
        except:
            pass
        self.matplotlibwidget_mapprod.axes.set_ylabel('Latitude')
        self.matplotlibwidget_mapprod.axes.set_xlabel('Longitude')
        self.matplotlibwidget_mapprod.axes.set_title('Cumulative Production / Injection Map (bbls / Mcf) - '+self.lineEdit_filename.text())
        self.matplotlibwidget_mapprod.axes.grid(True)
        lgnd = self.matplotlibwidget_mapprod.axes.legend(loc=0, shadow=False, scatterpoints=1)
        for i in range(len(lgnd.legendHandles)):
            if lgnd.legendHandles[i]._label in ['Wtr/10k','Stm/10k','Cont/10k','Cyc/100','WInj/10k','Gas/1k','Oil/1k']:
                lgnd.legendHandles[i]._sizes = [30]
        self.matplotlibwidget_mapprod.axes.get_xaxis().get_major_formatter().set_useOffset(False)
        self.matplotlibwidget_mapprod.axes.get_yaxis().get_major_formatter().set_useOffset(False)
        self.matplotlibwidget_mapprod.axes.set_aspect('equal', 'datalim')
        self.matplotlibwidget_mapprod.axes.figure.canvas.draw()
        print('Cumulative plot updated')
        print('#############################################################################')
        
    def updateSelection(self):
        self.districtNumber_idx = self.comboBox_districtNumber.currentText()
        self.field_idx = self.comboBox_field.currentText()
        self.fieldCode_idx = self.comboBox_fieldCode.currentText()
        self.operatorName_idx = self.comboBox_operatorName.currentText()
        self.operatorCode_idx = self.comboBox_operatorCode.currentText()
        self.sec_idx = self.comboBox_sec.currentText()
        self.twn_idx = self.comboBox_twn.currentText()
        self.rge_idx = self.comboBox_rge.currentText()
        self.apiNum_idx = self.comboBox_apiNum.currentText()
        self.lease_idx = self.comboBox_lease.currentText()
        self.wellName_idx = self.comboBox_wellName.currentText()
        self.status_idx = self.comboBox_status.currentText()
        self.type_idx = self.comboBox_type.currentText()
        self.bm_idx = self.comboBox_bm.currentText()
        self.areaName_idx = self.comboBox_areaName.currentText()
        self.areaCode_idx = self.comboBox_areaCode.currentText()
        self.latMin_idx = self.lineEdit_latMin.text()
        self.latMax_idx = self.lineEdit_latMax.text()
        self.lonMin_idx = self.lineEdit_lonMin.text()
        self.lonMax_idx = self.lineEdit_lonMax.text()
        self.gis_idx = self.comboBox_gis.currentText()
        self.datum_idx = self.comboBox_datum.currentText()
        self.blm_idx = self.comboBox_blm.currentText()
        self.dry_idx = self.comboBox_dry.currentText()
        self.direc_idx = self.comboBox_direc.currentText()
        self.frac_idx = self.comboBox_frac.currentText()
        print('Updating selections')
        self.updateComboboxes()

    def updateComboboxes(self):
        self.selections = self.results.copy(deep=True)
        if self.districtNumber_idx != 'All':
            self.selections = self.selections[self.selections['District #'] == self.districtNumber_idx]
        if self.field_idx != 'All':
            if self.field_idx == 'Cymric':
                self.selections = self.selections[self.selections['Field Name'].isin(['Cymric','McKittrick'])]
            elif self.field_idx == 'McKittrick':
                self.selections = self.selections[self.selections['Field Name'].isin(['Cymric','McKittrick'])]
            else:
                self.selections = self.selections[self.selections['Field Name'] == self.field_idx]
        if self.fieldCode_idx != 'All':
            self.selections = self.selections[self.selections['Field Code'] == self.fieldCode_idx]
        if self.operatorName_idx != 'All':
            self.selections = self.selections[self.selections['Operator Name'] == self.operatorName_idx]
        if self.operatorCode_idx != 'All':
            self.selections = self.selections[self.selections['Operator Code'] == self.operatorCode_idx]
        if self.sec_idx != 'All':
            self.selections = self.selections[self.selections['Section'] == self.sec_idx]
        if self.twn_idx != 'All':
            self.selections = self.selections[self.selections['Township'] == self.twn_idx]
        if self.rge_idx != 'All':
            self.selections = self.selections[self.selections['Range'] == self.rge_idx]
        if self.apiNum_idx != 'All':
            self.selections = self.selections[self.selections['API #'] == self.apiNum_idx]
        if self.lease_idx != 'All':
            self.selections = self.selections[self.selections['Lease Name'] == self.lease_idx]
        if self.wellName_idx != 'All':
            self.selections = self.selections[self.selections['Well #'] == self.wellName_idx]
        if self.status_idx != 'All':
            self.selections = self.selections[self.selections['Well Status'] == self.status_idx]
        if self.type_idx != 'All':
            self.selections = self.selections[self.selections['Pool WellTypes'] == self.type_idx]
        if self.bm_idx != 'All':
            self.selections = self.selections[self.selections['Base Meridian'] == self.bm_idx]
        if self.areaName_idx != 'All':
            self.selections = self.selections[self.selections['Area Name'] == self.areaName_idx]
        if self.areaCode_idx != 'All':
            self.selections = self.selections[self.selections['Area Code'] == self.areaCode_idx]
        if self.latMin_idx != '':
            self.selections = self.selections[self.selections['Latitude'] >= float(self.latMin_idx)]
        if self.latMax_idx != '':
            self.selections = self.selections[self.selections['Latitude'] <= float(self.latMax_idx)]
        if self.lonMin_idx != '':
            self.selections = self.selections[self.selections['Longitude'] >= float(self.lonMin_idx)]
        if self.lonMax_idx != '':
            self.selections = self.selections[self.selections['Longitude'] <= float(self.lonMax_idx)]
        if self.gis_idx != 'All':
            self.selections = self.selections[self.selections['GISSourceCode'] == self.gis_idx]
        if self.datum_idx != 'All':
            self.selections = self.selections[self.selections['DatumCode'] == self.datum_idx]
        if self.blm_idx != 'All':
            self.selections = self.selections[self.selections['BLMWell'] == self.blm_idx]
        if self.dry_idx != 'All':
            self.selections = self.selections[self.selections['DryHole'] == self.dry_idx]
        if self.direc_idx != 'All':
            self.selections = self.selections[self.selections['Directional'] == self.direc_idx]
        if self.frac_idx != 'All':
            self.selections = self.selections[self.selections['Hydraulically Fractured'] == self.frac_idx]
        self.label_wellsSelected.setText(_translate("MainWindow", str(len(self.selections)), None))
        self.apilist = self.selections['API #'].unique()
        print('Selection boxes read')
        self.makeMapSel()
        self.buildComboboxes()

    def buildComboboxes(self):
        self.comboBox_districtNumber.clear()
        self.comboBox_districtNumber.addItem(self.districtNumber_idx)
        if self.districtNumber_idx != 'All':
            self.comboBox_districtNumber.addItem('All')
        else:
            for idx, val in enumerate(sorted(self.selections.iloc[:,0].unique())):
                self.comboBox_districtNumber.addItem(val)
        self.comboBox_field.clear()
        self.comboBox_field.addItem(self.field_idx)
        if self.field_idx != 'All':
            self.comboBox_field.addItem('All')
        else:
            for idx, val in enumerate(sorted(self.selections.iloc[:,4].unique())):
                self.comboBox_field.addItem(val)
        self.comboBox_fieldCode.clear()
        self.comboBox_fieldCode.addItem(self.fieldCode_idx)
        if self.fieldCode_idx != 'All':
            self.comboBox_fieldCode.addItem('All')
        else:
            for idx, val in enumerate(sorted(self.selections.iloc[:,5].unique())):
                self.comboBox_fieldCode.addItem(val)
        self.comboBox_operatorName.clear()
        self.comboBox_operatorName.addItem(self.operatorName_idx)
        if self.operatorName_idx != 'All':
            self.comboBox_operatorName.addItem('All')
        else:
            for idx, val in enumerate(sorted(self.selections.iloc[:,2].unique())):
                self.comboBox_operatorName.addItem(val)
        self.comboBox_operatorCode.clear()
        self.comboBox_operatorCode.addItem(self.operatorCode_idx)
        if self.operatorCode_idx != 'All':
            self.comboBox_operatorCode.addItem('All')
        else:
            for idx, val in enumerate(sorted(self.selections.iloc[:,3].unique())):
                self.comboBox_operatorCode.addItem(val)
        self.comboBox_sec.clear()
        self.comboBox_sec.addItem(self.sec_idx)
        if self.sec_idx != 'All':
            self.comboBox_sec.addItem('All')
        else:
            for idx, val in enumerate(sorted(self.selections.iloc[:,11].unique())):
                self.comboBox_sec.addItem(val)
        self.comboBox_twn.clear()
        self.comboBox_twn.addItem(self.twn_idx)
        if self.twn_idx != 'All':
            self.comboBox_twn.addItem('All')
        else:
            for idx, val in enumerate(sorted(self.selections.iloc[:,12].unique())):
                self.comboBox_twn.addItem(val)
        self.comboBox_rge.clear()
        self.comboBox_rge.addItem(self.rge_idx)
        if self.rge_idx != 'All':
            self.comboBox_rge.addItem('All')
        else:
            for idx, val in enumerate(sorted(self.selections.iloc[:,13].unique())):
                self.comboBox_rge.addItem(val)
        self.comboBox_apiNum.clear()
        self.comboBox_apiNum.addItem(self.apiNum_idx)
        if self.apiNum_idx != 'All':
           self.comboBox_apiNum.addItem('All')
        else:
            for idx, val in enumerate(sorted(self.selections.iloc[:,6].unique()[:2000])):
                self.comboBox_apiNum.addItem(val)
        self.comboBox_lease.clear()
        self.comboBox_lease.addItem(self.lease_idx)
        if self.lease_idx != 'All':
            self.comboBox_lease.addItem('All')
        else:
            for idx, val in enumerate(sorted(self.selections.iloc[:,7].unique())):
                self.comboBox_lease.addItem(val)
        self.comboBox_wellName.clear()
        self.comboBox_wellName.addItem(self.wellName_idx)
        if self.fieldCode_idx != 'All':
           self.comboBox_wellName.addItem('All')
        else:
           for idx, val in enumerate(sorted(self.selections.iloc[:,8].unique()[:2000])):
               self.comboBox_wellName.addItem(val)
        self.comboBox_status.clear()
        self.comboBox_status.addItem(self.status_idx)
        if self.status_idx != 'All':
            self.comboBox_status.addItem('All')
        else:
            for idx, val in enumerate(sorted(self.selections.iloc[:,9].unique())):
                self.comboBox_status.addItem(val)
        self.comboBox_type.clear()
        self.comboBox_type.addItem(self.type_idx)
        if self.type_idx != 'All':
            self.comboBox_type.addItem('All')
        else:
            for idx, val in enumerate(sorted(self.selections.iloc[:,10].unique())):
                self.comboBox_type.addItem(val)
        self.comboBox_bm.clear()
        self.comboBox_bm.addItem(self.bm_idx)
        if self.bm_idx != 'All':
            self.comboBox_bm.addItem('All')
        else:
            for idx, val in enumerate(sorted(self.selections.iloc[:,14].unique())):
                self.comboBox_bm.addItem(val)
        self.comboBox_areaName.clear()
        self.comboBox_areaName.addItem(self.areaName_idx)
        if self.areaName_idx != 'All':
            self.comboBox_areaName.addItem('All')
        else:
            for idx, val in enumerate(sorted(self.selections.iloc[:,16].unique())):
                self.comboBox_areaName.addItem(val)
        self.comboBox_areaCode.clear()
        self.comboBox_areaCode.addItem(self.areaCode_idx)
        if self.areaCode_idx != 'All':
            self.comboBox_areaCode.addItem('All')
        else:
            for idx, val in enumerate(sorted(self.selections.iloc[:,15].unique())):
                self.comboBox_areaCode.addItem(val)
        self.comboBox_gis.clear()
        self.comboBox_gis.addItem(self.gis_idx)
        if self.gis_idx != 'All':
            self.comboBox_gis.addItem('All')
        else:
            for idx, val in enumerate(sorted(self.selections.iloc[:,19].unique())):
                self.comboBox_gis.addItem(val)
        self.comboBox_datum.clear()
        self.comboBox_datum.addItem(self.datum_idx)
        if self.datum_idx != 'All':
            self.comboBox_datum.addItem('All')
        else:
            for idx, val in enumerate(sorted(self.selections.iloc[:,20].unique())):
                self.comboBox_gis.addItem(val)
        self.comboBox_blm.clear()
        self.comboBox_blm.addItem(self.blm_idx)
        if self.blm_idx != 'All':
            self.comboBox_blm.addItem('All')
        else:
            for idx, val in enumerate(sorted(self.selections.iloc[:,21].unique())):
                self.comboBox_blm.addItem(val)
        self.comboBox_dry.clear()
        self.comboBox_dry.addItem(self.dry_idx)
        if self.dry_idx != 'All':
            self.comboBox_dry.addItem('All')
        else:
            for idx, val in enumerate(sorted(self.selections.iloc[:,22].unique())):
                self.comboBox_dry.addItem(val)
        self.comboBox_direc.clear()
        self.comboBox_direc.addItem(self.direc_idx)
        if self.direc_idx != 'All':
            self.comboBox_direc.addItem('All')
        else:
            for idx, val in enumerate(sorted(self.selections.iloc[:,23].unique())):
                self.comboBox_direc.addItem(val)
        self.comboBox_frac.clear()
        self.comboBox_frac.addItem(self.frac_idx)
        if self.frac_idx != 'All':
            self.comboBox_frac.addItem('All')
        else:
            for idx, val in enumerate(sorted(self.selections.iloc[:,24].unique())):
                self.comboBox_frac.addItem(val)
        print('Selection boxes built')
        print('#############################################################################')                

    def getCoords(self, dataset):
        dataset = dataset[(dataset['Latitude'] >= 32) & (dataset['Latitude'] <= 42)]
        dataset = dataset[(dataset['Longitude'] >= -150) & (dataset['Longitude'] <= -50)]
        if self.lineEdit_maplatMin_sel.text() != '':
            dataset = dataset[dataset['Latitude'] >= float(self.lineEdit_maplatMin_sel.text())]
        if self.lineEdit_maplatMax_sel.text() != '':
            dataset = dataset[dataset['Latitude'] <= float(self.lineEdit_maplatMax_sel.text())]
        if self.lineEdit_maplonMin_sel.text() != '':
            dataset = dataset[dataset['Longitude'] >= float(self.lineEdit_maplonMin_sel.text())]
        if self.lineEdit_maplonMax_sel.text() != '':
            dataset = dataset[dataset['Longitude'] <= float(self.lineEdit_maplonMax_sel.text())]
        dataset['Latitude'] = dataset['Latitude'].values
        dataset['Longitude'] = dataset['Longitude'].values
        return dataset

    def processSelections(self):
        self.starttime_process = dt.datetime.now()        
        self.getlist = {}
        print('Processing selection: '+str(len(self.apilist))+' unique wells found')
        print('#############################################################################')
        commands = []
        for self.api in self.apilist:
            for stream in ['Production', 'Injection']:
                commands.append('sys\\fetch_prodinj.vbs '+stream+' '+str(self.api))
        print('Commands built, passing to VBScript...')
        print('#############################################################################')
        maxprocesses=20        
        pool = Pool(maxprocesses)
        for i, returncode in enumerate(pool.imap(partial(call, shell=True), commands)):
            self.timeDiff = ((dt.datetime.now() - self.starttime_process).total_seconds())/60
            self.timeFcst = format(self.timeDiff * ((1/((i+1)/len(commands))) - 1), ".1f")
            print(str(round(100*(i+1)/len(commands),1))+'% complete: '+str(commands[i][22:])+', '+self.timeFcst+' min(s) left')
            if returncode != 0:
               print("**ERROR** %d failed" % (commands[i][22:]))
        pool.close() #add not in build
        pool.join() #add not in build
        print('Fetch job complete!')
        print('#############################################################################')
        print('Processing excel files')
        for self.api in self.apilist:
            self.processExcel()
        print('Processing job complete!')
        print('#############################################################################')
        self.compile_wells()
        self.label_wellsSelected.setText(_translate("MainWindow", 'Fetch job complete!', None))

    def processExcel(self):
        self.compiler = {}
        self.build = {}
        self.header = {}
        self.compile = pd.DataFrame()
        attempt = 1
        while attempt <= 20:
            try:
                self.build['prod'] = pd.ExcelFile('wells/'+str(self.api)+'_Production.xlsx')\
                        .parse('Well Production', header=None)
                os.remove('wells/'+str(self.api)+'_Production.xlsx')
            except:
                print('build prod fail: '+str(self.api)+' attempt: '+str(attempt))
                attempt = attempt + 1
                continue
            break       
        attempt = 1
        while attempt <= 20:
            try:
                self.build['inj'] = pd.ExcelFile('wells/'+str(self.api)+'_Injection.xlsx')\
                        .parse('Well Injection', header=None)
                os.remove('wells/'+str(self.api)+'_Injection.xlsx')
            except:
                print('build inj fail: '+str(self.api)+' attempt: '+str(attempt))
                attempt = attempt + 1
                continue
            break 
        for self.build['idx_hdr'], self.build['data'] in enumerate(self.build['prod'].iloc[0,:15]):
            self.header[self.build['data']] = self.build['prod'].iloc[1][self.build['idx_hdr']]
        self.build['prod_dates'] = pd.DataFrame(data=self.build['prod'].iloc[4:,1].unique())
        self.build['inj_dates'] = pd.DataFrame(data=self.build['inj'].iloc[4:,1].unique())
        self.build['dates'] = pd.DataFrame(data=self.build['prod_dates'].append(self.build['inj_dates'])[0].unique())
        self.build['dates'] = self.build['dates'][~self.build['dates'][0].str.contains('Total')]
        self.build['prod_pool'] = pd.DataFrame(data=self.build['prod'].iloc[4:,15].unique())
        self.build['inj_pool'] = pd.DataFrame(data=self.build['inj'].iloc[4:,11].unique())
        self.build['pools'] = pd.DataFrame(data=self.build['prod_pool'].append(self.build['inj_pool'])[0].unique())
        self.build['pools'] = self.build['pools'][pd.notnull(self.build['pools'][0])]
        self.build['prodinj'] = pd.DataFrame(data=self.build['dates'][0], columns=['Month'])
        for self.build['col'] in ['Field Name',
                    'Latitude',
                    'Lease Name',
                    'Longitude',
                    'Operator Name',
                    'Range',
                    'Section',
                    'Township',
                    'Well #']:
            self.build['prodinj'][self.build['col']] = self.header[self.build['col']]
        self.build['prodinj']['API10'] = '04'+str(self.header['API #'])
        self.build['prodinj'] = self.build['prodinj'].rename(columns={'Well #':'Well'})
        self.build['prod_used'] = False
        self.build['inj_used'] = False
        if len(self.build['prod_dates']) > 0:
            self.build['prod_data'] = self.build['prod'].iloc[4:,:17]
            self.build['prod_data'].columns = self.build['prod'].iloc[3,:17]
            self.build['prod_data'] = self.build['prod_data'].rename(columns={'Well Type':'Well Type Prod'})
            self.build['prod_data'] = self.build['prod_data'].drop(['Status', 'API Number', 'Gravity of Oil', 'Casing Pressure', 'Tubing Pressure', 'BTU', 'Method of Operation', 'Water Disposition', 'PWT Status', 'Reported Date'], axis=1)
            self.build['prodinj'] = self.build['prodinj'].merge(self.build['prod_data'], how='left', left_on=['Month'], right_on=['Production Date'])
            self.build['prodinj'] = self.build['prodinj'].drop(['Production Date'], axis=1)
            self.build['prod_used'] = True
        if len(self.build['inj_dates']) > 0:
            self.build['inj_data'] = self.build['inj'].iloc[4:,:13]
            self.build['inj_data'].columns = self.build['inj'].iloc[3,:13]
            self.build['inj_data'] = self.build['inj_data'].rename(columns={'Well Type':'Well Type Inj'})
            self.build['inj_data'] = self.build['inj_data'].drop(['Status', 'API Number', 'Surface Injection Pressure', 'Source of Water', 'Kind of Water', 'PWT Status', 'Reported Date'], axis=1)
            if self.build['prod_used'] == True:
                self.build['prodinj'] = self.build['prodinj'].merge(self.build['inj_data'], how='left', left_on=['Month','Pool Code'], right_on=['Injection Date','Pool Code'])
            else:
                self.build['prodinj'] = self.build['prodinj'].merge(self.build['inj_data'], how='left', left_on=['Month'], right_on=['Injection Date'])
            self.build['prodinj'] = self.build['prodinj'].drop(['Injection Date'], axis=1)
            self.build['inj_used'] = True
        for self.build['product'] in ['Days Well Injected', 'Days Well Produced', 'Gas Produced (Mcf)', 'Gas or Air Injected (Mcf)', 'Oil Produced (bbl)', 'Water Produced (bbl)', 'Water or Steam Injected (bbl)']:
            try:
                self.build['prodinj'][self.build['product']] = self.build['prodinj'][self.build['product']].fillna(0)
            except:
                pass
        self.build['prodinj']['Month'] = pd.to_datetime(self.build['prodinj']['Month'], format='%b-%Y')
        self.build['prodinj']['Spud'] = pd.to_datetime(self.build['prodinj']['Month'].min(), format='%b-%Y')
        if self.build['prod_used'] == True:
            if self.build['inj_used'] == True:
                self.build['prodinj'] = self.build['prodinj'][(self.build['prodinj']['Days Well Injected'] > 0) | (self.build['prodinj']['Days Well Produced'] > 0)]
            else:
                self.build['prodinj'] = self.build['prodinj'][self.build['prodinj']['Days Well Produced'] > 0]
        else:
            if self.build['inj_used'] == True:
                self.build['prodinj'] = self.build['prodinj'][self.build['prodinj']['Days Well Injected'] > 0]
        self.build['prodinj'] = self.build['prodinj'].drop_duplicates()
        self.compile = self.compile.append(self.build['prodinj'])
        try:
            self.compile['Cyclic Injected (bbl)'] = self.compile['Water or Steam Injected (bbl)']
        except:
            pass
        try:
            self.compile['Continous Injected (bbl)'] = self.compile['Water or Steam Injected (bbl)']
        except:
            pass
        try:
            self.compile['Water Injected (bbl)'] = self.compile['Water or Steam Injected (bbl)']
        except:
            pass
        try:
            self.compile.ix[self.compile['Well Type Inj'] != 'SC', 'Cyclic Injected (bbl)'] = 0
        except:
            pass
        try:
            self.compile.ix[self.compile['Well Type Inj'] != 'SF', 'Continous Injected (bbl)'] = 0
        except:
            pass
        try:
            self.compile.ix[self.compile['Well Type Inj'] != 'WD', 'Water Injected (bbl)'] = 0
        except:
            pass
        try:
            self.compile['Total Steam Injected (bbl)'] = self.compile['Cyclic Injected (bbl)'] + self.compile['Continous Injected (bbl)']
        except:
            pass
        try:
            self.compile = self.compile.drop(['Water or Steam Injected (bbl)'], axis=1)
        except:
            pass
        try:
            self.compile = self.compile.drop(['Gas or Air Injected (Mcf)'], axis=1)
        except:
            pass

        for self.compiler['product'] in ['Days Well Injected', 'Days Well Produced', 'Gas Produced (Mcf)', 'Oil Produced (bbl)', 'Water Produced (bbl)', 'Water Injected (bbl)', 'Continous Injected (bbl)', 'Cyclic Injected (bbl)', 'Total Steam Injected (bbl)']:
            try:
                self.compile[self.compiler['product']] = self.compile[self.compiler['product']].fillna(0)
            except:
                pass
        self.compile.to_pickle('wells/doggrScraper_'+self.lineEdit_filename.text()+'_'+str(self.api)+'.pk1')

    def compile_wells(self):
        print('Compiling wells...')
        filenames = glob.glob('wells/doggrScraper_'+self.lineEdit_filename.text()+'_*.pk1')
        df_compiles = pd.DataFrame()
        compiles = []
        for file_ in filenames:
            df_compiles_ind = pd.read_pickle(file_)
            compiles.append(df_compiles_ind)
            os.remove(file_)
        df_compiles = pd.concat(compiles)
        del df_compiles_ind
        df_compiles.to_csv('exports/doggrScraper_'+self.lineEdit_filename.text()+'.csv', index=False)
        self.prod_data = df_compiles
        self.prod_data_lim = df_compiles
        print('Job complete!')
        print('#############################################################################')

##########################  FUNCTIONAL CODE ABOVE HERE  #############################

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mainWindow = QtGui.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

