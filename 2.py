with open("test2_file.txt", "r", encoding='utf-8') as file:
    i = 0
    for string in file:
        i += 1
        print(i, 'строка -', len(string.split()))
print('Итого строк: ', i)