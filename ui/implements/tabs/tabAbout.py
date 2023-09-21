from PySide6.QtCore import QFile, Qt, Slot
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMessageBox, QWidget

from ui.designer.tabs.tabAbout_ui import Ui_TabAbout


class TabAbout(Ui_TabAbout, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        logoPixmap = QPixmap(":/images/logo.png").scaled(
            300,
            300,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        self.logoLabel.setPixmap(logoPixmap)

    @Slot()
    def on_aboutQtButton_clicked(self):
        QMessageBox.aboutQt(self)

    @Slot()
    def on_versionInfoButton_clicked(self):
        versionFile = QFile(":/VERSION")
        versionFile.open(QFile.OpenModeFlag.ReadOnly)
        versionText = str(versionFile.readAll(), encoding="utf-8")
        versionFile.close()
        QMessageBox.information(self, None, versionText)
