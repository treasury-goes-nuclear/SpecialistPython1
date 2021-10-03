# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here
name_length = 0
name_position = 0
i = 0
n = len(names)
while i < n:
    if name_length <= len(names[i]):
        name_length = len(names[i])
        name_position = i
    i += 1

print(names[name_position])
