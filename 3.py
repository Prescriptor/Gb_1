tramps = []
average = 0

with open("test3_file.txt", "r", encoding='utf-8') as file:
    for string in file:
        a = string.split()
        if float(a[1]) < 20000.00:
            tramps.append(a[0])
            average += float(a[1])
    print(tramps)
    print('Средняя зарплата: ', average / len(tramps))