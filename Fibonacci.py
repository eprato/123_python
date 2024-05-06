# -*- coding: utf-8 -*-
"""
Created on Sun May  5 22:31:14 2024

@author: P077328
"""

import sys

def main():
    n0 = 0
    n1 = 1
    swap = 1
#    result = 0
#    i = 0
    i_max = 0
    largest_n = 500
    

    print("ENTER N TO GENERATE THE FIBONACCI SEQUENCE")
    i_max = int(input())

    if i_max > largest_n:
        print("INVALID N VALUE. THE PROGRAM WILL NOW END")
        sys.exit()
    elif i_max > 2:
        case_greater_than_2(n0, n1, swap, i_max)
    elif i_max == 2:
        case_2(n0, n1, swap)
    elif i_max == 1:
        case_1(n0, n1)
    elif i_max == 0:
        case_0(n0)
    else:
        print("INVALID N VALUE. THE PROGRAM WILL NOW END")
        sys.exit()

    print("THE PROGRAM HAS COMPLETED AND WILL NOW END")

def case_0(n0):
    result = n0
    print(result)

def case_1(n0, n1):
    case_0(n0)
    result = n1
    print(result)

def case_2(n0, n1, swap):
    case_1(n0, n1)
    result = n1
    print(result)

def case_greater_than_2(n0, n1, swap, i_max):
    case_1(n0, n1)
    for i in range(1, i_max):
        swap = n0 + n1
        n0 = n1
        n1 = swap
        result = swap
        print(result)

if __name__ == "__main__":
    main()

