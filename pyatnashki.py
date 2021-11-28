from random import random

# ПЯТНАШКИ


desk = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]


def print_desk(desk):
    for row in desk:
        rez = ''
        for cell in row:
            rez += '\t' + ('_' if cell == 0 else str(cell))
        print(rez)


marks = [i for i in range(0, 16, 1)]

for i in range(4):
    for j in range(4):
        item = marks[round(random() * (len(marks) - 1))]
        desk[i][j] = item
        marks.remove(item)


def makeStep():
    for i in range(4):
        for j in range(4):
            if desk[i][j] == step:
                if i + 1 < 4 and desk[i + 1][j] == 0:
                    desk[i + 1][j] = step
                    desk[i][j] = 0
                    return True
                elif i - 1 >= 0 and desk[i - 1][j] == 0:
                    desk[i - 1][j] = step
                    desk[i][j] = 0
                    return True
                elif j + 1 < 4 and desk[i][j + 1] == 0:
                    desk[i][j + 1] = step
                    desk[i][j] = 0
                    return True
                elif j - 1 >= 0 and desk[i][j - 1] == 0:
                    desk[i][j - 1] = step
                    desk[i][j] = 0
                    return True
                else:
                    return False


step_count = 0

while True:
    print_desk(desk)
    print(f"Количество ходов: {step_count}")
    step = input('Введите номер фишки: ')
    if not step.isnumeric():
        print('Неподпустимый ход. Введите цифры.')
        continue
    step = int(step)
    if not (1 <= step <= 15):
        print('Номер фишки находится в диапазоне 1...15.')
        continue
    if not makeStep():
        print('Недопустимый ход, рядом с выбранной фишкой нет свободных клеток.')
        continue
    step_count += 1
    new_desk = desk[0] + desk[1] + desk[2] + desk[3]
    game_over = True
    for i in range(1, 15, 1):
        if not new_desk[i - 1] == i:
            game_over = False
    if game_over:
        print(f'Игра закончена. Количество ходов: {step_count}.')
        break

print_desk(desk)
