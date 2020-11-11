from PyQt5 import QtWidgets, QtCore, QtGui
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 545)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(130, 0, 551, 151))
        self.textEdit.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.textEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 400, 251, 101))
        self.pushButton.setMouseTracking(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_grn = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_grn.setGeometry(QtCore.QRect(-10, 150, 201, 61))
        self.pushButton_grn.setObjectName("pushButton_grn")
        self.pushButton_rd = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_rd.setGeometry(QtCore.QRect(190, 150, 201, 61))
        self.pushButton_rd.setObjectName("pushButton_rd")
        self.pushButton_blck = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_blck.setGeometry(QtCore.QRect(590, 150, 201, 61))
        self.pushButton_blck.setObjectName("pushButton_blck")
        self.pushButton_bl = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_bl.setGeometry(QtCore.QRect(390, 150, 201, 61))
        self.pushButton_bl.setObjectName("pushButton_bl")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 320, 101, 51))
        self.label.setObjectName("label")
        self.fontComboBox = QtWidgets.QFontComboBox(self.centralwidget)
        self.fontComboBox.setGeometry(QtCore.QRect(0, 230, 321, 81))
        self.fontComboBox.setObjectName("fontComboBox")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(320, 230, 151, 81))
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setRange(0 , 50)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.textEdit.clear)
        self.fontComboBox.currentFontChanged['QFont'].connect(self.textEdit.setCurrentFont)
        self.pushButton_grn.clicked.connect(self.green)
        self.pushButton_rd.clicked.connect(self.red)
        self.pushButton_bl.clicked.connect(self.blue)
        self.pushButton_blck.clicked.connect(self.black)
        self.spinBox.valueChanged.connect(self.changeFontSize)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Clear"))
        self.pushButton_grn.setText(_translate("MainWindow", "Green"))
        self.pushButton_rd.setText(_translate("MainWindow", "Red"))
        self.pushButton_blck.setText(_translate("MainWindow", "Black"))
        self.pushButton_bl.setText(_translate("MainWindow", "Blue"))
        self.textEdit.setText("Write something right here!")
        self.label.setText(_translate("MainWindow", "Font Size"))     

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
class mywindow(QtWidgets.QMainWindow):  
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  
 
app = QtWidgets.QApplication([])
application = mywindow()
app.setApplicationName("Simple Text Editor")
application.show()
 
sys.exit(app.exec())
