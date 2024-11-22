from PyQt5 import QtCore, QtWidgets

class Ui_VertexWeight(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(247, 221)
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
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.submit_button = QtWidgets.QPushButton(Dialog)
        self.submit_button.setMinimumSize(QtCore.QSize(0, 35))
        self.submit_button.setStyleSheet("font-size: 13pt;\n"
                                         "background-color: rgb(176, 196, 222);")
        self.submit_button.setObjectName("submit_button")
        self.gridLayout.addWidget(self.submit_button, 6, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(0, 35))
        self.label.setStyleSheet("font-size:13pt;")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.energy_input = QtWidgets.QLineEdit(Dialog)
        self.energy_input.setMinimumSize(QtCore.QSize(0, 35))
        self.energy_input.setStyleSheet("font-size:13pt;")
        self.energy_input.setObjectName("energy_input")
        self.gridLayout.addWidget(self.energy_input, 5, 0, 1, 1)
        self.speed_input = QtWidgets.QLineEdit(Dialog)
        self.speed_input.setMinimumSize(QtCore.QSize(0, 35))
        self.speed_input.setStyleSheet("font-size:13pt;")
        self.speed_input.setObjectName("speed_input")
        self.gridLayout.addWidget(self.speed_input, 3, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Residual energy:0-100(%)"))
        self.submit_button.setText(_translate("Dialog", "Submit"))
        self.label.setText(_translate("Dialog", "Speed:0-12(m/s)"))