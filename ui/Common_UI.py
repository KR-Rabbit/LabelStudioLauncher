# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Common.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtWidgets import (QCheckBox, QGridLayout, QGroupBox,
                               QHBoxLayout, QRadioButton, QSizePolicy,
                               QStatusBar, QVBoxLayout, QWidget)


class Ui_Common(object):
    def setupUi(self, Common):
        if not Common.objectName():
            Common.setObjectName(u"Common")
        Common.setWindowModality(Qt.ApplicationModal)
        Common.resize(500, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Common.sizePolicy().hasHeightForWidth())
        Common.setSizePolicy(sizePolicy)
        Common.setMinimumSize(QSize(500, 300))
        Common.setMaximumSize(QSize(500, 300))
        self.centralwidget = QWidget(Common)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(50, -1, -1, 50)
        self.radioButton_min = QRadioButton(self.groupBox)
        self.radioButton_min.setObjectName(u"radioButton_min")
        self.radioButton_min.setStyleSheet(u"")

        self.gridLayout.addWidget(self.radioButton_min, 0, 0, 1, 1)

        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 0, 1, 1, 1)

        self.radioButton_close = QRadioButton(self.groupBox)
        self.radioButton_close.setObjectName(u"radioButton_close")
        self.radioButton_close.setStyleSheet(u"")

        self.gridLayout.addWidget(self.radioButton_close, 1, 0, 1, 1)

        self.horizontalLayout_2.addLayout(self.gridLayout)

        self.verticalLayout.addWidget(self.groupBox)

        Common.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Common)
        self.statusbar.setObjectName(u"statusbar")
        Common.setStatusBar(self.statusbar)

        self.retranslateUi(Common)
        self.checkBox.clicked["bool"].connect(Common.on_checked)

        QMetaObject.connectSlotsByName(Common)

    # setupUi

    def retranslateUi(self, Common):
        Common.setWindowTitle(QCoreApplication.translate("Common", u"\u5e38\u89c4\u8bbe\u7f6e", None))
        self.groupBox.setTitle(QCoreApplication.translate("Common", u"\u5173\u95ed\u7a0b\u5e8f", None))
        self.radioButton_min.setText(QCoreApplication.translate("Common",
                                                                u"\u6700\u5c0f\u5316\u5230\u6258\u76d8\uff0c\u4e0d\u9000\u51fa\u7a0b\u5e8f",
                                                                None))
        self.checkBox.setText(QCoreApplication.translate("Common", u"\u9000\u51fa\u65f6\u4e8c\u6b21\u786e\u8ba4", None))
        self.radioButton_close.setText(QCoreApplication.translate("Common", u"\u9000\u51fa\u7a0b\u5e8f", None))
    # retranslateUi
