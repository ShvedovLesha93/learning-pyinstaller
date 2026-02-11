import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
)
from PySide6.QtCore import QTimer, Qt

import logging

logging.basicConfig(level=logging.DEBUG)

from app.translator import language_manager, _


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.lang_manager = language_manager
        self._languages = ["ru", "en"]
        self._current_lang = "en"
        self.lang_manager.set_language(self._current_lang)
        self._setup_ui()
        self.retranslate()

    def _setup_ui(self) -> None:
        self.setWindowTitle("Click Me Demo")
        self.setGeometry(100, 100, 300, 150)

        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Button
        self.button = QPushButton()
        self.button.clicked.connect(self.on_button_click)
        layout.addWidget(self.button)

        # Label
        self.label = QLabel("")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        # Timer for hiding the message
        self.timer = QTimer()
        self.timer.timeout.connect(self.clear_label)
        self.timer.setSingleShot(True)  # Fire only once

    def on_button_click(self) -> None:
        self.change_lang()
        self.retranslate()
        self.timer.start(3000)  # 3000 milliseconds = 3 seconds

    def change_lang(self) -> None:
        if self._current_lang == "en":
            self._current_lang = "ru"
            self.lang_manager.set_language("ru")
        else:
            self._current_lang = "en"
            self.lang_manager.set_language("en")

    def clear_label(self) -> None:
        self.label.setText("")

    def retranslate(self) -> None:
        self.label.setText(
            _("Language changed to: {lang}").format(lang=self._current_lang)
        )
        self.button.setText(_("Change language"))


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
