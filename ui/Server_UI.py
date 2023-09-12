# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Server.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtWidgets import (QGroupBox, QHBoxLayout, QLabel,
                               QLineEdit, QPushButton, QSizePolicy,
                               QSpacerItem, QStatusBar, QVBoxLayout, QWidget)


class Ui_Server(object):
    def setupUi(self, Server):
        if not Server.objectName():
            Server.setObjectName(u"Server")
        Server.setWindowModality(Qt.ApplicationModal)
        Server.resize(640, 240)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Server.sizePolicy().hasHeightForWidth())
        Server.setSizePolicy(sizePolicy)
        Server.setMinimumSize(QSize(640, 240))
        self.centralwidget = QWidget(Server)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_6 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.groupBox_studio = QGroupBox(self.centralwidget)
        self.groupBox_studio.setObjectName(u"groupBox_studio")
        self.groupBox_studio.setMinimumSize(QSize(600, 180))
        self.groupBox_studio.setMaximumSize(QSize(400, 400))
        self.groupBox_studio.setFlat(False)
        self.groupBox_studio.setCheckable(False)
        self.verticalLayout = QVBoxLayout(self.groupBox_studio)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 5)
        self.pushButton_check = QPushButton(self.groupBox_studio)
        self.pushButton_check.setObjectName(u"pushButton_check")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_check.sizePolicy().hasHeightForWidth())
        self.pushButton_check.setSizePolicy(sizePolicy1)
        self.pushButton_check.setMinimumSize(QSize(50, 25))
        self.pushButton_check.setMaximumSize(QSize(50, 25))
        self.pushButton_check.setAutoDefault(False)
        self.pushButton_check.setFlat(False)

        self.horizontalLayout_3.addWidget(self.pushButton_check)

        self.pushButton_install = QPushButton(self.groupBox_studio)
        self.pushButton_install.setObjectName(u"pushButton_install")
        sizePolicy1.setHeightForWidth(self.pushButton_install.sizePolicy().hasHeightForWidth())
        self.pushButton_install.setSizePolicy(sizePolicy1)
        self.pushButton_install.setMinimumSize(QSize(50, 25))
        self.pushButton_install.setMaximumSize(QSize(50, 25))
        self.pushButton_install.setCheckable(False)
        self.pushButton_install.setChecked(False)

        self.horizontalLayout_3.addWidget(self.pushButton_install)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_data_root_tip = QLabel(self.groupBox_studio)
        self.label_data_root_tip.setObjectName(u"label_data_root_tip")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_data_root_tip.sizePolicy().hasHeightForWidth())
        self.label_data_root_tip.setSizePolicy(sizePolicy2)
        self.label_data_root_tip.setMinimumSize(QSize(60, 25))

        self.horizontalLayout.addWidget(self.label_data_root_tip)

        self.lineEdit_data_root = QLineEdit(self.groupBox_studio)
        self.lineEdit_data_root.setObjectName(u"lineEdit_data_root")
        self.lineEdit_data_root.setMinimumSize(QSize(290, 25))
        self.lineEdit_data_root.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEdit_data_root)

        self.pushButton_data_root = QPushButton(self.groupBox_studio)
        self.pushButton_data_root.setObjectName(u"pushButton_data_root")
        self.pushButton_data_root.setMinimumSize(QSize(50, 25))

        self.horizontalLayout.addWidget(self.pushButton_data_root)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_data_tip = QLabel(self.groupBox_studio)
        self.label_data_tip.setObjectName(u"label_data_tip")
        sizePolicy2.setHeightForWidth(self.label_data_tip.sizePolicy().hasHeightForWidth())
        self.label_data_tip.setSizePolicy(sizePolicy2)
        self.label_data_tip.setMinimumSize(QSize(60, 25))

        self.horizontalLayout_2.addWidget(self.label_data_tip)

        self.lineEdit_data = QLineEdit(self.groupBox_studio)
        self.lineEdit_data.setObjectName(u"lineEdit_data")
        self.lineEdit_data.setMinimumSize(QSize(290, 25))
        self.lineEdit_data.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_data)

        self.pushButton_data = QPushButton(self.groupBox_studio)
        self.pushButton_data.setObjectName(u"pushButton_data")
        self.pushButton_data.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_2.addWidget(self.pushButton_data)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.pushButton_generate = QPushButton(self.groupBox_studio)
        self.pushButton_generate.setObjectName(u"pushButton_generate")
        sizePolicy1.setHeightForWidth(self.pushButton_generate.sizePolicy().hasHeightForWidth())
        self.pushButton_generate.setSizePolicy(sizePolicy1)
        self.pushButton_generate.setMinimumSize(QSize(100, 25))
        self.pushButton_generate.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_4.addWidget(self.pushButton_generate)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalLayout_2.addWidget(self.groupBox_studio)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        Server.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Server)
        self.statusbar.setObjectName(u"statusbar")
        Server.setStatusBar(self.statusbar)

        self.retranslateUi(Server)
        self.pushButton_check.clicked.connect(Server.check_studio)
        self.pushButton_install.clicked.connect(Server.install_studio)
        self.pushButton_data_root.clicked.connect(Server.select_root)
        self.pushButton_data.clicked.connect(Server.select_data_path)
        self.pushButton_generate.clicked.connect(Server.generate_json)

        self.pushButton_check.setDefault(False)

        QMetaObject.connectSlotsByName(Server)

    # setupUi

    def retranslateUi(self, Server):
        Server.setWindowTitle(QCoreApplication.translate("Server", u"ServerSetting", None))
        self.groupBox_studio.setTitle(QCoreApplication.translate("Server", u"LabelStudio", None))
        self.pushButton_check.setText(QCoreApplication.translate("Server", u"\u68c0\u67e5", None))
        self.pushButton_install.setText(QCoreApplication.translate("Server", u"\u5b89\u88c5", None))
        self.label_data_root_tip.setText(QCoreApplication.translate("Server", u"\u6570\u636e\u6839\u76ee\u5f55", None))
        self.pushButton_data_root.setText(QCoreApplication.translate("Server", u"\u9009\u62e9", None))
        self.label_data_tip.setText(QCoreApplication.translate("Server", u"\u6570\u636e\u76ee\u5f55", None))
        self.pushButton_data.setText(QCoreApplication.translate("Server", u"\u9009\u62e9", None))
        self.pushButton_generate.setText(QCoreApplication.translate("Server", u"\u751f\u6210JSON\u6587\u4ef6", None))
    # retranslateUi
