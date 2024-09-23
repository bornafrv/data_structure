import sys
import re


class Queue:
    def __init__(self):
        self.q = []

    def getSize(self):
        return len(self.q)

    def enqueue(self, value):
        self.q.append(value)

    def dequeue(self):
        return self.q.pop(0)

    def isEmpty(self):
        if len(self.q) == 0 : return True
        else : return False

    def getInOneLine(self):
        """qInLine = ""
        if len(self.q) != 0:
            for i in range(len(self.q) - 1):
                qInLine += (str(self.q[i]) + ' ')
            qInLine += str(self.q[len(self.q) - 1])
        print(qInLine)"""
        print(*self.q)


class Stack:
    def __init__(self, size=10):
        self.s = []
        self.cap = size

    def isEmpty(self):
        if len(self.s) == 0 : return True
        else : return False

    def push(self, value):
        self.s.append(value)

    def pop(self):
        return(self.s.pop())

    def put(self, value):
        self.s.pop()    
        self.s.append(value)

    def peek(self):
        return self.s[-1]

    def expand(self):
        self.cap = self.cap * 2

    def getInOneLine(self):
        print(*self.s)

    def getSize(self):
        return len(self.s)

    def getCapacity(self):
        return self.cap


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def getList(self):
        values = ""
        node = self.head
        while(node != None):
            values += (str(node.value) + " ")
            node = node.next
        print(values)

    def insertFront(self, new_data):
        new_node = Node(new_data)
        if self.head != None: new_node.next = self.head
        self.head = new_node

    def insertEnd(self, new_data):
        new_node = Node(new_data)
        if self.head == None: self.head = new_node
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = new_node
            

    def reverse(self):
        prev = None
        temp = self.head
        while(temp != None):
            next = temp.next
            temp.next = prev 
            prev = temp 
            temp = next
        self.head = prev 
            


class Runner:
    dsMap = {'stack': Stack, 'queue': Queue, 'linked_list': LinkedList}
    callRegex = re.compile(r'^(\w+)\.(\w+)\(([\w, ]*)\)$')

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
        args = argsList.split(',') if argsList != '' else []

        method = getattr(self.items[itemName], funcName)
        result = method(*args)
        if result is not None:
            print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
