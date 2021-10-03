# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.

# TODO: your code here
import random
n = 10
list = []
i = 0
s = 0
while i < n:
    list.append(random.randint(-10, 10))
    i += 1
for el in list:
    s += el
print(list) # проверка
print(s)
