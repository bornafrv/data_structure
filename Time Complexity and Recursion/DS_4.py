number = input()
def func(x, y, substr):
    #print("aa" + substr + "aa")
    if len(substr) == 0: 
        #print("true")
        return True
    z = x + y

    if str(z) == substr[ : len(str(z)) + 1]:
        #print(y, int(substr[ : len(str(z)) + 1]),  substr[len(str(z)): ])
        return func(y, int(substr[ : len(str(z)) + 1]), substr[len(str(z)): ])
    elif str(z) == substr[:len(str(z))]:
        #print(y, int(substr[ : len(str(z))]),  substr[len(str(z)): ])
        return func(y, int(substr[ : len(str(z))]), substr[len(str(z)): ])
    else: 
        #print("false")
        return False

result = 0
for i in range(0, len(number)):
    for j in range(i+1 ,len(number)):
        if number[ : i+1][0] != '0' and number[i+1 : j+1][0] != '0':
            #print(number[ : i+1][0] + "Aa" + number[i+1 : j+1][0])
            x = int(number[ : i+1])
            y = int(number[i+1 : j+1])
            #print("bb" + number[j + 1:] + "bb")
            if len(number[j + 1:]) != 0:
                if (func(x, y, number[j+1 : ])):
                    print("YES")
                    exit()
print("NO")
        