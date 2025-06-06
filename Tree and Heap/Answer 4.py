class Tree:
    class Node:
        def __init__(self, indx, prnt = None):
            self.index = indx
            self.parent = prnt
            self.children = []
            self.state = "shir"
            self.khat_children = 0
            
    def __init__(self):
        self.root = self.Node(1)
        self.nodes = []
        self.nodes.append(self.root)
    
    def insert(self, prnt, indx):
        new_node = self.Node(indx, prnt)
        self.nodes.append(new_node)   
        
node_numbers, rounds = input().split()
parents_index = list(map(int, input().split()))
tree = Tree()

khat = []
for i in range(int(rounds)):
    khat.append(list(map(int, input().split())))
    khat[i].pop(0)
    
index = 2
for parent in parents_index:
    tree.insert(parent, index)
    tree.nodes[parent - 1].children.append(index)
    index += 1

result = []
for i in range(int(rounds)):
    ans = 0
    for indx in khat[i]:
        tree.nodes[indx - 1].state = "khat"
    for indx in khat[i]:
        parent_index = tree.nodes[indx - 1].parent
        if (parent_index == None):
            continue
        if (tree.nodes[parent_index - 1].state == "khat"):
            tree.nodes[parent_index - 1].khat_children += 1
    for indx in khat[i]:
        total_children = len(tree.nodes[indx - 1].children)
        khat_children = tree.nodes[indx - 1].khat_children
        ans += 1 + total_children - (2 * khat_children)
    for indx in khat[i]:
        parent_index = tree.nodes[indx - 1].parent
        if (parent_index == None):
            continue
        if (tree.nodes[parent_index - 1].state == "khat"):
            tree.nodes[parent_index - 1].khat_children = 0
    for indx in khat[i]:
        tree.nodes[indx - 1].state = "shir"
    result.append(str(ans))
    
print("\n".join(result))