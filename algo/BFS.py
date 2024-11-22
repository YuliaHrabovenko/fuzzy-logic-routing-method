from collections import deque


class BFS:
    def __init__(self, graph, start, end):
        self.graph = graph
        self.start = start
        self.end = end
        self.path = []
        self.avg_speed = float
        self.total_energy = float
        self.hop_count = int
        self.total_dist = float
        self.energy_cons = float
        self.lifetime = float

    def shortest_path(self):
        # create a queue for BFS
        queue = deque()
        # enqueue the start node and mark as visited
        queue.append(self.start)
        visited = {self.start}
        # create a dictionary to store the parent node of each visited node
        parent = {self.start: None}
        # BFS loop
        while queue:
            # dequeue a vertex from the queue
            current_node = queue.popleft()
            # if the current node is the end node, return the path
            if current_node == self.end:
                path = []
                # backtrace the path from the end node to the start node using parent dictionary
                while current_node != self.start:
                    path.append(current_node)
                    current_node = parent[current_node]
                path.append(self.start)
                path.reverse()
                self.path = [i.get_node_id() for i in path]
                self.avg_speed = round(sum(i.get_node_speed() for i in path) / len(path), 2)
                self.total_energy = round(sum(i.get_node_energy() for i in path) / len(path), 2)
                self.hop_count = len(path) - 1
                self.total_dist = round(sum(i.get_dist_to_neighbor(j) for i, j in zip(path, path[1::])), 2)
                self.energy_cons = (100 - self.total_energy) / (self.total_dist / self.avg_speed)
                self.lifetime = round(min(i.get_node_energy() for i in path) / self.energy_cons, 2)
                return path
            # visit all the neighbors_dict of the current node
            for neighbor in current_node.neighbors_dict:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    parent[neighbor] = current_node
        # if there is no path from start to end, return None
        return None
