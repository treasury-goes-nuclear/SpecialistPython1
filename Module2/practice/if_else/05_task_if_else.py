# Дано целое число m, задающее номер месяца года.
# Выведите строку — название времени года, соответствующего данному месяцу.
# Формат входных данных: дано целое число m (1 ≤ m ≤ 12).
# Формат выходных данных: требуется вывести название времени года

x = int (input("Enter month number "))

if x <= 2 or x == 12:
    print ("Winter")
elif x >= 3 and x <= 5:
    print ("Spring")
elif x >= 6 and x <= 8:
    print ("Summer")
elif x >= 9 and x <= 10:
    print ("Autumn")
else:
    print ("Sum Tin Wrong")
