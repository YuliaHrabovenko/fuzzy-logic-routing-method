from PyQt5.QtWidgets import QDialog

from ui.Ui_SourceEnd import Ui_SourceEnd


class Start_End_Dialog(QDialog):
    def __init__(self):
        super(Start_End_Dialog, self).__init__()
        self.m_ui = Ui_SourceEnd()
        self.m_ui.setupUi(self)
        self.setWindowTitle("QSetSourceEndDialog")
