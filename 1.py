import random
numbers = [
    [random.randint(1, 100) for i in range(3)],
    [random.randint(1, 100) for i in range(2)]
]
print(f'Исходный вложенный список: {numbers}')
value = numbers[0][0]
row = 0
col = 0
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        if numbers[i][j] > value:  #текущий элемент больше максимального
            value = numbers[i][j]  #этот элемент становится новым максимумом
            row, col = i, j
print(f'Максимальный элемент: {value}')
print(f'Позиция: список {row + 1}, индекс {col}')