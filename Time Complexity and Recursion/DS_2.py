test = input()
result_list = []
for i in range(int(test)):
    result = ""
    p = input()
    if p[0:2] == "12": p = "00" + p[2:]
    friends = input()
    for i in range(int(friends)):
        time_i = input()
        if time_i[0:2] == "12": time_i = "00" + time_i[2:]
        if time_i[9:11] == "12": time_i = time_i[:9] + "00" + time_i[11:]
        if time_i[6] == p[6] and time_i[15] > p[6] and time_i[0:5] <= p[0:5]: result += '1'
        elif time_i[6] < p[6] and time_i[15] == p[6] and time_i[9:14] >= p[0:5]: result += '1'
        elif time_i[6] == p[6] and time_i[15] == p[6] and time_i[0:5] <= p[0:5] and time_i[9:14] >= p[0:5]: result += '1'
        else: result += '0'
    result_list.append(result)

for item in result_list:
    print(item)