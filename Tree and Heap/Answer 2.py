class Bst:
    class Node:
        def __init__(self, value, indx):
            self.key = value
            self.left = None
            self.right = None
            self.parent = None
            self.height = 0
            self.index = indx

    def __init__(self):
        self.nodes = []
        self.root = None

    def insert(self, key, indx):
        new_node = self.Node(key, indx)
        if (self.root == None):
            self.root = new_node
            self.nodes.append(self.root)
            return
        cur = self.root
        while (True):
            if (key < cur.key):
                new_node.height += 1
                if (cur.left != None):
                    cur = cur.left
                else:
                    new_node.parent = cur
                    cur.left = new_node
                    self.nodes.append(cur.left)
                    break
            elif (key >= cur.key):
                new_node.height += 1
                if (cur.right != None):
                    cur = cur.right
                else:
                    new_node.parent = cur
                    cur.right = new_node
                    self.nodes.append(cur.right)
                    break
        return new_node.parent.key
    
    def first_joint_ancestor(self, indx1, indx2):
        node1 = node2 = self.root
        for node in self.nodes:
            if (node.index == indx1):
                node1 = node
            if (node.index == indx2):
                node2 = node
        if (node1.height > node2.height):
            while (node1.height != node2.height):
                node1 = node1.parent
        elif (node1.height < node2.height):
            while (node1.height != node2.height):
                node2 = node2.parent
        while (node1 != node2):
            node1 = node1.parent
            node2 = node2.parent
        return node1.index
            
n = int(input())
nodes = list(input().split())
a, b = input().split()
BST = Bst()

parents = []
for i in range(len(nodes)):
    parent = BST.insert(int(nodes[i]), i + 1)
    if (i != 0):
        parents.append(parent)

ancestor = BST.first_joint_ancestor(int(a), int(b))

print(*parents)
print(ancestor)