import logging
import sys
import traceback

from arcaea_offline.database import Database
from PySide6.QtCore import QLibraryInfo, QLocale, QTranslator
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox

from ui.startup.databaseChecker import DatabaseChecker
from ui.implements.mainwindow import MainWindow
import ui.resources.images.images_rc
import ui.resources.translations.translations_rc

logging.basicConfig(level=logging.INFO, stream=sys.stdout, force=True)

if __name__ == "__main__":
    locale = QLocale.system()
    translator = QTranslator()
    translator_load_success = translator.load(QLocale.system(), "", "", ":/lang/")
    if not translator_load_success:
        translator.load(":/lang/en_US.qm")
    baseTranslator = QTranslator()
    baseTranslator.load(
        QLocale.system(),
        "qt",
        "_",
        QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath),
    )
    app = QApplication(sys.argv)

    app.installTranslator(translator)
    app.installTranslator(baseTranslator)

    databaseChecker = DatabaseChecker()
    result = databaseChecker.exec()

    if result == QDialog.DialogCode.Accepted:
        try:
            Database()
        except Exception as e:
            QMessageBox.critical(
                None, "Database Error", "\n".join(traceback.format_exception(e))
            )
            sys.exit(1)

        window = MainWindow()
        window.setWindowIcon(QIcon(":/images/icon.png"))
        window.show()
        sys.exit(app.exec())
    else:
        sys.exit(1)