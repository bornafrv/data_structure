import itertools

n = int(input())
t = int(input())
word = "abcdefgh"[:n]

firsts = []
seconds = []
for i in range(t):
    x, y = input().split()
    firsts.append(x)
    seconds.append(y)

permutations = []
for per in itertools.permutations(word):
    permutations.append("".join(per))

heights = {}
gray = {}
for vertex in permutations:
    heights[vertex] = 0
    gray[vertex] = 0
gray[word] = 1
    
queue = []
queue.append(word)
while len(queue) > 0:
    for left in range(n):
        for right in range(left + 1, n):
            one_reverse = queue[0][:left] + queue[0][left : right + 1][::-1] + queue[0][right + 1:]
            if (not gray[one_reverse]):
                queue.append(one_reverse)
                gray[one_reverse] = 1
                heights[one_reverse] = heights[queue[0]] + 1
    queue.pop(0)

mappings = {}  
for senario in range(t):
    for char in word:
        mappings[char] = ""
    
    s1 = firsts[senario]
    s2 = seconds[senario]
    
    count = 0
    for char in s1:
        mappings[word[count]] += char
        count += 1
    map_keys = list(mappings.keys())
    map_vals = list(mappings.values())
        
    final_s = ""
    for char in s2:
        indx = map_vals.index(char)
        final_s += map_keys[indx]
    
    print(heights[final_s])