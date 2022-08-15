# def translate_file():
#     num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
#     new_text = []
#     try:
#         with open('Testfile.txt', 'r', encoding="utf-8") as file:
#             with open('Lesson_4.txt', 'w', encoding="utf-8") as new_file:
#                 l = file.readlines()
#                 for i in l:
#                     i = i.split(' ', 1)
#                     new_text.append(num[i[0]] + ' ' + i[1])
#                 new_file.writelines(new_text)
#     except FileNotFoundError:
#         return 'Файл не найден.'

# translate_file()

from googletrans import Translator
with open ("Lesson_4.txt", 'w', encoding='utf-8') as f:
    with open('Testfile.txt', 'r', encoding="utf-8") as f1:
        text = f1.read()
    try:
        f.write(Translator().translate(text, dest='ru').text)
    except AttributeError:
        print ("DDoS-атака на Google не прошла, продолжаем попытки! :)")

