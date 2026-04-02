import random
numbers = [
    [random.randint(1, 100) for _ in range(3)],
    [random.randint(1, 100) for _ in range(2)]
]
print(f'Исходный вложенный список: {numbers}')
sums = []
total = 0
for i in numbers:
    line_sum = 0
    for j in i: #берем элемент из i = линии
        line_sum += j #прибавляе м его к сумме
    sums.append(line_sum)
    total += line_sum
print(f'Суммы строк: {sums}')
print(f'Общая сумма: {total}')
print(f'Максимальная сумма в строке {sums.index(max(sums)) + 1} = {max(sums)}')