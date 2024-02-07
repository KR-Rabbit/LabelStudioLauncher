# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Server.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_Server(object):
    def setupUi(self, Server):
        if not Server.objectName():
            Server.setObjectName(u"Server")
        Server.setWindowModality(Qt.ApplicationModal)
        Server.resize(640, 400)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Server.sizePolicy().hasHeightForWidth())
        Server.setSizePolicy(sizePolicy)
        Server.setMinimumSize(QSize(640, 400))
        Server.setMaximumSize(QSize(760, 500))
        self.centralwidget = QWidget(Server)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_5 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_studio = QGroupBox(self.centralwidget)
        self.groupBox_studio.setObjectName(u"groupBox_studio")
        sizePolicy.setHeightForWidth(self.groupBox_studio.sizePolicy().hasHeightForWidth())
        self.groupBox_studio.setSizePolicy(sizePolicy)
        self.groupBox_studio.setMinimumSize(QSize(600, 180))
        self.groupBox_studio.setMaximumSize(QSize(800, 400))
        self.groupBox_studio.setFlat(False)
        self.groupBox_studio.setCheckable(False)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_studio)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
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

        self.horizontalLayout_6.addWidget(self.pushButton_check)

        self.pushButton_install = QPushButton(self.groupBox_studio)
        self.pushButton_install.setObjectName(u"pushButton_install")
        sizePolicy1.setHeightForWidth(self.pushButton_install.sizePolicy().hasHeightForWidth())
        self.pushButton_install.setSizePolicy(sizePolicy1)
        self.pushButton_install.setMinimumSize(QSize(50, 25))
        self.pushButton_install.setMaximumSize(QSize(50, 25))
        self.pushButton_install.setCheckable(False)
        self.pushButton_install.setChecked(False)

        self.horizontalLayout_6.addWidget(self.pushButton_install)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

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


        self.verticalLayout_2.addLayout(self.horizontalLayout)

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


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.checkBox_recursive = QCheckBox(self.groupBox_studio)
        self.checkBox_recursive.setObjectName(u"checkBox_recursive")
        self.checkBox_recursive.setMinimumSize(QSize(90, 25))
        self.checkBox_recursive.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_3.addWidget(self.checkBox_recursive)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addWidget(self.groupBox_studio)

        self.groupBox_http = QGroupBox(self.centralwidget)
        self.groupBox_http.setObjectName(u"groupBox_http")
        sizePolicy.setHeightForWidth(self.groupBox_http.sizePolicy().hasHeightForWidth())
        self.groupBox_http.setSizePolicy(sizePolicy)
        self.groupBox_http.setMinimumSize(QSize(600, 120))
        self.groupBox_http.setMaximumSize(QSize(800, 220))
        self.verticalLayout = QVBoxLayout(self.groupBox_http)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.label_ip = QLabel(self.groupBox_http)
        self.label_ip.setObjectName(u"label_ip")

        self.horizontalLayout_7.addWidget(self.label_ip)

        self.lineEdit_ip = QLineEdit(self.groupBox_http)
        self.lineEdit_ip.setObjectName(u"lineEdit_ip")
        self.lineEdit_ip.setMinimumSize(QSize(100, 20))
        self.lineEdit_ip.setMaxLength(16)

        self.horizontalLayout_7.addWidget(self.lineEdit_ip)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)

        self.label_port = QLabel(self.groupBox_http)
        self.label_port.setObjectName(u"label_port")

        self.horizontalLayout_8.addWidget(self.label_port)

        self.lineEdit_port = QLineEdit(self.groupBox_http)
        self.lineEdit_port.setObjectName(u"lineEdit_port")
        self.lineEdit_port.setMinimumSize(QSize(100, 20))
        self.lineEdit_port.setMaxLength(5)

        self.horizontalLayout_8.addWidget(self.lineEdit_port)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout_8)


        self.verticalLayout_3.addWidget(self.groupBox_http)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(50, 0))
        self.groupBox.setMaximumSize(QSize(16777215, 60))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.pushButton_generate = QPushButton(self.groupBox)
        self.pushButton_generate.setObjectName(u"pushButton_generate")
        sizePolicy1.setHeightForWidth(self.pushButton_generate.sizePolicy().hasHeightForWidth())
        self.pushButton_generate.setSizePolicy(sizePolicy1)
        self.pushButton_generate.setMinimumSize(QSize(100, 25))
        self.pushButton_generate.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_4.addWidget(self.pushButton_generate)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.verticalLayout_3.addWidget(self.groupBox)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

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
        self.checkBox_recursive.stateChanged.connect(Server.change_recursive)

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
        self.checkBox_recursive.setText(QCoreApplication.translate("Server", u"\u641c\u7d22\u5b50\u76ee\u5f55", None))
        self.groupBox_http.setTitle(QCoreApplication.translate("Server", u"HTTP", None))
        self.label_ip.setText(QCoreApplication.translate("Server", u"IP\u5730\u5740", None))
        self.label_port.setText(QCoreApplication.translate("Server", u"\u7aef\u53e3\u53f7", None))
        self.groupBox.setTitle("")
        self.pushButton_generate.setText(QCoreApplication.translate("Server", u"\u751f\u6210JSON\u6587\u4ef6", None))
    # retranslateUi

