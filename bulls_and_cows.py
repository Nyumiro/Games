from random import choice

#БЫКИ И КОРОВЫ

z = '0123456789'
x = choice(z)
for i in range(3):
    z = ''.join(j for j in z if j != x[i])
    x += choice(z)
print(x)  # выводим загаданное программой число в целях отладки.
print('Число загадано.')
enter = 0

while x != enter:
    enter = input('Введите четыре цифры: ')
    if not enter.isnumeric() or not len(enter) == 4:
        print('Неподходящий формат. Пожалуйста, введите 4 цифры.')
        continue
    oxCount = 0
    cowCount = 0
    if x[0] == enter[0]:
        oxCount += 1
    elif enter[0] in x:
        cowCount += 1
    if x[1] == enter[1]:
        oxCount += 1
    elif enter[1] in x:
        cowCount += 1
    if x[2] == enter[2]:
        oxCount += 1
    elif enter[2] in x:
        cowCount += 1
    if x[3] == enter[3]:
        oxCount += 1
    elif enter[3] in x:
        cowCount += 1

    print(f"Количество быков: {oxCount}, количество коров: {cowCount}")

print('Вы выиграли.')