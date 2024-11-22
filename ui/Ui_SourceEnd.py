from PyQt5 import QtCore, QtWidgets

class Ui_SourceEnd(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(245, 222)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(6, 3, 6, -1)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setMinimumSize(QtCore.QSize(0, 35))
        self.label_2.setStyleSheet("font-size:13pt;")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.source_inp = QtWidgets.QLineEdit(Dialog)
        self.source_inp.setMinimumSize(QtCore.QSize(0, 35))
        self.source_inp.setStyleSheet("font-size:13pt;")
        self.source_inp.setObjectName("source_inp")
        self.gridLayout.addWidget(self.source_inp, 2, 0, 1, 1)
        self.sub_but = QtWidgets.QPushButton(Dialog)
        self.sub_but.setMinimumSize(QtCore.QSize(0, 35))
        self.sub_but.setStyleSheet("font-size: 13pt;\n"
                                   "background-color: rgb(176, 196, 222);")
        self.sub_but.setObjectName("sub_but")
        self.gridLayout.addWidget(self.sub_but, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(0, 35))
        self.label.setStyleSheet("font-size:13pt;")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.end_inp = QtWidgets.QLineEdit(Dialog)
        self.end_inp.setMinimumSize(QtCore.QSize(0, 35))
        self.end_inp.setStyleSheet("font-size:13pt;")
        self.end_inp.setObjectName("end_inp")
        self.gridLayout.addWidget(self.end_inp, 4, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Input end node"))
        self.sub_but.setText(_translate("Dialog", "Submit"))
        self.label.setText(_translate("Dialog", "Input source node"))
