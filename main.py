import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from dialog.QMain import QMain

if __name__ == '__main__':
    my_app = QApplication(sys.argv)
    my_app.setApplicationName("Network Project")
    main_window = QMain()
    wid_get = QtWidgets.QStackedWidget()
    wid_get.addWidget(main_window)
    wid_get.show()
    my_app.exec_()
