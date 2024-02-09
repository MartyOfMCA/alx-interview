#!/usr/bin/python3
"""
Define an implementation to the
N-Queen's problem.
"""
from sys import (
        argv,
        exit
        )


if (__name__ == "__main__"):
    if (len(argv) != 2):
        print("Usage: nqueens N")
        exit(1)

    N = argv[1]
    try:
        N = int(N)
        if (N < 4):
            print("N must be at least 4")
            exit(1)
    except ValueError:
        print("N must be a number")
        exit(1)
