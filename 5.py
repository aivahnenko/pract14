N = int(input('Сколько предметов может унести игрок (целое число) '))
text = input('Ценности всех найденных предметов (список целых чисел, разделённых пробелами) ').split()
cost_str = text
cost = [] 
for x in cost_str:
    cost.append(int(x))
positive = [] # Оставляю только предметы с положительной ценностью (ценные предметы)
for x in cost:
    if x > 0:
        positive.append(x)
positive.sort(reverse=True) # Сортирую от самых дорогих к самым дешёвым
result = 0 # Беру первые N предметов (самые ценные) и суммирую их
for i in range(N):
    if i < len(positive):
        result = result + positive[i]
print(f'максимально возможную суммарную ценность предметов {result}')
