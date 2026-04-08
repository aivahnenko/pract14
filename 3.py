list1 = input('Введите 1й список: ').split()
list2 = input('Введите 2й список: ').split()
list1_int = [int(x) for x in list1] # преобразую строки в числа
list2_int = [int(x) for x in list2]
original = [list1_int, list2_int]
filtered = [] # оставляю только положительные числа
for lst in [list1, list2]:
    good = [int(x) for x in lst if int(x) > 0]
    filtered.append(good)

print(f'Исходный список: {original}')
print(f'Отфильтрованный список: {filtered}')
