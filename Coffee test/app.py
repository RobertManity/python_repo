from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button = QPushButton("Click me!", self)
        self.button.clicked.connect(self.button_clicked)
        self.button.move(100, 100)

        self.label = QLabel(self)
        self.label.move(100, 150)

        self.label2 = QLabel(self)
        self.label2.move(100, 200)

        self.resize(400,400)

    def button_clicked(self):
        self.label.setText('Hello')
        self.label.adjustSize()  # adjust label size to fit the new text

        self.label2.setText('Hello2')
        self.label2.adjustSize()  # adjust label size to fit the new text

def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

if __name__ == "__main__":
    main()

    # vrste varijabli: intiger, float, dictionary, boolean, string, list, aray.