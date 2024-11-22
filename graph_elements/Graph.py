from graph_elements.Node import Node


class Graph:
    def __init__(self):
        self.nodes_dict = {}

    def append_new_node(self, node_id, speed, energy):
        self.nodes_dict[node_id] = Node(node_id, speed, energy)

    def append_new_edge(self, from_node_id, to_node_id, dist):
        if from_node_id not in self.nodes_dict:
            self.append_new_node(from_node_id)
        if to_node_id not in self.nodes_dict:
            self.append_new_node(to_node_id)

        self.nodes_dict[from_node_id].set_adjacent(self.nodes_dict[to_node_id], dist)
        self.nodes_dict[to_node_id].set_adjacent(self.nodes_dict[from_node_id], dist)

    def extract_edge(self, from_node_id, to_node_id):
        self.nodes_dict[from_node_id].extract_adjacent(self.nodes_dict[to_node_id])
        self.nodes_dict[to_node_id].extract_adjacent(self.nodes_dict[from_node_id])

    def get_all_nodes(self):
        return self.nodes_dict.values()

    def get_node_by_id(self, node_id):
        return self.nodes_dict[node_id]
