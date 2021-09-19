# Дан треугольник со сторонами a, b и c. Определите, является ли он равнобедренным.
# Формат входных данных: дано три натуральных числа. Гарантируется, что отрезки с данными длинами образуют треугольник.
# Формат выходных данных: Выведите «YES», если треугольник равнобедренный, и «NO» в противном случае.

# TODO: your code here
x = int (input("Enter edge 1 length "))
y = int (input("Enter edge 2 length "))
z = int (input("Enter edge 3 length "))
if x == y or y == z:
    print ("Yes")
elif x == z:
    print ("Yes")
else:
    print ("No")
