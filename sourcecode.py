from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def dis(self, i):
        self.oneone.setEnabled(i)
        self.onetwo.setEnabled(i)
        self.onethree.setEnabled(i)
        self.twoone.setEnabled(i)
        self.twotwo.setEnabled(i)
        self.twothree.setEnabled(i)
        self.threeone.setEnabled(i)
        self.threetwo.setEnabled(i)
        self.threethree.setEnabled(i)

    def check(self):
        _11 = self.oneone.text()
        _12 = self.onetwo.text()
        _13 = self.onethree.text()
        _21 = self.twoone.text()
        _22 = self.twotwo.text()
        _23 = self.twothree.text()
        _31 = self.threeone.text()
        _32 = self.threetwo.text()
        _33 = self.threethree.text()
        _all = _11 + _12 + _13 + _21 + _22 + _23 + _31 + _32 + _33

        if _11 + _12 + _13 == "XXX":
            self.label.setText("First player won...")
            self.dis(False)
        
        if _11 + _12 + _13 == "OOO":
            self.label.setText("Second player won...")
            self.dis(False)

        if _21 + _22 + _23 == "XXX":
            self.label.setText("First player won...")
            self.dis(False)
        
        if _21 + _22 + _23 == "OOO":
            self.label.setText("Second player won...")
            self.dis(False)

        if _31 + _32 + _33 == "XXX":
            self.label.setText("First player won...")
            self.dis(False)
        
        if _31 + _32 + _33 == "OOO":
            self.label.setText("Second player won...")
            self.dis(False)

        if _11 + _21 + _31 == "XXX":
            self.label.setText("First player won...")
            self.dis(False)
        
        if _11 + _21 + _31 == "OOO":
            self.label.setText("Second player won...")
            self.dis(False)

        if _12 + _22 + _32 == "XXX":
            self.label.setText("First player won...")
            self.dis(False)
        
        if _12 + _22 + _32 == "OOO":
            self.label.setText("Second player won...")
            self.dis(False)

        if _13 + _23 + _33 == "XXX":
            self.label.setText("First player won...")
            self.dis(False)
        
        if _13 + _23 + _33 == "OOO":
            self.label.setText("Second player won...")
            self.dis(False)

        if _11 + _22 + _33 == "XXX":
            self.label.setText("First player won...")
            self.dis(False)
        
        if _11 + _22 + _33 == "OOO":
            self.label.setText("Second player won...")
            self.dis(False)

        if _13 + _22 + _31 == "XXX":
            self.label.setText("First player won...")
            self.dis(False)
        
        if _13 + _22 + _31 == "OOO":
            self.label.setText("Second player won...")
            self.dis(False)

            
        if '-' not in _all:
            self.dis(False)
            self.label.setText("No one won...")

    def tick(self, r):
        ch = ''
        if self.turn == "fp":
            ch = 'X'
            self.label.setText("Second player's turn")
            self.turn = "sp"
        elif self.turn == "sp":
            ch = 'O'
            self.label.setText("First player's turn")
            self.turn = "fp"

        if r == "11":
            self.oneone.setText(ch)
        elif r == "12":
            self.onetwo.setText(ch)
        elif r == "13":
            self.onethree.setText(ch)
        elif r == "21":
            self.twoone.setText(ch)
        elif r == "22":
            self.twotwo.setText(ch)
        elif r == "23":
            self.twothree.setText(ch)
        elif r == "31":
            self.threeone.setText(ch)
        elif r == "32":
            self.threetwo.setText(ch)
        elif r == "33":
            self.threethree.setText(ch)

        self.check()
            
    
    def restart(self):
        self.oneone.setText('-')
        self.onetwo.setText('-')
        self.onethree.setText('-')
        self.twoone.setText('-')
        self.twotwo.setText('-')
        self.twothree.setText('-')
        self.threeone.setText('-')
        self.threetwo.setText('-')
        self.threethree.setText('-')
        self.label.setText("First player's turn")
        self.dis(True)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(711, 563)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(711, 563))
        MainWindow.setMaximumSize(QtCore.QSize(711, 563))
        self.turn = "fp"
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fpl = QtWidgets.QLabel(self.centralwidget)
        self.fpl.setGeometry(QtCore.QRect(20, 20, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.fpl.setFont(font)
        self.fpl.setObjectName("fpl")
        self.spl = QtWidgets.QLabel(self.centralwidget)
        self.spl.setGeometry(QtCore.QRect(380, 20, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.spl.setFont(font)
        self.spl.setObjectName("spl")
        self.vsl = QtWidgets.QLabel(self.centralwidget)
        self.vsl.setGeometry(QtCore.QRect(310, 40, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.vsl.setFont(font)
        self.vsl.setObjectName("vsl")
        self.oneone = QtWidgets.QPushButton(self.centralwidget)
        self.oneone.setGeometry(QtCore.QRect(20, 170, 121, 111))
        font = QtGui.QFont()
        font.setPointSize(33)
        self.oneone.setFont(font)
        self.oneone.setObjectName("oneone")
        self.onetwo = QtWidgets.QPushButton(self.centralwidget)
        self.onetwo.setGeometry(QtCore.QRect(160, 170, 121, 111))
        font = QtGui.QFont()
        font.setPointSize(33)
        self.onetwo.setFont(font)
        self.onetwo.setObjectName("onetwo")
        self.onethree = QtWidgets.QPushButton(self.centralwidget)
        self.onethree.setGeometry(QtCore.QRect(300, 170, 121, 111))
        font = QtGui.QFont()
        font.setPointSize(33)
        self.onethree.setFont(font)
        self.onethree.setObjectName("onethree")
        self.twothree = QtWidgets.QPushButton(self.centralwidget)
        self.twothree.setGeometry(QtCore.QRect(300, 300, 121, 111))
        font = QtGui.QFont()
        font.setPointSize(33)
        self.twothree.setFont(font)
        self.twothree.setObjectName("twothree")
        self.twotwo = QtWidgets.QPushButton(self.centralwidget)
        self.twotwo.setGeometry(QtCore.QRect(160, 300, 121, 111))
        font = QtGui.QFont()
        font.setPointSize(33)
        self.twotwo.setFont(font)
        self.twotwo.setObjectName("twotwo")
        self.twoone = QtWidgets.QPushButton(self.centralwidget)
        self.twoone.setGeometry(QtCore.QRect(20, 300, 121, 111))
        font = QtGui.QFont()
        font.setPointSize(33)
        self.twoone.setFont(font)
        self.twoone.setObjectName("twoone")
        self.threeone = QtWidgets.QPushButton(self.centralwidget)
        self.threeone.setGeometry(QtCore.QRect(20, 430, 121, 111))
        font = QtGui.QFont()
        font.setPointSize(33)
        self.threeone.setFont(font)
        self.threeone.setObjectName("threeone")
        self.threetwo = QtWidgets.QPushButton(self.centralwidget)
        self.threetwo.setGeometry(QtCore.QRect(160, 430, 121, 111))
        font = QtGui.QFont()
        font.setPointSize(33)
        self.threetwo.setFont(font)
        self.threetwo.setObjectName("threetwo")
        self.threethree = QtWidgets.QPushButton(self.centralwidget)
        self.threethree.setGeometry(QtCore.QRect(300, 430, 121, 111))
        font = QtGui.QFont()
        font.setPointSize(33)
        self.threethree.setFont(font)
        self.threethree.setObjectName("threethree")
        self.rb = QtWidgets.QPushButton(self.centralwidget)
        self.rb.setGeometry(QtCore.QRect(550, 190, 89, 25))
        self.rb.setObjectName("rb")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(510, 230, 150, 17))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.oneone.clicked.connect(lambda:self.tick("11"))
        self.onetwo.clicked.connect(lambda:self.tick("12"))
        self.onethree.clicked.connect(lambda:self.tick("13"))
        self.twoone.clicked.connect(lambda:self.tick("21"))
        self.twotwo.clicked.connect(lambda:self.tick("22"))
        self.twothree.clicked.connect(lambda:self.tick("23"))
        self.threeone.clicked.connect(lambda:self.tick("31"))
        self.threetwo.clicked.connect(lambda:self.tick("32"))
        self.threethree.clicked.connect(lambda:self.tick("33"))
        self.rb.clicked.connect(self.restart)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tic Tac Toe"))
        self.fpl.setText(_translate("MainWindow", "First Player : X"))
        self.spl.setText(_translate("MainWindow", "Second Player : O"))
        self.vsl.setText(_translate("MainWindow", "VS"))
        self.oneone.setText(_translate("MainWindow", "-"))
        self.onetwo.setText(_translate("MainWindow", "-"))
        self.onethree.setText(_translate("MainWindow", "-"))
        self.twothree.setText(_translate("MainWindow", "-"))
        self.twotwo.setText(_translate("MainWindow", "-"))
        self.twoone.setText(_translate("MainWindow", "-"))
        self.threeone.setText(_translate("MainWindow", "-"))
        self.threetwo.setText(_translate("MainWindow", "-"))
        self.threethree.setText(_translate("MainWindow", "-"))
        self.rb.setText(_translate("MainWindow", "RESTART"))
        self.label.setText(_translate("MainWindow", "First player's turn"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
