with open("test1_file.txt", "a", encoding='utf-8') as file:
    string = 0
    while string != '':
        string = input(("Введите данные: "))
        file.write(f'{string}\n')