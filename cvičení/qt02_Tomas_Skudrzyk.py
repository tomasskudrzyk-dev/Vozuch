import sys
from PySide6 import QtWidgets,QtCore

class btnColorSwatch(QtWidgets.QPushButton):
    def __init__(self, color_hex, parent=None):
        super().__init__(parent)
        self.color_hex = color_hex
        self.setFixedSize(24,24)
        self.setCursor(QtCore.Qt.PointingHandCursor)
                
        self.setStyleSheet(f"background-color: {color_hex}; border: 1px solid #ddd; border-radius: 12px;")
        self.clicked.connect(self.print_my_color)
    
    def print_my_color(self):
        print(f"Byl stiskut vzornik barvy: {self.color_hex}")


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.setWindowTitle("Aplikace QT")
        self.resize(500, 500)

        self.central_widget = QtWidgets.QWidget() # vložení prázdné desky do okna QMainWindow (nejde vkládat přímo do okna)

        self.setCentralWidget(self.central_widget)

        # Vytvoření "Rozložení" (Layoutu). Bez něj by se tlačítka házela jedno přes druhé.
        main_layout = QtWidgets.QVBoxLayout(self.central_widget) # umístění na desku
        
        label = QtWidgets.QLabel("Klikni na barvu")
        label.setAlignment(QtCore.Qt.AlignCenter) # Zarovnání textu
        main_layout.addWidget(label)        

        red_swatch = btnColorSwatch("#ff0000")
        red_swatch.clicked.connect(lambda: self.change_background(red_swatch.color_hex))
        main_layout.addWidget(red_swatch, alignment=QtCore.Qt.AlignCenter)    

    def change_background(self, color_hex):
        self.central_widget.setStyleSheet(f"background-color: {color_hex};")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window. show()
    sys.exit(app.exec())
