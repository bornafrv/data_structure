word = input()
my_dict = {}
bit_map = 0
result = 0
my_dict[0] = 1
for i in range(1, 1024):
    my_dict[i] = 0

for char in word:
    which_bit = ord(char)-97
    bit_map ^= 1 << which_bit
    result += my_dict[bit_map]
    for alph in range(10):
        result += my_dict[bit_map ^ (1 << alph)]
    my_dict[bit_map] += 1

print(result)