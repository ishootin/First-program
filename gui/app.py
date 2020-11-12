from PyQt5 import QtWidgets, QtCore, QtGui
import sys

from texteditor import Ui_MainWindow

class mywindow(QtWidgets.QMainWindow):  

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_grn.clicked.connect(self.green)
        self.ui.pushButton_rd.clicked.connect(self.red)
        self.ui.pushButton_bl.clicked.connect(self.blue)
        self.ui.pushButton_blck.clicked.connect(self.black)
        self.ui.spinBox.valueChanged.connect(self.changeFontSize)

    def green(self):
        self.ui.textEdit.setTextColor(QtGui.QColor('green'))
    def red(self):
        self.ui.textEdit.setTextColor(QtGui.QColor('red'))
    def blue(self):
        self.ui.textEdit.setTextColor(QtGui.QColor('blue'))
    def black(self):
        self.ui.textEdit.setTextColor(QtGui.QColor('black'))
    def changeFontSize(self):
        self.ui.value = self.ui.spinBox.value()
        self.ui.textEdit.setFontPointSize(self.ui.value)  

app = QtWidgets.QApplication([])
application = mywindow()
app.setApplicationName("Simple Text Editor")
application.show()
 
sys.exit(app.exec())
