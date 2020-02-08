import json

dictionary = {}
average, s, m = 0, 0, 0


def summary(a, b):
    s = float(a) - float(b)
    return s


with open('mifile.json', 'w') as structure:

    with open('test_file7.txt', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.split()
            summ = summary(line[2], line[3])
            dicti = dict.fromkeys([line[0]], summ)
            dictionary.update(dicti)
            if summ > 0:
                average += summ
                m += 1
        average = average / m
        dicti = dict.fromkeys(['average'], average)
        dictionary = [dictionary, dicti]
    print(dictionary)

    json.dump(dictionary, structure)