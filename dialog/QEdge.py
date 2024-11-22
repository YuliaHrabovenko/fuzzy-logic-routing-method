from PyQt5.QtCore import QLineF, Qt
from PyQt5.QtGui import QPen
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsLineItem

class QEdge(QGraphicsLineItem):
    def __init__(self, source, dest, parent=None, label=None):
        QGraphicsLineItem.__init__(self, parent)
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.start_vertex = source
        self.end_vertex = dest
        self.start_vertex.attachEdge(self)
        self.end_vertex.attachEdge(self)
        self.setPen(QPen(Qt.black, 2.4))
        self.adjustPosition()

    def adjustPosition(self):
        self.prepareGeometryChange()
        x_offset_dest = self.end_vertex.rect().x() + self.end_vertex.rect().width() / 2
        y_offset_dest = self.end_vertex.rect().y() + self.end_vertex.rect().height() / 2

        x_offset_source = self.start_vertex.rect().x() + self.start_vertex.rect().width() / 2
        y_offset_source = self.start_vertex.rect().y() + self.start_vertex.rect().height() / 2

        self.setLine(QLineF(self.end_vertex.pos().x() + x_offset_dest, self.end_vertex.pos().y() + y_offset_dest,
                            self.start_vertex.x() + x_offset_source, self.start_vertex.pos().y() + y_offset_source))
