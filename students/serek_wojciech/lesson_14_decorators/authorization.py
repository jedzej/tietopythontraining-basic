#!/usr/bin/env python3
"""Helper authorization script"""


class Access:
    """"Access class"""
    __access_counter = -1

    def __init__(self):
        pass

    @staticmethod
    def has_access():
        """Give access every 3rd run"""
        Access.__access_counter += 1
        if Access.__access_counter > 2:
            Access.__access_counter = 0
        return not Access.__access_counter
