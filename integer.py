#!/usr/bin/envpython3
# Created By:Deepak
# Date: 10/19/2026
# This program asks the user to input an integer if it's positive, negative or a zero

import math


def main():

    num = int(input("Enter a integer: "))

    if num > 0:
        print("Number is positive")
    elif num < 0:
        print("Number is negative")
    else:
        print("Number is zero")


if __name__ == "__main__":
    main()
