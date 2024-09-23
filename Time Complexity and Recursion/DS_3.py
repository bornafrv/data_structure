burger = input()
text = ""
max_len = 0
for start in range(len(burger)):
    for end in burger[start:]:
        if end in text:
            if len(text) > max_len: max_len = len(text)
            text = ""
            break
        else: text += end
if len(text) > max_len: max_len = len(text)
print(max_len)