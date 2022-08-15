# with open('Textfile.txt', 'r') as my_file:
#     print(f'Содержимое файла: \n {my_file.read()}')
#     my_file = open('Textfile.txt', 'r')
#     q_str = my_file.readlines()
#     print(f'Количество строк в файле - {len(q_str)}')
#     for i in range(len(q_str)):
#         print(f'Количество символов {i+1} строки - {len(q_str[i])}')
#     my_file = open('Textfile.txt', 'r')
#     q_world = my_file.read()
#     q_world = q_world.split()
#     print(f'Общее количество слов - {len(q_world)}')

with open('Textfile.txt', 'r', encoding="utf-8") as my_file:
    print(f'Содержимое файла: \n {my_file.read()}')
    my_file = open('Textfile.txt', 'r')
    q_str = my_file.readlines()
    print(f'Количество строк в файле - {len(q_str)}')
    my_file = open('Textfile.txt', 'r')
    my_line = my_file.readlines()
    for index, value in enumerate(my_line, 1):
        q_words = len(value.split())
        print(f'Строка {index} содержит {q_words} слов')
