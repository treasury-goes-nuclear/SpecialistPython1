# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

# TODO: your code here
import random
n = 10
list = []
i = 0

while i < n:
    list.append(random.randint(-10, 10))
    i += 1

s = 0
for el in list:
    if el > 0:
        s += el
print(list) # проверка
print(s)
