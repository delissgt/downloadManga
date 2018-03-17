# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prodeliss.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_link = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_link.sizePolicy().hasHeightForWidth())
        self.label_link.setSizePolicy(sizePolicy)
        self.label_link.setMinimumSize(QtCore.QSize(100, 0))
        self.label_link.setAlignment(QtCore.Qt.AlignCenter)
        self.label_link.setObjectName(_fromUtf8("label_link"))
        self.horizontalLayout.addWidget(self.label_link)
        self.lineEdit_link = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_link.setObjectName(_fromUtf8("lineEdit_link"))
        self.horizontalLayout.addWidget(self.lineEdit_link)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_titulo = QtGui.QLabel(self.centralwidget)
        self.label_titulo.setStyleSheet(_fromUtf8("color: rgb(70, 144, 255);\n"
"font: 75 18pt \"Comfortaa\";"))
        self.label_titulo.setObjectName(_fromUtf8("label_titulo"))
        self.verticalLayout.addWidget(self.label_titulo)
        self.label_imagen = QtGui.QLabel(self.centralwidget)
        self.label_imagen.setObjectName(_fromUtf8("label_imagen"))
        self.verticalLayout.addWidget(self.label_imagen)
        self.label_capitulo = QtGui.QLabel(self.centralwidget)
        self.label_capitulo.setStyleSheet(_fromUtf8("color: rgb(5, 127, 5);\n"
"font: oblique 14pt \"Mingzat\";"))
        self.label_capitulo.setObjectName(_fromUtf8("label_capitulo"))
        self.verticalLayout.addWidget(self.label_capitulo)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.barraProgreso = QtGui.QProgressBar(self.centralwidget)
        self.barraProgreso.setProperty("value", 0)
        self.barraProgreso.setObjectName(_fromUtf8("barraProgreso"))
        self.verticalLayout_2.addWidget(self.barraProgreso)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushBoton_stop = QtGui.QPushButton(self.centralwidget)
        self.pushBoton_stop.setObjectName(_fromUtf8("pushBoton_stop"))
        self.horizontalLayout_2.addWidget(self.pushBoton_stop)
        self.pushBoton_start = QtGui.QPushButton(self.centralwidget)
        self.pushBoton_start.setObjectName(_fromUtf8("pushBoton_start"))
        self.horizontalLayout_2.addWidget(self.pushBoton_start)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_link.setBuddy(self.lineEdit_link)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_link.setText(_translate("MainWindow", "&Link", None))
        self.label_titulo.setText(_translate("MainWindow", "TextLabel", None))
        self.label_imagen.setText(_translate("MainWindow", "TextLabel", None))
        self.label_capitulo.setText(_translate("MainWindow", "TextLabel", None))
        self.pushBoton_stop.setText(_translate("MainWindow", "St&op", None))
        self.pushBoton_start.setText(_translate("MainWindow", "St&art", None))

