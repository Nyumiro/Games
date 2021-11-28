# КРЕСТИКИ-НОЛИКИ

desk = [['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']]

player = 'x'
is_winner = False
play_a_draw = False


def print_desk(desk):
    for row in desk:
        str = '\t'.join(row)
        print(str)


while not is_winner:
    print_desk(desk)
    print(f'Ходит игрок {player}. Введите позицию хода в формате [row, column].')
    step = input()
    i = step.split(',')

    if len(i) != 2:
        print('Недопустимый ход. Введите ровно два числа.')
        continue
    if not i[0].isnumeric() or not i[1].isnumeric():
        print('Неподпустимый ход. Введите цифры.')
        continue

    row, column = int(i[0]) - 1, int(i[1]) - 1

    if row < 0 or row > 2 or column < 0 or column > 2:
        print('Неподпустимый ход. Позиция вне границ игрового поля.')
        continue

    if desk[row][column] != '-':
        print(f'Неподпустимый ход. Позиция занята символом {desk[row][column]}.')
        continue

    desk[row][column] = player

    for j in range(3):
        if desk[0][j] == desk[1][j] == desk[2][j] and desk[0][j] != '-':
            is_winner = True
            break
        elif desk[j][0] == desk[j][1] == desk[j][2] and desk[j][0] != '-':
            is_winner = True
            break
        elif (desk[0][0] == desk[1][1] == desk[2][2] or desk[0][2] == desk[1][1] == desk[2][0]) and desk[1][1] != '-':
            is_winner = True
            break

    if not '-' in desk[0] and not '-' in desk[1] and not '-' in desk[2]:
        print('Игра окончена. Ничья.')
        break

    if not is_winner:
        player = '0' if player == 'x' else 'x'
    else:
        print(f'Игра окончена. Победил {player}')

print_desk(desk)