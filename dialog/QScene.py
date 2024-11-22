from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsScene

class QScene(QGraphicsScene):

    def __init__(self, parent=None):
        QGraphicsScene.__init__(self, parent)
        self.node_number = 1
        self.vertex_list = []
        self.dict_nodes_weights = {}
        self.list_edges_position = []
        self.list_result_nodes_edges = []
        self.setBackgroundBrush(QColor(224, 225, 226))
