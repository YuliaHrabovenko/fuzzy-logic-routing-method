from PyQt5.QtWidgets import QDialog

from ui.Ui_VertexWeight import Ui_VertexWeight


class Weights_Dialog(QDialog):
    def __init__(self):
        super(Weights_Dialog, self).__init__()
        self.m_ui = Ui_VertexWeight()
        self.m_ui.setupUi(self)
        self.setWindowTitle("QSetWeightDialog")
