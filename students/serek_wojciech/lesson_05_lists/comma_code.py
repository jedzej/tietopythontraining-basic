#!/usr/bin/env python3
"""Coma code exercise"""


def comma_code(param):
    """Create string from list"""
    if not param:
        return ''
    elif len(param) == 1:
        return param[0] + ', '

    res = ''
    for i in range(len(param) - 1):
        res += param[i] + ', '
    res += 'and ' + param[-1]
    return res
