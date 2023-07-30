# pokrenuti skriptu sa pytest app_test.py
import pytest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt

# Assume that your main window class is in a module called main_window
from app import MainWindow

# Initialize application 
app = QApplication([])

def test_button_click_updates_label(qtbot):
    # Arrange 
    window = MainWindow()
    window.show()
    qtbot.addWidget(window)

    # Act
    qtbot.mouseClick(window.button, Qt.LeftButton)
    print('check')
    # Assert
    assert window.label.text() == "Hello"
    assert window.label2.text() == "Hello2"

    print('success')