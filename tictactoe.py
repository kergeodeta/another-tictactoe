#! /usr/bin/python3
# -*- coding: utf-8 -*-

import os


def start():
    return [
        [' '] * 3,
        [' '] * 3,
        [' '] * 3,
    ]


def draw_table(table):
    os.system('clear')
    print('   |   |   ')
    print(f' {table[0][0]} | {table[0][1]} | {table[0][2]} ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(f' {table[1][0]} | {table[1][1]} | {table[1][2]} ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(f' {table[2][0]} | {table[2][1]} | {table[2][2]} ')
    print('   |   |   ')
    print('')


def get_player():
    usr_input = input('Choose your weapon! ')
    if len(usr_input) and usr_input in ['x', 'o']:
        return usr_input
    else:
        return False


def get_position():
    usr_input = input('Position: ')
    if len(usr_input) == 1 and usr_input.isdigit():
        pos = int(usr_input)

        if 0 < pos <= 3:
            return {'x': 0, 'y': pos - 1}
        elif 3 < pos <= 6:
            return {'x': 1, 'y': pos - 4}
        elif 6 < pos <= 9:
            return {'x': 2, 'y': pos - 7}
        else:
            return False
    else:
        return False


def toggle_player(player):
    if player == 'x':
        return 'o'
    else:
        return 'x'


def has_winner(table):
    res = False

    i = 0
    while i < len(table) and not res:
        res = res or table[i][0] == table[i][1] == table[i][2] != ' '
        i += 1

    i = 0
    while i < len(table) and not res:
        res = res or table[0][i] == table[1][i] == table[2][i] != ' '
        i += 1

    return res or table[0][0] == table[1][1] == table[2][2] != ' ' or table[0][2] == table[1][1] == table[2][0] != ' '


def play(table):
    play = True
    turn = 0
    current_player = ''

    while not current_player:
        current_player = get_player()

    while play and turn < 9:
        draw_table(table)

        is_free = True
        while is_free:
            pos = get_position()
            is_free = not table[pos['x']][pos['y']] == ' '
            if is_free:
                print('This place is already occupied!')

        table[pos['x']][pos['y']] = current_player

        play = not has_winner(table)
        turn += 1
        draw_table(table)

        if not play:
            print(f'\nThe winner is: {current_player}\n\n')
        current_player = toggle_player(current_player)


if __name__ == '__main__':
    table = start()
    play(table)
