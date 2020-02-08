import random

string = []
with open('test5_file.txt', 'w') as file:
    i = int((random.random() * 100 // 1))
    x = 0
    while x < i:
        string.append(int(random.random() * 10000 // 1))
        x += 1
    string = ''.join(str(string).split(','))
    string = string.replace('[', '')
    string = string.replace(']', '')
    file.write(string)
print(string)

with open('test5_file.txt', 'r') as file:
    s = 0
    string = file.read()
    for el in string.split():
        s += int(el)
    print(s)