import sys, os
from PySide6.QtWidgets import QMainWindow
from ui.NandemoEmail_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, data_address):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        print(data_address)