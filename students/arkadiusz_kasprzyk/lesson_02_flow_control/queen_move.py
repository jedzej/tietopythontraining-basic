"""
title: queen_moves
author: akasp@interia.pl, arkadiusz.kasprzyk@tieto.com
date: 2018-03-13
description:
    Chess queen moves horizontally, vertically or diagonally to any number of cells.
    Given two different cells of the chessboard, determine whether a queen
    can go from the first cell to the second in one move.

    The program receives the input of four numbers from 1 to 8,
    each specifying the column and row number,
    first two - for the first cell, and then the last two - for the second cell.
    The program output YES if a queen can go from the first cell to the second in one move,
    or NO otherwise.
"""

data = {}  ## input data

for ss in ["start", "stop"]:
    for cr in ["column", "row"]:
        key = "{}_{}".format(ss, cr)
        data[key] = int(input("number of {} {} : ".format(ss, cr)))

col_diff = abs(data['start_column'] - data['stop_column'])
row_diff = abs(data['start_row'] - data['stop_row'])

if col_diff == row_diff or col_diff == 0 or row_diff == 0:
    print('YES')
else:
    print('NO')

input("")