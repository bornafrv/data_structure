class Tree:
    class Vertex:
        def __init__(self, indx):
            self.index = indx
            self.children = []
            self.parent = None

    def __init__(self):
        self.vertexes = []
        self.root = None
        self.heights = []

    def insert(self, indx):
        new_vertex = self.Vertex(indx)
        if (self.root == None):
            self.root = new_vertex
        self.vertexes.append(new_vertex)
        self.heights.append(0)
        
    def add_child_and_parent(self, u, v):
        self.vertexes[u].children.append(v)
        self.vertexes[v].parent = u
        
    def set_heights(self):
        for vrtx in self.vertexes:
            l = []
            vertex = vrtx.index
            if (vertex == 0):
                continue
            self.shortest_path(0, vertex, l)
            self.heights[vertex] = len(l) - 1
    
    def first_joint_ancestor(self, indx1, indx2):
        if (indx1 == 0 or indx2 == 0):
            return 0
        vertex1 = indx1
        vertex2 = indx2
        if (self.heights[vertex1] > self.heights[vertex2]):
            while (self.heights[vertex1] != self.heights[vertex2]):
                vertex1 = self.vertexes[vertex1].parent
        elif (self.heights[vertex1] < self.heights[vertex2]):
            while (self.heights[vertex1] != self.heights[vertex2]):
                vertex2 = self.vertexes[vertex2].parent
        while (self.vertexes[vertex1].index != self.vertexes[vertex2].index):
            vertex1 = self.vertexes[vertex1].parent
            vertex2 = self.vertexes[vertex2].parent
        return self.vertexes[vertex1].index
    
    def shortest_path(self, start, leaf, l):
        l.append(leaf)
        if (self.vertexes[leaf].index == 0):
            return
        if (self.vertexes[leaf].index == self.vertexes[start].index):
            return
        self.shortest_path(start, self.vertexes[leaf].parent, l)
            
n = int(input())
size = (2 * n) - 2

G = Tree()
for indx in range(n):
    G.insert(indx)

for edge in range(n - 1):
    u, v = input().split()
    G.add_child_and_parent(int(u) - 1, int(v) - 1)
G.set_heights()
    
leaves = list(map(int, input().split()))

result = []
G.shortest_path(0, leaves[0] - 1, result)
result.reverse()
result.pop()
for i in range(len(leaves) - 1):
    l1 = []
    l2 = []
    ancestor = G.first_joint_ancestor(leaves[i] - 1, leaves[i + 1] - 1)
    G.shortest_path(ancestor, leaves[i] - 1, l1)
    result.extend(l1)
    result.pop()
    G.shortest_path(ancestor, leaves[i + 1] - 1, l2)
    l2.reverse()
    result.extend(l2)
    result.pop()
l = []
G.shortest_path(0, leaves[-1] - 1, l)
result.extend(l)
result.pop()

result = [vertex + 1 for vertex in result]
if (len(result) == size):
    print(*result)
else:
    print(-1)