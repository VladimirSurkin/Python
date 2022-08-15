with open('Lesson_6.txt', 'r', encoding="utf-8") as f:
    for l in f:
        new_str = ''.join((i if i in '1234567890' else ' ') for i in l)
        new_sum = [int(i) for i in new_str.split()]
        print(f'{l.split()[0]} {sum(new_sum)}')
