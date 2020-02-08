dictionary = {'One': 'Раз', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('create_file.txt', 'w', encoding='utf-8') as create:
    with open('test4_file.txt', 'r+', encoding='utf-8') as file:
        for string in file:
            inx = string.split()
            el = dictionary.get(inx[0])
            create.write(' '.join([el, inx[1], inx[2], '\n']))
