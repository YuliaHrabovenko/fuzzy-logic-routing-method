import math
import os
import random
import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPen, QFont, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, \
    QFileDialog

from algo.BFS import BFS
from algo.FIS import FIS
from algo.MultiPathAlgorithm import MultiPathAlgorithm
from dialog.QEdge import QEdge
from dialog.QScene import QScene
from dialog.QVertex import QVertex
from dialog.Start_End_Dialog import Start_End_Dialog
from dialog.Weights_Dialog import Weights_Dialog
from graph_elements.Graph import Graph
from graph_elements.Node import Node
from ui.Ui_MainWindow import Ui_MainWindow


class QMain(QMainWindow):
    def __init__(self):
        super(QMain, self).__init__()
        self.m_ui = Ui_MainWindow()
        self.m_ui.setupUi(self)
        self.start_end_dialog = Start_End_Dialog()
        self.scene_window = QScene()
        self.weights_dialog = Weights_Dialog()
        self.m_ui.graphicsView.setScene(self.scene_window)
        self.start_end_dialog.m_ui.sub_but.clicked.connect(self.set_source_finish_nodes)
        self.weights_dialog.m_ui.submit_button.clicked.connect(self.save_nodes_weights_in_list)
        self.m_ui.actionAdd_Node.triggered.connect(self.draw_node)
        self.m_ui.actionAdd_Edge.triggered.connect(self.draw_edge)
        self.m_ui.actionAdd_Weight.triggered.connect(self.set_weights)  # new
        self.m_ui.actionDelete_Node.triggered.connect(self.clear_node)
        self.m_ui.actionDelete_Edge.triggered.connect(self.clear_edge)
        self.m_ui.actionClear_All.triggered.connect(self.blank_scene)
        self.m_ui.actionSave.triggered.connect(self.save_in_file)
        self.m_ui.actionOpen.triggered.connect(self.open_from_file)
        self.m_ui.actionNew.triggered.connect(self.open_new_window)
        self.m_ui.actionExit.triggered.connect(self.quit_window)
        self.m_ui.actionInput_source_and_end.triggered.connect(self.input_source_finish)
        self.m_ui.actionMake_Full_Modeling.triggered.connect(self.output_result_paths)
        self.m_ui.actionSave.setShortcut("Ctrl+S")
        self.m_ui.actionAdd_Node.setShortcut("Ctrl+N")
        self.m_ui.actionAdd_Edge.setShortcut("Ctrl+E")
        self.m_ui.actionAdd_Weight.setShortcut("Ctrl+W")
        self.m_ui.actionDelete_Node.setShortcut("Ctrl+R")
        self.m_ui.actionDelete_Edge.setShortcut("Ctrl+D")
        self.m_ui.actionClear_All.setShortcut("Ctrl+C")
        self.m_ui.actionOpen.setShortcut("Ctrl+O")
        self.m_ui.actionNew.setShortcut("Ctrl+V")
        self.m_ui.actionExit.setShortcut("Ctrl+X")
        self.m_ui.actionInput_source_and_end.setShortcut("Ctrl+P")
        self.m_ui.actionMake_Full_Modeling.setShortcut("Ctrl+M")
        self.source_node = None
        self.finish_node = None

    def save_nodes_weights_in_list(self):

        n1 = self.scene_window.selectedItems()[0].id
        w1 = self.weights_dialog.m_ui.speed_input.text()
        w2 = self.weights_dialog.m_ui.energy_input.text()

        self.scene_window.dict_nodes_weights[n1] = [float(w1), float(w2)]
        w1 = self.weights_dialog.m_ui.speed_input.setText("")
        w2 = self.weights_dialog.m_ui.energy_input.setText("")
        self.weights_dialog.close()

    def save_edges_pos_in_list(self):

        n1 = self.scene_window.selectedItems()[0].id
        n2 = self.scene_window.selectedItems()[1].id
        n1_x = self.scene_window.selectedItems()[0].x()
        n1_y = self.scene_window.selectedItems()[0].y()
        n2_x = self.scene_window.selectedItems()[1].x()
        n2_y = self.scene_window.selectedItems()[1].y()
        dist = round(math.sqrt(math.pow((n2_x - n1_x), 2) + math.pow((n2_y - n1_y), 2)), 2)
        # print("saved_edges = ", [n1, n2, n1_x, n1_y, n2_x, n2_y])

        self.scene_window.list_edges_position.append([n1, n2, n1_x, n1_y, n2_x, n2_y, dist])

    def draw_node(self):
        q_vertex = QVertex()
        q_vertex.id = self.scene_window.node_number
        self.scene_window.vertex_list.append(q_vertex.id)
        node_label = QtWidgets.QLabel()
        node_label.setText('S' + str(self.scene_window.node_number))
        node_label.move(q_vertex.pos().x() + q_vertex.rect().x() + q_vertex.rect().width() / 2 - 25,
                        q_vertex.pos().y() + q_vertex.rect().y() + q_vertex.rect().height() / 2 - 18)
        node_label.setStyleSheet('background-color: transparent')
        node_label.setFont(QFont('Arial', 19))

        prox = QtWidgets.QGraphicsProxyWidget(q_vertex)
        prox.setWidget(node_label)
        self.scene_window.node_number += 1
        self.scene_window.addItem(q_vertex)
        # self.weights_dialog.exec_()

    def draw_edge(self):
        if len(self.scene_window.selectedItems()) == 2:
            new_edge = QEdge(self.scene_window.selectedItems()[0], self.scene_window.selectedItems()[1])
            self.scene_window.addItem(new_edge)
            self.save_edges_pos_in_list()

    def set_weights(self):
        if len(self.scene_window.selectedItems()) == 1:
            self.weights_dialog.exec_()

    def clear_node(self):
        if len(self.scene_window.selectedItems()) == 1:
            if type(self.scene_window.selectedItems()[0]) == QVertex:
                vertex_to_delete = self.scene_window.selectedItems()[0].id
                self.scene_window.vertex_list.remove(vertex_to_delete)
                if vertex_to_delete in self.scene_window.dict_nodes_weights:
                    del self.scene_window.dict_nodes_weights[vertex_to_delete]
                for elem in self.scene_window.items():
                    if type(elem) == QEdge:
                        if elem.start_vertex.id == vertex_to_delete:
                            for _list in self.scene_window.list_edges_position:
                                if elem.start_vertex.id in _list and elem.end_vertex.id in _list:
                                    self.scene_window.list_edges_position.remove(_list)
                            self.scene_window.removeItem(elem)
                        elif elem.end_vertex.id == vertex_to_delete:
                            for _list in self.scene_window.list_edges_position:
                                if elem.start_vertex.id in _list and elem.end_vertex.id in _list:
                                    self.scene_window.list_edges_position.remove(_list)
                            self.scene_window.removeItem(elem)
                self.scene_window.removeItem(self.scene_window.selectedItems()[0])

    def clear_edge(self):
        if len(self.scene_window.selectedItems()) == 1:
            if type(self.scene_window.selectedItems()[0]) == QEdge:
                for edge_list in self.scene_window.list_edges_position:
                    if self.scene_window.selectedItems()[0].start_vertex.id in edge_list and \
                            self.scene_window.selectedItems()[0].end_vertex.id in edge_list:
                        self.scene_window.list_edges_position.remove(edge_list)
                self.scene_window.removeItem(self.scene_window.selectedItems()[0])

    def blank_scene(self):
        self.scene_window.dict_nodes_weights = {}
        self.scene_window.list_edges_position = []
        self.scene_window.vertex_list = []
        self.scene_window.clear()
        self.scene_window.node_number = 1

    def save_in_file(self):
        file_options = QFileDialog.Options()
        file_options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getSaveFileName(self, "QSaveFileDialog", "",
                                                   "All Files (*);;Text Files (*.txt)", options=file_options)
        if file_path == "":
            return

        if os.path.exists(file_path):
            os.remove(file_path)

        nw_dict = self.scene_window.dict_nodes_weights
        res_list = self.scene_window.list_result_nodes_edges

        for n1, n2, n1_x, n1_y, n2_x, n2_y, dist in self.scene_window.list_edges_position:
            new = [n1, n2, n1_x, n1_y, n2_x, n2_y, nw_dict[n1][0], nw_dict[n1][1], nw_dict[n2][0], nw_dict[n2][1], dist]
            res_list.append(new)

        for n1, n2, n1_x, n1_y, n2_x, n2_y, w1_1, w1_2, w2_1, w2_2, dist in res_list:
            with open(file_path, 'a') as file:
                file.write(str(n1) + ',' + str(n2) + ',' + str(n1_x) + ',' + str(n1_y) + ',' + str(n2_x) + ','
                           + str(n2_y) + ',' + str(w1_1) + ',' + str(w1_2) + ',' + str(w2_1) + ','
                           + str(w2_2) + ',' + str(dist) + '\n')
        file.close()

    def open_from_file(self):
        file_options = QFileDialog.Options()
        file_options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getOpenFileName(self, "QOpenFileDialog", "",
                                                   "All Files (*);;Python Files (*.py)", options=file_options)
        if file_path == "":
            return

        with open(file_path) as f:
            lines = f.readlines()
            for line in lines:
                n1, n2, n1_x, n1_y, n2_x, n2_y, w1_1, w1_2, w2_1, w2_2, dist = (line.strip().split(','))
                n_l = [(n1, n1_x, n1_y), (n2, n2_x, n2_y)]
                for n_i in n_l:
                    if int(n_i[0]) not in self.scene_window.vertex_list:
                        # print(int(s_i))
                        vert = QVertex()
                        vert.id = int(n_i[0])
                        self.scene_window.vertex_list.append(vert.id)
                        # print(self.vertex_list)
                        node_label = QtWidgets.QLabel()
                        node_label.setText('S' + n_i[0])
                        node_label.move(vert.pos().x() + vert.rect().x() + vert.rect().width() / 2 - 25,
                                        vert.pos().y() + vert.rect().y() + vert.rect().height() / 2 - 18)
                        node_label.setStyleSheet('background-color: transparent')
                        node_label.setFont(QFont('Arial', 18))
                        proxy = QtWidgets.QGraphicsProxyWidget(vert)
                        proxy.setWidget(node_label)
                        self.scene_window.node_number += 1
                        point = QPoint(float(n_i[1]), float(n_i[2]))
                        point_item = vert.mapFromScene(point)
                        vert.setPos(point_item)
                        self.scene_window.addItem(vert)
                vert1 = None
                vert2 = None
                scene_elems = self.scene_window.items()
                # print(scene_items)
                for elem in scene_elems:
                    if type(elem) == QVertex:
                        if elem.id == int(n1):
                            vert1 = elem
                        elif elem.id == int(n2):
                            vert2 = elem
                new_edge = QEdge(vert1, vert2)
                # print(self.selectedItems()[0], self.selectedItems()[1])
                self.scene_window.addItem(new_edge)
                self.scene_window.list_edges_position.append(
                    [int(n1), int(n2), float(n1_x), float(n1_y), float(n2_x), float(n2_y), float(dist)])
                self.scene_window.dict_nodes_weights[int(n1)] = [float(w1_1), float(w1_2)]
                self.scene_window.dict_nodes_weights[int(n2)] = [float(w2_1), float(w2_2)]

    def open_new_window(self):

        self.my_app = QApplication(sys.argv)
        self.my_app.setApplicationName("Network Project")
        self.main_win = QMain()
        self.my_widget = QtWidgets.QStackedWidget()
        self.my_widget.addWidget(self.main_win)
        self.my_widget.show()
        self.my_app.exec_()

    def quit_window(self):
        sys.exit(self.close())

    def set_source_finish_nodes(self):
        # global s, d
        self.source_node = int(self.start_end_dialog.m_ui.source_inp.text())
        self.finish_node = int(self.start_end_dialog.m_ui.end_inp.text())
        # print(self.source_node, self.finish_node)
        self.start_end_dialog.close()

    def input_source_finish(self):
        self.start_end_dialog.exec_()

    def output_result_paths(self):
        # global nodes_number
        if self.source_node is None and self.finish_node is None:
            self.m_ui.disjoint_paths_field.setText("No start node and end node were entered!!!")
            return

        start_node = self.source_node
        end_node = self.finish_node
        graph = Graph()

        for number, weights in self.scene_window.dict_nodes_weights.items():
            graph.append_new_node(number, weights[0], weights[1])

        for _list in self.scene_window.list_edges_position:
            # print(_list[6])
            graph.append_new_edge(_list[0], _list[1], _list[6])

        global start, end
        if end_node in self.scene_window.vertex_list:
            end = graph.get_node_by_id(end_node)
        else:
            self.m_ui.disjoint_paths_field.setText("End node is not in graph!!!")
            return

        if start_node in self.scene_window.vertex_list:
            start = graph.get_node_by_id(start_node)
        else:
            self.m_ui.disjoint_paths_field.setText("Start node is not in graph!!!")
            return

        str_alg = MultiPathAlgorithm(graph, start, end)

        str_alg.select_disjoint_paths()

        paths_params = str_alg.disjoint_paths_metrics  # list of tuples of paths and their params

        edges = []
        for path, params in paths_params:
            path_edges = [[i, j] for i, j in zip(path, path[1::])]
            for edge in path_edges:
                edges.append(edge)

        scen_items = self.scene_window.items()
        i = 0
        colors = [QColor(177, 255, 99), QColor(255, 255, 80), QColor(255, 192, 203), QColor(235, 181, 235),
                  QColor(255, 210, 0)]

        random.shuffle(colors)
        used_col = []

        for item in scen_items:
            if type(item) == QEdge:
                for e in edges:
                    if item.start_vertex.id in e and item.end_vertex.id in e:
                        item.setPen(QPen(Qt.black, 4.1))

        paths_and_stability = {}
        op_path = []
        op_rtng = 0
        for path, params in str_alg.disjoint_paths_metrics:
            # print('t =', params[0], 'l =', params[1])
            fl = FIS(params[1], params[0], params[2])
            # fl.time, fl.load_coef = params[0], params[1]
            fl.fuzzy_controler()
            paths_and_stability[str(path)] = fl.stability
            if fl.stability > op_rtng:
                op_rtng = fl.stability
                op_path = path
        # print(paths_and_stability)
        text_paths = 'Found Disjoint Paths'.center(52, ' ') + '-' * 55 + '\n'
        i = 0

        for path, params in paths_params:
            speed, energy, hops, dist, energy_cons, lifetime = params
            # print(t, l)
            i += 1
            n = '-' * 55
            R_in_paths = ['S' + str(i) + '->' for i in path]
            p = ''.join(str(r) for r in R_in_paths)

            f = f'Path_{i} :\n  {p[:-2]}\n\nStability_{i} = {round(paths_and_stability[str(path)], 2)}%\nAverage_Residual_Energy_{i} = {energy}%\nAverage_Speed_{i} = {speed}m/s\nHops_{i} = {hops}\nTotal_Distance_{i} = {dist}m\nEnergy_Consumed{i} = {energy_cons}%\nLifetime_{i} = {lifetime}s\n\n'
            text_paths += f

        best_path = ['S' + str(i) + '->' for i in op_path]
        str_best_path = ''.join(str(r) for r in best_path)

        #### add bfs beneath ####
        text_paths += '-' * 55 + 'Result path:\n  ' + str_best_path[:-2]

        text_paths += '\n'+'-' * 55

        bfs = BFS(graph, start, end)
        bfs.shortest_path()

        fl2 = FIS(bfs.total_energy, bfs.avg_speed, bfs.hop_count)
        fl2.fuzzy_controler()

        shortest_path = ['S' + str(i) + '->' for i in bfs.path]
        str_shortest_path = ''.join(str(r) for r in shortest_path)
        new_text = f'\n\nPath_bfs :\n  {str_shortest_path[:-2]}\n\nStability = {round(fl2.stability, 2)}%\nAverage_Residual_Energy = {bfs.total_energy}%\nAverage_Speed = {bfs.avg_speed}m/s\nHops = {bfs.hop_count}\nTotal_Distance = {bfs.total_dist}m\nEnergy_Consumed{i} = {bfs.energy_cons}%\nLifetime_{i} = {bfs.lifetime}s\n\n'
        text_paths += new_text

        self.m_ui.disjoint_paths_field.setText(text_paths)
