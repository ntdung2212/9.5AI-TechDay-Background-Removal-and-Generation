# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QTextBrowser, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(773, 370)
        self.Title = QTextBrowser(Widget)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(260, 0, 256, 41))
        self.GetFilePath = QPushButton(Widget)
        self.GetFilePath.setObjectName(u"GetFilePath")
        self.GetFilePath.setGeometry(QRect(20, 320, 121, 31))
        font = QFont()
        font.setPointSize(12)
        self.GetFilePath.setFont(font)
        self.RunBgR = QPushButton(Widget)
        self.RunBgR.setObjectName(u"RunBgR")
        self.RunBgR.setGeometry(QRect(260, 320, 121, 31))
        self.RunBgR.setFont(font)
        self.SavePNG = QPushButton(Widget)
        self.SavePNG.setObjectName(u"SavePNG")
        self.SavePNG.setGeometry(QRect(530, 320, 121, 31))
        self.SavePNG.setFont(font)
        self.InputView = QLabel(Widget)
        self.InputView.setObjectName(u"InputView")
        self.InputView.setGeometry(QRect(30, 50, 351, 251))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputView.sizePolicy().hasHeightForWidth())
        self.InputView.setSizePolicy(sizePolicy)
        self.InputView.setScaledContents(True)
        self.InputView.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.OutputView = QLabel(Widget)
        self.OutputView.setObjectName(u"OutputView")
        self.OutputView.setGeometry(QRect(410, 50, 351, 251))
        sizePolicy.setHeightForWidth(self.OutputView.sizePolicy().hasHeightForWidth())
        self.OutputView.setSizePolicy(sizePolicy)
        self.OutputView.setScaledContents(True)
        self.OutputView.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.Title.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Background Removal</span></p></body></html>", None))
        self.GetFilePath.setText(QCoreApplication.translate("Widget", u"Select an image", None))
        self.RunBgR.setText(QCoreApplication.translate("Widget", u"Run", None))
        self.SavePNG.setText(QCoreApplication.translate("Widget", u"Save Picture", None))
        self.InputView.setText("")
        self.OutputView.setText("")
    # retranslateUi

