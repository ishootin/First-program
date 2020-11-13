from PyQt5 import QtWidgets, QtCore, QtGui
import sys

from texteditor import Ui_MainWindow

class mywindow(Ui_MainWindow, QtWidgets.QMainWindow):  

    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.pushButton_grn.clicked.connect(self.green)
        self.pushButton_rd.clicked.connect(self.red)
        self.pushButton_bl.clicked.connect(self.blue)
        self.pushButton_blck.clicked.connect(self.black)
        self.spinBox.valueChanged.connect(self.changeFontSize)

    def green(self):
        self.textEdit.setTextColor(QtGui.QColor('green'))
    def red(self):
        self.textEdit.setTextColor(QtGui.QColor('red'))
    def blue(self):
        self.textEdit.setTextColor(QtGui.QColor('blue'))
    def black(self):
        self.textEdit.setTextColor(QtGui.QColor('black'))
    def changeFontSize(self):
        self.value = self.spinBox.value()
        self.textEdit.setFontPointSize(self.value)  

app = QtWidgets.QApplication([])
application = mywindow()
app.setApplicationName("Simple Text Editor")
application.show()
 
sys.exit(app.exec())
