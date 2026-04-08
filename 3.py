list1 = input('Введите 1й список: ').split()
list2 = input('Введите 2й список: ').split()
original = [[int(x) for x in list1], [int(x) for x in list2]] #собираем вложенный список из 2х обычных
filtered = [[int(x) for x in lst if int(x) > 0] for lst in [list1, list2]] #собираем вложенный список с элементами где х>0
print(f'Исходный список: {original}')
print(f'Отфильтрованный список: {filtered}')
