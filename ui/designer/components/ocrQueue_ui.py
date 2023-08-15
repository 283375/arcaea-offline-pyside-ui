# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ocrQueue.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QGroupBox,
    QHBoxLayout, QHeaderView, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
    QWidget)

class Ui_OcrQueue(object):
    def setupUi(self, OcrQueue):
        if not OcrQueue.objectName():
            OcrQueue.setObjectName(u"OcrQueue")
        OcrQueue.resize(741, 372)
        self.horizontalLayout_2 = QHBoxLayout(OcrQueue)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_3 = QGroupBox(OcrQueue)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ocr_addImageButton = QPushButton(self.groupBox_3)
        self.ocr_addImageButton.setObjectName(u"ocr_addImageButton")

        self.verticalLayout_2.addWidget(self.ocr_addImageButton)

        self.ocr_removeSelectedButton = QPushButton(self.groupBox_3)
        self.ocr_removeSelectedButton.setObjectName(u"ocr_removeSelectedButton")
        self.ocr_removeSelectedButton.setEnabled(True)

        self.verticalLayout_2.addWidget(self.ocr_removeSelectedButton)

        self.ocr_removeAllButton = QPushButton(self.groupBox_3)
        self.ocr_removeAllButton.setObjectName(u"ocr_removeAllButton")
        self.ocr_removeAllButton.setEnabled(True)

        self.verticalLayout_2.addWidget(self.ocr_removeAllButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.ocr_startButton = QPushButton(self.groupBox_3)
        self.ocr_startButton.setObjectName(u"ocr_startButton")

        self.verticalLayout_2.addWidget(self.ocr_startButton)


        self.horizontalLayout_2.addWidget(self.groupBox_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tableView = QTableView(OcrQueue)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.tableView.setSelectionMode(QAbstractItemView.MultiSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableView.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout_3.addWidget(self.tableView)

        self.progressBar = QProgressBar(OcrQueue)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(0)
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setFormat(u"%v/%m - %p%")

        self.verticalLayout_3.addWidget(self.progressBar)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.groupBox_5 = QGroupBox(OcrQueue)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.ocr_acceptSelectedButton = QPushButton(self.groupBox_5)
        self.ocr_acceptSelectedButton.setObjectName(u"ocr_acceptSelectedButton")
        self.ocr_acceptSelectedButton.setEnabled(True)

        self.verticalLayout_4.addWidget(self.ocr_acceptSelectedButton)

        self.ocr_acceptAllButton = QPushButton(self.groupBox_5)
        self.ocr_acceptAllButton.setObjectName(u"ocr_acceptAllButton")

        self.verticalLayout_4.addWidget(self.ocr_acceptAllButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.ocr_ignoreValidateCheckBox = QCheckBox(self.groupBox_5)
        self.ocr_ignoreValidateCheckBox.setObjectName(u"ocr_ignoreValidateCheckBox")

        self.verticalLayout_4.addWidget(self.ocr_ignoreValidateCheckBox)


        self.horizontalLayout_2.addWidget(self.groupBox_5)


        self.retranslateUi(OcrQueue)

        QMetaObject.connectSlotsByName(OcrQueue)
    # setupUi

    def retranslateUi(self, OcrQueue):
        OcrQueue.setWindowTitle(QCoreApplication.translate("OcrQueue", u"OcrQueue", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("OcrQueue", u"ocr.queue.title", None))
        self.ocr_addImageButton.setText(QCoreApplication.translate("OcrQueue", u"ocr.queue.addImageButton", None))
        self.ocr_removeSelectedButton.setText(QCoreApplication.translate("OcrQueue", u"ocr.queue.removeSelected", None))
        self.ocr_removeAllButton.setText(QCoreApplication.translate("OcrQueue", u"ocr.queue.removeAll", None))
        self.ocr_startButton.setText(QCoreApplication.translate("OcrQueue", u"ocr.queue.startOcrButton", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("OcrQueue", u"ocr.results", None))
        self.ocr_acceptSelectedButton.setText(QCoreApplication.translate("OcrQueue", u"ocr.results.acceptSelectedButton", None))
        self.ocr_acceptAllButton.setText(QCoreApplication.translate("OcrQueue", u"ocr.results.acceptAllButton", None))
        self.ocr_ignoreValidateCheckBox.setText(QCoreApplication.translate("OcrQueue", u"ocr.results.ignoreValidate", None))
    # retranslateUi
