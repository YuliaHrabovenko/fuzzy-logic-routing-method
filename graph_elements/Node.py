class Node:
    def __init__(self, node_id, speed, energy):
        self.node_id = node_id
        self.neighbors_dict = {}
        self.energy = energy
        self.speed = speed

    def get_node_id(self):
        return self.node_id

    def get_node_energy(self):
        return self.energy

    def get_node_speed(self):
        return self.speed

    def set_adjacent(self, node_object, distance):
        self.neighbors_dict[node_object] = distance

    def extract_adjacent(self, node_object):
        del self.neighbors_dict[node_object]

    def get_dist_to_neighbor(self, node_object):
        return self.neighbors_dict[node_object]
