class MultiPathAlgorithm:
    def __init__(self, graph, start_node, end_node):
        self.graph = graph
        self.start_node = start_node
        self.end_node = end_node
        self.disjoint_paths = []
        self.disjoint_paths_metrics = []

    def search_paths(self, start_node, end_node, path=[]):
        path = path + [start_node]
        if start_node == end_node:
            return [path]
        if start_node not in self.graph.get_all_nodes():
            return []
        paths_list = []
        for neighbor in start_node.neighbors_dict:
            if neighbor not in path:
                found_new_paths = self.search_paths(neighbor, end_node, path)
                for new in found_new_paths:
                    paths_list.append(new)
        return paths_list

    def select_disjoint_paths(self, path=[]):
        paths_list = self.search_paths(self.start_node, self.end_node, path)
        path_metrics = []

        for path in paths_list:
            avg_speed = round(sum(i.get_node_speed() for i in path) / len(path), 2)
            total_energy = round(sum(i.get_node_energy() for i in path) / len(path), 2)
            hop_count = len(path) - 1
            total_dist = sum(i.get_dist_to_neighbor(j) for i, j in zip(path, path[1::]))
            path_metrics.append((path, total_energy, avg_speed, hop_count, total_dist))

        def intersect_check(path, paths):
            count = 0
            for p in paths:
                if set(path[1:-1]).intersection(set(p[1:-1])) == set():
                    count += 1
            return count

        sort_list = sorted(path_metrics, key=lambda element: (element[3], -element[1], -element[2]))

        self.disjoint_paths.append(sort_list[0][0])
        for path, energy, speed, hop, dist in sort_list:
            if path not in self.disjoint_paths:
                count = intersect_check(path, self.disjoint_paths)
                if count == len(self.disjoint_paths):
                    self.disjoint_paths.append(path)

        self.get_path_metrics(self.disjoint_paths)

    def get_path_metrics(self, paths):
        for path in paths:
            avg_speed = round(sum(i.get_node_speed() for i in path) / len(path), 2)
            total_energy = round(sum(i.get_node_energy() for i in path) / len(path), 2)
            hop_count = len(path) - 1
            total_dist = round(sum(i.get_dist_to_neighbor(j) for i, j in zip(path, path[1::])), 2)
            energy_cons = (100 - total_energy)/(total_dist/avg_speed)
            lifetime = min(i.get_node_energy() for i in path)/2

            integer_path_view = [i.get_node_id() for i in path]  # turn nodes into their identifiers
            self.disjoint_paths_metrics.append(
                (integer_path_view, (avg_speed, total_energy, hop_count, total_dist, energy_cons, lifetime)))  # paths and params
