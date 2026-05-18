import sys
from PySide6 import QtWidgets, QtCore

class ColorSwatch(QtWidgets.QPushButton):
    def __init__(self, color_hex, parent=None):
        super().__init__(parent)
        self.color_hex = color_hex
        self.setFixedSize(24, 24)
        self.setCursor(QtCore.Qt.PointingHandCursor)
        self.setStyleSheet(f"background-color: {color_hex}; border: 1px solid #ddd; border-radius: 12px;")
        self.clicked.connect(self.print_my_color)

    def print_my_color(self):
        print(f"Kliknuto na barvu: {self.color_hex}")

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Titulek okna")
        self.resize(500, 400)

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QtWidgets.QVBoxLayout(central_widget)
        #štítky
        label = QtWidgets.QLabel("Nějaký text na desce.")
        label.setAlignment(QtCore.Qt.AlignCenter)

        main_layout.addWidget(label)
        button = QtWidgets.QPushButton("Klikni na tlačítko")

        red_swatch = ColorSwatch("ff0000")
        main_layout.addWidget(red_swatch, alignment=QtCore.Qt.AlignCenter)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())