#!/usr/bin/env python3
"""Car route"""
import math


def main():
    """Main function"""
    km_peer_day = int(input())
    rout_length = int(input())

    print(math.ceil(rout_length / km_peer_day))


if __name__ == '__main__':
    main()
