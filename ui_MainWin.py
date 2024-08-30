# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWinVLQnuk.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 592)
        self.actionabout = QAction(MainWindow)
        self.actionabout.setObjectName(u"actionabout")
        self.verticalLayoutWidget = QWidget(MainWindow)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.imageLabel = QLabel(self.verticalLayoutWidget)
        self.imageLabel.setObjectName(u"imageLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageLabel.sizePolicy().hasHeightForWidth())
        self.imageLabel.setSizePolicy(sizePolicy)
        self.imageLabel.setMinimumSize(QSize(500, 500))
        self.imageLabel.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.imageLabel)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_width = QLabel(self.verticalLayoutWidget)
        self.label_width.setObjectName(u"label_width")

        self.horizontalLayout_3.addWidget(self.label_width)

        self.widthLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.widthLineEdit.setObjectName(u"widthLineEdit")

        self.horizontalLayout_3.addWidget(self.widthLineEdit)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_high = QLabel(self.verticalLayoutWidget)
        self.label_high.setObjectName(u"label_high")

        self.horizontalLayout_5.addWidget(self.label_high)

        self.heightLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.heightLineEdit.setObjectName(u"heightLineEdit")

        self.horizontalLayout_5.addWidget(self.heightLineEdit)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_resolution = QLabel(self.verticalLayoutWidget)
        self.label_resolution.setObjectName(u"label_resolution")

        self.horizontalLayout_4.addWidget(self.label_resolution)

        self.resolutionLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.resolutionLineEdit.setObjectName(u"resolutionLineEdit")

        self.horizontalLayout_4.addWidget(self.resolutionLineEdit)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.sizeLimitLabel = QLabel(self.verticalLayoutWidget)
        self.sizeLimitLabel.setObjectName(u"sizeLimitLabel")

        self.horizontalLayout_6.addWidget(self.sizeLimitLabel)

        self.sizeLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.sizeLineEdit.setObjectName(u"sizeLineEdit")

        self.horizontalLayout_6.addWidget(self.sizeLineEdit)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_6.addWidget(self.label)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.openButton = QPushButton(self.verticalLayoutWidget)
        self.openButton.setObjectName(u"openButton")

        self.horizontalLayout.addWidget(self.openButton)

        self.exportButton = QPushButton(self.verticalLayoutWidget)
        self.exportButton.setObjectName(u"exportButton")

        self.horizontalLayout.addWidget(self.exportButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.verticalLayoutWidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 700, 24))
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u4e2a\u4eba\u6863\u6848\u7167\u7247\u5904\u7406\u5de5\u5177", None))
        self.actionabout.setText(QCoreApplication.translate("MainWindow", u"about", None))
        self.imageLabel.setText("")
        self.label_width.setText(QCoreApplication.translate("MainWindow", u"\u5bbd", None))
        self.widthLineEdit.setText(QCoreApplication.translate("MainWindow", u"358", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"px", None))
        self.label_high.setText(QCoreApplication.translate("MainWindow", u"\u9ad8", None))
        self.heightLineEdit.setText(QCoreApplication.translate("MainWindow", u"441", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"px", None))
        self.label_resolution.setText(QCoreApplication.translate("MainWindow", u"\u5206\u8fa8\u7387", None))
        self.resolutionLineEdit.setText(QCoreApplication.translate("MainWindow", u"350", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"dpi", None))
        self.sizeLimitLabel.setText(QCoreApplication.translate("MainWindow", u"\u5927\u5c0f\u9650\u5236", None))
        self.sizeLineEdit.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"kb", None))
        self.openButton.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u7167\u7247", None))
        self.exportButton.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u7167\u7247", None))
    # retranslateUi

