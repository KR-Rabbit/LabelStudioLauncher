# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Conda.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtWidgets import (QComboBox, QLabel, QLineEdit,
                               QMenuBar, QPushButton, QRadioButton,
                               QSizePolicy, QStatusBar, QWidget)


class Ui_Conda(object):
    def setupUi(self, Conda):
        if not Conda.objectName():
            Conda.setObjectName(u"Conda")
        Conda.setWindowModality(Qt.ApplicationModal)
        Conda.resize(605, 386)
        self.centralwidget = QWidget(Conda)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_conda_tip = QLabel(self.centralwidget)
        self.label_conda_tip.setObjectName(u"label_conda_tip")
        self.label_conda_tip.setGeometry(QRect(70, 60, 101, 25))
        self.lineEdit_conda = QLineEdit(self.centralwidget)
        self.lineEdit_conda.setObjectName(u"lineEdit_conda")
        self.lineEdit_conda.setGeometry(QRect(200, 60, 256, 25))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_conda.sizePolicy().hasHeightForWidth())
        self.lineEdit_conda.setSizePolicy(sizePolicy)
        self.lineEdit_conda.setMinimumSize(QSize(256, 25))
        self.lineEdit_conda.setReadOnly(True)
        self.pushButton_select = QPushButton(self.centralwidget)
        self.pushButton_select.setObjectName(u"pushButton_select")
        self.pushButton_select.setGeometry(QRect(470, 60, 80, 25))
        sizePolicy.setHeightForWidth(self.pushButton_select.sizePolicy().hasHeightForWidth())
        self.pushButton_select.setSizePolicy(sizePolicy)
        self.pushButton_select.setMinimumSize(QSize(80, 25))
        self.comboBox_envs = QComboBox(self.centralwidget)
        self.comboBox_envs.setObjectName(u"comboBox_envs")
        self.comboBox_envs.setGeometry(QRect(200, 160, 221, 25))
        self.radioButton_current = QRadioButton(self.centralwidget)
        self.radioButton_current.setObjectName(u"radioButton_current")
        self.radioButton_current.setGeometry(QRect(70, 120, 95, 20))
        self.radioButton_current.setChecked(True)
        self.radioButton_new = QRadioButton(self.centralwidget)
        self.radioButton_new.setObjectName(u"radioButton_new")
        self.radioButton_new.setGeometry(QRect(210, 120, 95, 20))
        self.label_env_name_tip = QLabel(self.centralwidget)
        self.label_env_name_tip.setObjectName(u"label_env_name_tip")
        self.label_env_name_tip.setGeometry(QRect(70, 160, 100, 25))
        sizePolicy.setHeightForWidth(self.label_env_name_tip.sizePolicy().hasHeightForWidth())
        self.label_env_name_tip.setSizePolicy(sizePolicy)
        self.label_env_name_tip.setMinimumSize(QSize(100, 25))
        self.label_env_name_tip.setMaximumSize(QSize(100, 25))
        self.lineEdit_env_name = QLineEdit(self.centralwidget)
        self.lineEdit_env_name.setObjectName(u"lineEdit_env_name")
        self.lineEdit_env_name.setGeometry(QRect(200, 160, 160, 25))
        sizePolicy.setHeightForWidth(self.lineEdit_env_name.sizePolicy().hasHeightForWidth())
        self.lineEdit_env_name.setSizePolicy(sizePolicy)
        self.lineEdit_env_name.setMinimumSize(QSize(160, 25))
        self.lineEdit_env_name.setMaximumSize(QSize(160, 25))
        self.lineEdit_env_name.setClearButtonEnabled(True)
        self.label_version_tip = QLabel(self.centralwidget)
        self.label_version_tip.setObjectName(u"label_version_tip")
        self.label_version_tip.setGeometry(QRect(70, 200, 100, 25))
        sizePolicy.setHeightForWidth(self.label_version_tip.sizePolicy().hasHeightForWidth())
        self.label_version_tip.setSizePolicy(sizePolicy)
        self.label_version_tip.setMinimumSize(QSize(100, 25))
        self.label_version_tip.setMaximumSize(QSize(100, 25))
        self.comboBox_version = QComboBox(self.centralwidget)
        self.comboBox_version.addItem("")
        self.comboBox_version.addItem("")
        self.comboBox_version.addItem("")
        self.comboBox_version.addItem("")
        self.comboBox_version.addItem("")
        self.comboBox_version.addItem("")
        self.comboBox_version.setObjectName(u"comboBox_version")
        self.comboBox_version.setGeometry(QRect(200, 200, 80, 22))
        sizePolicy.setHeightForWidth(self.comboBox_version.sizePolicy().hasHeightForWidth())
        self.comboBox_version.setSizePolicy(sizePolicy)
        self.comboBox_version.setMinimumSize(QSize(80, 20))
        self.comboBox_version.setMaximumSize(QSize(80, 25))
        self.comboBox_version.setStyleSheet(u"font: 10pt \"Microsoft YaHei UI\";")
        Conda.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Conda)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 605, 22))
        Conda.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Conda)
        self.statusbar.setObjectName(u"statusbar")
        Conda.setStatusBar(self.statusbar)

        self.retranslateUi(Conda)
        self.pushButton_select.clicked.connect(Conda.select_conda)
        self.comboBox_envs.activated.connect(Conda.update_env_name)

        QMetaObject.connectSlotsByName(Conda)

    # setupUi

    def retranslateUi(self, Conda):
        Conda.setWindowTitle(QCoreApplication.translate("Conda", u"Codna", None))
        self.label_conda_tip.setText(
            QCoreApplication.translate("Conda", u"Conda\u53ef\u6267\u884c\u6587\u4ef6\uff1a", None))
        self.pushButton_select.setText(QCoreApplication.translate("Conda", u"\u9009\u62e9", None))
        self.radioButton_current.setText(
            QCoreApplication.translate("Conda", u"\u4f7f\u7528\u73b0\u6709\u73af\u5883", None))
        self.radioButton_new.setText(QCoreApplication.translate("Conda", u"\u521b\u9020\u65b0\u73af\u5883", None))
        self.label_env_name_tip.setText(QCoreApplication.translate("Conda", u"\u73af\u5883\u540d\u79f0\uff1a", None))
        self.label_version_tip.setText(QCoreApplication.translate("Conda", u"Python\u7248\u672c\uff1a", None))
        self.comboBox_version.setItemText(0, QCoreApplication.translate("Conda", u"3.11", None))
        self.comboBox_version.setItemText(1, QCoreApplication.translate("Conda", u"3.10", None))
        self.comboBox_version.setItemText(2, QCoreApplication.translate("Conda", u"3.9", None))
        self.comboBox_version.setItemText(3, QCoreApplication.translate("Conda", u"3.8", None))
        self.comboBox_version.setItemText(4, QCoreApplication.translate("Conda", u"3.7", None))
        self.comboBox_version.setItemText(5, QCoreApplication.translate("Conda", u"3.6", None))

        self.comboBox_version.setCurrentText(QCoreApplication.translate("Conda", u"3.11", None))
    # retranslateUi
