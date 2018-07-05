#!/usr/bin/env python3

"""
helpers.py: a helper functions for usage with argparse
"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


import argparse
import os


def get_positive_int(value):
    """
    This function verifies if the input string represents a positive integer
    :param string value: The value to be verified
    :return int:  The positive number represented by the input string
    :raises: argparse.ArgumentTypeError when the input parameter is incorrect
    """
    value = int(value)
    if value <= 0:
        raise argparse.ArgumentTypeError('incorrect value: {} '.format(value))

    return value


def get_dir_path(path):
    """
    This function verifies if the input string is a valid directory path
    :param string path: The path to be verified
    :return string: The absolute path to the directory passed as input
    :raises: argparse.ArgumentTypeError when the path is invalid
    """
    if not os.path.exists(path) or not os.path.isdir(path):
        raise argparse.ArgumentTypeError('"{}" is not a valid directory!'
                                         .format(path))
    if not os.path.isabs(path):
        path = os.path.abspath(path)

    return path


def get_outdir_path(path):
    """
    This function verifies if the path leads to a directory. In case the
    directory does not exist and there is no name conflict with a file, then it
     is created
    :param string path: The path to be verified
    :return string: The absolute path to the directory passed as input
    :raises: argparse.ArgumentTypeError when the directory cannot be created
    """
    if not os.path.exists(path):
        os.makedirs(path)
    elif not os.path.isdir(path):
        raise argparse.ArgumentTypeError('"{}" is a file!'.format(path))

    if not os.path.isabs(path):
        path = os.path.abspath(path)

    return path


if __name__ == '__main__':
    pass
