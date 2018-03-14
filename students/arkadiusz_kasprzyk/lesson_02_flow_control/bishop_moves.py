"""
title: bishop_moves
author: akasp@interia.pl, arkadiusz.kasprzyk@tieto.com
date: 2018-03-13
description:
    In chess, the bishop moves diagonally, any number of squares.
    Given two different squares of the chessboard,
    determine whether a bishop can go from the first to the second in one move.

    The program receives as input four numbers from 1 to 8,
    specifying the column and row numbers of the starting square
    and the column and row numbers of the ending square.
    The program output YES if a Bishop can go from the first square to the second in one move,
    or NO otherwise.
"""


data = {}  ## input data

for ss in ["start", "stop"]:
    for cr in ["column", "row"]:
        key = "{}_{}".format(ss, cr)
        data[key] = int(input("number of {} {} : ".format(ss, cr)))



if abs(data['start_column'] - data['stop_column']) ==  abs(data['start_row'] - data['stop_row']):
    print('YES')
else:
    print('NO')

input("")
