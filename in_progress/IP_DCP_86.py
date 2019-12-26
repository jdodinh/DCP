"""
Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0, using only mathematical or bit operations.
You can assume b can only be 1 or 0.

"""

import numpy as np


def main():
    x = 86
    y = 99
    b = 0
    answer = (y & (0xffff + b)) + ((0xffff + b) | x)
    print(answer)


if __name__=="__main__":
    main()
