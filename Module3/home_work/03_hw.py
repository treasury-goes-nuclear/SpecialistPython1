# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
import random
numbers = []
n = 11
i = 0 # counter
while i < n:
    numbers.append(random.randint(-100, 100))
    i += 1
print(numbers) # to check result
i = 0
s = 0 # sum
while i < n:
    if numbers[i] > 0 and numbers[i] % 2 == 0:
        s = s + numbers[i]
    i += 1
print(s)
