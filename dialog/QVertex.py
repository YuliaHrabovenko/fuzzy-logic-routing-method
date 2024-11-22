from PyQt5.QtCore import QRectF, Qt
from PyQt5.QtGui import QPen, QColor, QBrush
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsEllipseItem

class QVertex(QGraphicsEllipseItem):
    def __init__(self, rect=QRectF(-75, -15, 70, 70), parent=None):

        QGraphicsEllipseItem.__init__(self, rect, parent)
        self.id = None
        self.vertex_edges_list = []
        self.setZValue(1)
        self.setPen(QPen(Qt.black, 2.4))
        self.color = Qt.white
        self.setBrush(self.color)
        self.setFlags(QGraphicsItem.ItemIsMovable |
                      QGraphicsItem.ItemIsSelectable |
                      QGraphicsItem.ItemSendsGeometryChanges)

    def attachEdge(self, edge):
        self.vertex_edges_list.append(edge)

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemSelectedChange:
            self.setBrush(QColor(144, 238, 144) if value else self.color)

        if change == QGraphicsItem.ItemPositionHasChanged:
            for edge in self.vertex_edges_list:
                edge.adjustPosition()

        return QGraphicsItem.itemChange(self, change, value)
