dictionary = {}
chislo = []
per = ''
a = ''


def summary(x):
    s = 0
    for el in x:
        s += int(el)
    return s


with open('test6_file.txt', 'r', encoding='utf-8') as file:
    for line in file:
        for el in line:
            try:
                if int(el) > -1:
                    per = per + el
            except ValueError:
                pass
            if el == '(':
                chislo.append(per)
                per = ''
        dist = line.split()[0][0:-1]
        dicti = dict.fromkeys([dist], summary(chislo))
        chislo = []
        dictionary.update(dicti)
    print(dictionary)
