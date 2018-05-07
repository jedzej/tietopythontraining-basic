#!/usr/bin/env python3
"""Swap min and max exercise"""


def main():
    """Main function"""
    nums = [int(n) for n in input().split()]

    idx_max = 0
    idx_min = 0

    for idx, val in enumerate(nums):
        if val > nums[idx_max]:
            idx_max = idx
        if val < nums[idx_min]:
            idx_min = idx

    nums[idx_max], nums[idx_min] = nums[idx_min], nums[idx_max]

    print(' '.join([str(item) for item in nums]))


if __name__ == '__main__':
    main()
