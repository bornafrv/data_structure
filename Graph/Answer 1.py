n, m = input().split()

adj_list = {}
ok_vertexes = []
for vertex in range(int(n) + 1):
    adj_list[vertex] = []
    ok_vertexes.append(0)

for i in range(int(m)):
    u, v = input().split()
    adj_list[int(u)].append(int(v))
    adj_list[int(v)].append(int(u))
    
result = []
while (0 in ok_vertexes[1:]):
    max_edges = 0
    founded = 0
    for i in range(1, int(n) + 1):
        if ((len(adj_list[i]) > max_edges) and (ok_vertexes[i] == 0)):
            max_edges = len(adj_list[i])
            vertex = i
            founded = 1
    if (founded):
        ok_vertexes[vertex] = 1
        for ver in adj_list[vertex]:
            ok_vertexes[ver] = 1
        result.append(str(vertex))

print(len(result))
print(" ".join(result))