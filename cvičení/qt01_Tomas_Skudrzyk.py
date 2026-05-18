import sys
from PySide6 import QtWidgets,QtCore

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplikace QT")
        self.resize(500, 500)

        self.central_widget = QtWidgets.QWidget() # vložení prázdné desky do okna QMainWindow (nejde vkládat přímo do okna)
        self.setCentralWidget(self.central_widget)

        main_layout = QtWidgets.QVBoxLayout(self.central_widget) # umístění na desku
        
        label = QtWidgets.QLabel("Ahoj tady je nejaky text")
        label.setAlignment(QtCore.Qt.AlignCenter) # Zarovnání textu
        main_layout.addWidget(label)        

        button = QtWidgets.QPushButton("Klikni na me!")
        button.clicked.connect(self.on_button_clicked)
        main_layout.addWidget(button)


    def on_button_clicked(self):
        print("Kliknuto! ")

        # změna barvy pozadí po kliknutí na tlačítko
        self.central_widget.setStyleSheet("background-color: lightblue;")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window. show()
    sys.exit(app.exec())

