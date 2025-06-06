import sys
import re

INVALID_INDEX = 'invalid index'
OUT_OF_RANGE_INDEX = 'out of range index'
EMPTY = 'empty'

class MinHeap:
    class Node:
        def __init__(self, value):
            self.key = value

    def __init__(self):
        self.heap = []

    def bubble_up(self, index):
        if (type(index) != int):
            raise Exception(INVALID_INDEX)
        if (index >= len(self.heap) or index < 0):
            raise Exception(OUT_OF_RANGE_INDEX)
        if (len(self.heap) == 0):
            raise Exception(EMPTY)
        while (index > 0):
            parent = (index - 1) // 2
            if (parent >= 0 and self.heap[parent].key > self.heap[index].key):
                temp = self.heap[parent].key
                self.heap[parent].key = self.heap[index].key
                self.heap[index].key = temp
                index = parent
            else:
                break

    def bubble_down(self, index):
        if (type(index) != int):
            raise Exception(INVALID_INDEX)
        if (index >= len(self.heap) or index < 0):
            raise Exception(OUT_OF_RANGE_INDEX)
        if (len(self.heap) == 0):
            raise Exception(EMPTY)
        minn = index
        while (2 * index < len(self.heap)):
            left = (2 * index) + 1
            right = (2 * index) + 2
            if (left < len(self.heap) and self.heap[left].key < self.heap[minn].key):
                minn = left
            if (right < len(self.heap) and self.heap[right].key < self.heap[minn].key):
                minn = right
            if (minn != index):
                temp = self.heap[minn].key
                self.heap[minn].key = self.heap[index].key
                self.heap[index].key = temp
                index = minn
            else:
                break

    def heap_push(self, value):
        new_node = self.Node(value)
        self.heap.append(new_node)
        self.bubble_up(len(self.heap) - 1)

    def heap_pop(self):
        if (len(self.heap) == 0):
            raise Exception(EMPTY)
        root = self.heap[0].key
        self.heap[0].key = self.heap[-1].key
        self.heap.pop()
        if (len(self.heap) != 0):
            self.bubble_down(0)
        return root

    def find_min_child(self, index):
        if (type(index) != int):
            raise Exception(INVALID_INDEX)
        if (index >= len(self.heap) or index < 0):
            raise Exception(OUT_OF_RANGE_INDEX)
        if (len(self.heap) == 0):
            raise Exception(EMPTY)
        left = (2 * index) + 1
        right = (2 * index) + 2
        minn = left
        if (right < len(self.heap) and self.heap[right].key < self.heap[left].key):
            minn = right
        return minn

    def heapify(self, *args):
        for val in args:
            self.heap_push(val)

class HuffmanTree:
    class Node:
        def __init__(self, lett, rep, lft = None, rght = None):
            self.left = lft
            self.right = rght
            self.letter = lett
            self.repeat = rep
            self.code = -1
            
    def __init__(self):
        self.nodes = []
        self.letters = []
        self.repeats = []

    def set_letters(self, *args):
        self.letters = args

    def set_repetitions(self, *args):
        self.repeats = args

    def build_huffman_tree(self):
        for i in range(len(self.letters)):
            new_node = self.Node(self.letters[i], self.repeats[i])
            self.nodes.append(new_node)
        while (len(self.nodes) != 1):
            self.nodes.sort(key=lambda x: x.repeat)
            left = self.nodes.pop(0)
            right = self.nodes.pop(0)
            left.code = 0
            right.code = 1
            new_node = self.Node("", left.repeat + right.repeat, left, right)
            self.nodes.append(new_node)
                        
    def rec_cost(self, root, count):
        summ = 0
        if (root.left != None and root.right != None):
            count += 1
            if (root.left.letter != ""):
                summ += (count * root.left.repeat)
            if (root.right.letter != ""):
                summ += (count * root.right.repeat)   
            summ += self.rec_cost(root.left, count)
            summ += self.rec_cost(root.right, count)
        return summ

    def get_huffman_code_cost(self):
        count = 0
        cost = self.rec_cost(self.nodes[0], count)
        print(cost)
        
    def text_encoding(self, text):
        lett_and_rep = {}
        for lett in text:
            if (lett not in lett_and_rep.keys()):
                lett_and_rep[lett] = 1
            else:
                lett_and_rep[lett] += 1
        self.set_letters(*list(lett_and_rep.keys()))
        self.set_repetitions(*list(lett_and_rep.values()))
        self.build_huffman_tree()

class Bst:
    class Node:
        def __init__(self, value):
            self.key = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = self.Node(key)
        if (self.root == None):
            self.root = new_node
            return
        cur = self.root
        while (True):
            if (key <= cur.key):
                if (cur.left != None):
                    cur = cur.left
                else:
                    cur.left = new_node
                    break
            elif (key > cur.key):
                if (cur.right != None):
                    cur = cur.right
                else:
                    cur.right = new_node
                    break
                
    def rec_inorder(self, root, nodes):
        if (root == None):
            return
        self.rec_inorder(root.left, nodes)
        nodes.append(root.key)
        self.rec_inorder(root.right, nodes)

    def inorder(self):
        if (self.root == None):
            raise Exception(EMPTY)
        nodes = []
        self.rec_inorder(self.root, nodes)
        for i in range(len(nodes) - 1):
            print(nodes[i], end=" ")
        print(nodes[-1])
        
class Runner:
    dsMap = {'min_heap': MinHeap, 'bst': Bst, 'huffman_tree': HuffmanTree}
    callRegex = re.compile(r'^(\w+)\.(\w+)\(([\w, \-"\']*)\)$')

    def __init__(self, inputSrc):
        self.input = inputSrc
        self.items = {}

    def run(self):
        for line in self.input:
            line = line.strip()
            action, _, param = line.partition(' ')
            actionMethod = getattr(self, action, None)
            if actionMethod is None:
                return
            actionMethod(param)

    def make(self, params):
        itemType, itemName = params.split()
        self.items[itemName] = self.dsMap[itemType]()

    def call(self, params):
        regexRes = self.callRegex.match(params)
        itemName, funcName, argsList = regexRes.groups()

        args = [x.strip() for x in argsList.split(',')] if argsList != '' else []
        args = [x[1:-1] if x[0] in ('"', "'") else int(x) for x in args]

        method = getattr(self.items[itemName], funcName)
        try:
            result = method(*args)
        except Exception as ex:
            print(ex)
        else:
            if result is not None:
                print(result)

def main():
    runner = Runner(sys.stdin)
    runner.run()

if __name__ == "__main__":
    main()