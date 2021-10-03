# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]
numbers = [2, -5, 8, 9, -25, 25, 4] # при заполении случайными числами подходящие элементы почти не появлялись
good_numbers = []

i = 0
while i < len(numbers):
    if numbers[i] > 0 and (numbers[i] ** 0.5 - int(numbers[i] ** 0.5) == 0):
        good_numbers.append(int(numbers[i]**0.5))
    i += 1
print(good_numbers)
