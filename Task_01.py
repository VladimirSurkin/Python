# print("Для выхода введите пустую строку.")
# new_el = 1
# my_list = []
# while new_el != None:
#     new_el = input('Введите данные:')
#     if not new_el:
#         break
#     my_list.append(new_el)
# with open('textfile.txt', "w", encoding="utf-8") as f_txt:
#     try:
#         for i in my_list[:-1]:
#             f_txt.write(f"{i}\n")
#         f_txt.write(my_list[-1])
#     except:
#         if my_list==[]:
#             print('Вы не ввели данные. Повторите попытку')
# f_txt = open('textfile.txt', 'r')
# context = f_txt.readlines()
# print(context)
# f_txt.close()

print("Для выхода введите пустую строку.")
with open('textfile.txt', "w", encoding="utf-8") as f_txt:
    while True:
        new_el = input('Введите данные:')
        if not new_el:
            break
        f_txt.write(f"{new_el}\n")
