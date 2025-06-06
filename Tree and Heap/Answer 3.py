class Modarres:
    def __init__(self, strt, unt, rag):
        self.start = strt
        self.units = unt
        self.index = -1
        self.rage = rag
        
n, days = input().split()
raged_maxheap = []

for i in range(int(n)):
    A, T, S = input().split()
    raged_maxheap.append(Modarres(int(A), int(T), int(S)))
raged_maxheap.sort(key=lambda teacher: teacher.rage, reverse=True) 

for day in range(1, int(days) + 1):
    for teacher in raged_maxheap:
        if (teacher.units == 0):
            continue
        if (teacher.start <= day):
            teacher.units -= 1
            break
        
total_rage = 0
for teacher in raged_maxheap:
    total_rage += teacher.units * teacher.rage
    
print(total_rage)