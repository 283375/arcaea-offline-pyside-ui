# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabDbEntry.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QTabWidget, QVBoxLayout,
    QWidget)

from ui.implements.tabs.tabDb.tabDb_ChartInfoEditor import TabDb_ChartInfoEditor
from ui.implements.tabs.tabDb.tabDb_Manage import TabDb_Manage
from ui.implements.tabs.tabDb.tabDb_RemoveDuplicateScores import TabDb_RemoveDuplicateScores

class Ui_TabDbEntry(object):
    def setupUi(self, TabDbEntry):
        if not TabDbEntry.objectName():
            TabDbEntry.setObjectName(u"TabDbEntry")
        TabDbEntry.resize(648, 579)
        TabDbEntry.setWindowTitle(u"TabDbEntry")
        self.verticalLayout = QVBoxLayout(TabDbEntry)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(TabDbEntry)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_manage = TabDb_Manage()
        self.tab_manage.setObjectName(u"tab_manage")
        self.tabWidget.addTab(self.tab_manage, "")
        self.tab_chartInfoEditor = TabDb_ChartInfoEditor()
        self.tab_chartInfoEditor.setObjectName(u"tab_chartInfoEditor")
        self.tabWidget.addTab(self.tab_chartInfoEditor, "")
        self.tab_removeDuplicateScores = TabDb_RemoveDuplicateScores()
        self.tab_removeDuplicateScores.setObjectName(u"tab_removeDuplicateScores")
        self.tabWidget.addTab(self.tab_removeDuplicateScores, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(TabDbEntry)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TabDbEntry)
    # setupUi

    def retranslateUi(self, TabDbEntry):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_manage), QCoreApplication.translate("TabDbEntry", u"tab.manage", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_chartInfoEditor), QCoreApplication.translate("TabDbEntry", u"tab.chartInfoEditor", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_removeDuplicateScores), QCoreApplication.translate("TabDbEntry", u"tab.removeDuplicateScores", None))
        pass
    # retranslateUi

