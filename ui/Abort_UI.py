# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Abort.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            Qt)
from PySide6.QtWidgets import (QLabel, QSizePolicy)

from ui import ico_rc
class Ui_Abort(object):
    def setupUi(self, Abort):
        if not Abort.objectName():
            Abort.setObjectName(u"Abort")
        Abort.setWindowModality(Qt.ApplicationModal)
        Abort.resize(400, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Abort.sizePolicy().hasHeightForWidth())
        Abort.setSizePolicy(sizePolicy)
        Abort.setAutoFillBackground(False)
        Abort.setStyleSheet(u"#Abort{background-image: url(:/main/background.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center center;\n"
"background-attachment: fixed;}")
        self.label = QLabel(Abort)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 50, 71, 31))
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setOpenExternalLinks(True)

        self.retranslateUi(Abort)

        QMetaObject.connectSlotsByName(Abort)
    # setupUi

    def retranslateUi(self, Abort):
        Abort.setWindowTitle(QCoreApplication.translate("Abort", u"\u5173\u4e8e", None))
        self.label.setText(QCoreApplication.translate("Abort", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/KR-Rabbit/LabelStudioLauncher/blob/master/README.md\"><span style=\" font-size:10pt; font-weight:700; text-decoration: underline; color:#131522;\">Github</span></a></p></body></html>", None))
    # retranslateUi

