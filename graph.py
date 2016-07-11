from collections import defaultdict

class Graph(object):
    def __init__(self, connects, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connects(connects)

    def add_connects(self, connects):
        for prev, next in connects:
            self.add(prev, next)

    def add(self, prev, next):
        self._graph[prev].add(next)
        if not self._directed:
            self._graph[next].add(prev)

    def remove(self, prev, next):
        self._graph[prev].remove(next)
        if not self._directed:
            self._graph[next].remove(prev)
        if len(self._graph[prev]) == 0:
            del self._graph[prev]
        if len(self._graph[next]) == 0:
            del self._graph[next]

    def children(self, node):
        if len(self._graph[node]) > 0:
            return "{}: {}".format(node, self._graph[node])
        else:
            return "{} has no children.".format(node)

    def is_linked(self, prev, next, path=[]):
        path = path + [prev]
        if prev == next:
            print "Path: ", path
            return True
        if prev not in self._graph:
            return False
        for node in self._graph[prev]:
            if node not in path:
                new_path = self.is_linked(node, next, path)
                if new_path:
                    return new_path
        return False

    def __str__(self):
        return 'Graph:({})'.format(dict(self._graph))

connects = []
my_graph = Graph(connects, directed=False)
my_graph.add(1,2)
my_graph.add(2,3)
my_graph.add(3,4)
print my_graph
print my_graph.is_linked(3,1)
my_graph.remove(3,4)
print my_graph.is_linked(1,4)
print my_graph
