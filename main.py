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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Click Me Demo")
        self.setGeometry(100, 100, 300, 150)

        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Button
        self.button = QPushButton("Click Me")
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

    def on_button_click(self):
        self.label.setText("clicked")
        self.timer.start(3000)  # 3000 milliseconds = 3 seconds

    def clear_label(self):
        self.label.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
