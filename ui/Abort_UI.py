# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Abort.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)
from . import ico_rc

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
        self.label.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setOpenExternalLinks(True)

        self.retranslateUi(Abort)

        QMetaObject.connectSlotsByName(Abort)
    # setupUi

    def retranslateUi(self, Abort):
        Abort.setWindowTitle(QCoreApplication.translate("Abort", u"\u5173\u4e8e", None))
        self.label.setText(QCoreApplication.translate("Abort", u"<html><head/><body><p><a href=\"https://github.com/KR-Rabbit/LabelStudioLauncher/blob/master/README.md\"><span style=\" text-decoration: underline; color:#0000ff;\">Here</span></a></p></body></html>", None))
    # retranslateUi

