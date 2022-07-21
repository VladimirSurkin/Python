#4
input_str = input("Введите строку из несколько слов, разделенных пробелами: ")
input_str.split()
n = 1
for i in input_str.split():
    if len(i) > 10:
        print(n, "-", i[:10])
        n += 1
    else:
        print(n, "-", i)
        n += 1
