# Дано целое число.
# Если оно делится на 3 без остатка - вывести ”Foo”,
# если делится на 5 - вывести “Bar”,
# а если делится на 3 и на 5 - вывести “Foobar”.
# Для всех остальных случаев не выводить ничего.

# TODO: your code here
x = int (input("Enter number "))

if x % 3 == 0 and x % 5 != 0:
    print ("Foo")
if x % 5 == 0 and x % 3 != 0:
    print ("Bar")
if x % 3 == 0 and x % 5 == 0:
    print ("Foobar")
'''
# в случае, если Foobar == FooBar
if x % 3 == 0:
    print ("Foo", end = "")
if x % 5 == 0:
    print ("Bar")
'''
