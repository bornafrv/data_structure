class Stack:
    def __init__(self):
        self.stack = []
    def isEmpty(self):
        return len(self.stack) == 0
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        return self.stack.pop(len(self.stack) - 1)
    def put(self, value):
        if not self.isEmpty():
            self.pop()
            self.push(value)
    def peek(self):
        if(not self.isEmpty()):
            return self.stack[len(self.stack) - 1]
        else:
            return 0
    def getInOneLine(self):
        return ' '.join(map(str,self.stack))



n = int(input())
inp = [int(i) for i in input().split()]
pos = {inp[i]:i for i in range(len(inp))}


prev = {0:-2}

s = Stack()
for i in range(n, 0, -1):
    if(s.isEmpty()):
        s.push(pos[i])
        prev[pos[i]] = -1
    else:
        while(s.peek() > pos[i]):
            s.pop()
        if(s.isEmpty()):
            s.push(pos[i])
            prev[pos[i]] = -1
        else:
            prev[pos[i]] = s.peek()
            s.push(pos[i])


# print (pos)
# print (inp)
# print (prev)

ans = [0] * (n+1)
ss = Stack()
for i in range(1,n+1):
    ans[i] = ans[i-1]
    while( not ss.isEmpty() and pos[i] < ss.peek()):
        ss.pop()
        ans[i]-=1
    if(prev[pos[i]] != -1 and (ss.isEmpty()) | prev[pos[i]] != -1 and prev[pos[i]] != prev[ss.peek()]):
        ans[i]+=1
        ss.push(pos[i])
        
for i in range(len(ans)):
        print(ans[i])