
from nodes.Node import Node
from queue import LifoQueue
def dfs_adj_matrix(graph, start, target):
    visited = set()
    target_node = Node(target)
    open_nodes = LifoQueue()
    node_start = Node(start)
    open_nodes.put(node_start)
    while not open_nodes.empty():
        node = open_nodes.get()
        if node.getValue() == target:
            target_node = node
            break
        visited.add(node.getValue())
        neighbors = [neighbor for neighbor in range(len(graph[node.getValue()])) if neighbor not in visited and graph[node.getValue()][neighbor] == 1]
        for neighbor in neighbors:
            neigh_node = Node(neighbor)
            neigh_node.setParent(node)
            open_nodes.put(neigh_node)
    if target_node.getParent() is not None:
        temp = target_node
        res = []
        while temp is not None:
            res.append(temp.getValue())
            temp = temp.getParent()
        return res[::-1]