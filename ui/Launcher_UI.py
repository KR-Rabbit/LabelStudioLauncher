# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Launcher.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QMainWindow,
                               QMenu, QMenuBar, QPushButton, QSizePolicy,
                               QSpacerItem, QStatusBar, QTextBrowser, QVBoxLayout,
                               QWidget)
from . import ico_rc


class Ui_LabelStudio(object):
    def setupUi(self, LabelStudio):
        if not LabelStudio.objectName():
            LabelStudio.setObjectName(u"LabelStudio")
        LabelStudio.setWindowModality(Qt.ApplicationModal)
        LabelStudio.resize(800, 600)
        icon = QIcon()
        icon.addFile(u":/main/launcher.ico", QSize(), QIcon.Normal, QIcon.Off)
        LabelStudio.setWindowIcon(icon)
        self.actionSelectConda = QAction(LabelStudio)
        self.actionSelectConda.setObjectName(u"actionSelectConda")
        self.actionSetServer = QAction(LabelStudio)
        self.actionSetServer.setObjectName(u"actionSetServer")
        self.actionAbourt = QAction(LabelStudio)
        self.actionAbourt.setObjectName(u"actionAbourt")
        self.actionCommon = QAction(LabelStudio)
        self.actionCommon.setObjectName(u"actionCommon")
        self.actionAbort = QAction(LabelStudio)
        self.actionAbort.setObjectName(u"actionAbort")
        self.centralwidget = QWidget(LabelStudio)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.pushButton_start = QPushButton(self.centralwidget)
        self.pushButton_start.setObjectName(u"pushButton_start")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_start.sizePolicy().hasHeightForWidth())
        self.pushButton_start.setSizePolicy(sizePolicy)
        self.pushButton_start.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_4.addWidget(self.pushButton_start)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox_studio = QGroupBox(self.centralwidget)
        self.groupBox_studio.setObjectName(u"groupBox_studio")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_studio.sizePolicy().hasHeightForWidth())
        self.groupBox_studio.setSizePolicy(sizePolicy1)
        self.groupBox_studio.setMinimumSize(QSize(360, 400))
        self.horizontalLayout = QHBoxLayout(self.groupBox_studio)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.textBrowser_studio = QTextBrowser(self.groupBox_studio)
        self.textBrowser_studio.setObjectName(u"textBrowser_studio")
        self.textBrowser_studio.setOpenExternalLinks(True)

        self.horizontalLayout.addWidget(self.textBrowser_studio)

        self.horizontalLayout_3.addWidget(self.groupBox_studio)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        LabelStudio.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(LabelStudio)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuSetting = QMenu(self.menubar)
        self.menuSetting.setObjectName(u"menuSetting")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.menuSetting.sizePolicy().hasHeightForWidth())
        self.menuSetting.setSizePolicy(sizePolicy2)
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        LabelStudio.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(LabelStudio)
        self.statusbar.setObjectName(u"statusbar")
        LabelStudio.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menuSetting.addAction(self.actionSelectConda)
        self.menuSetting.addAction(self.actionSetServer)
        self.menuSetting.addAction(self.actionCommon)
        self.menu.addAction(self.actionAbort)

        self.retranslateUi(LabelStudio)
        self.actionSelectConda.triggered.connect(LabelStudio.set_conda)
        self.actionSetServer.triggered.connect(LabelStudio.set_server)
        self.pushButton_start.clicked.connect(LabelStudio.start)
        self.actionAbort.triggered.connect(LabelStudio.abort)
        self.actionCommon.triggered.connect(LabelStudio.set_common)

        QMetaObject.connectSlotsByName(LabelStudio)

    # setupUi

    def retranslateUi(self, LabelStudio):
        LabelStudio.setWindowTitle(QCoreApplication.translate("LabelStudio", u"LabelStudio", None))
        self.actionSelectConda.setText(QCoreApplication.translate("LabelStudio", u"\u9009\u62e9conda\u73af\u5883", None))
        self.actionSetServer.setText(QCoreApplication.translate("LabelStudio", u"\u670d\u52a1\u8bbe\u7f6e", None))
        self.actionAbourt.setText(QCoreApplication.translate("LabelStudio", u"\u5173\u4e8e", None))
        self.actionCommon.setText(QCoreApplication.translate("LabelStudio", u"\u5e38\u89c4\u8bbe\u7f6e", None))
        self.actionAbort.setText(QCoreApplication.translate("LabelStudio", u"\u5173\u4e8e", None))
        self.pushButton_start.setText(QCoreApplication.translate("LabelStudio", u"\u542f\u52a8", None))
        self.groupBox_studio.setTitle(QCoreApplication.translate("LabelStudio", u"Label Studio", None))
        self.menuSetting.setTitle(QCoreApplication.translate("LabelStudio", u"\u8bbe\u7f6e", None))
        self.menu.setTitle(QCoreApplication.translate("LabelStudio", u"\u5e2e\u52a9", None))
    # retranslateUi
