import random
numbers = [
    [random.randint(1, 100) for _ in range(3)],
    [random.randint(1, 100) for _ in range(2)]
]
print(f'Исходный вложенный список: {numbers}')
element = int(input('Введите значение для поиска: '))
for i in range(len(numbers)): #работа с внешними списками
    for j in range(len(numbers[i])): #работа со внутренними списками
        if numbers[i][j] == element:
            print(f'список {i + 1}, индекс {j}')