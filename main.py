"""Main fucntion for Magic 8 ball"""
from PyQt5.QtWidgets import QApplication
from mods.gui import MainWindow
app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
