#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Sep. 23, 2022
# This program calculates the circumference
# of a circle with user input & tau


import math


def main():
    # input
    print("This program calculates the")
    print("circumference of a circle with tau.")
    print("")
    radius = int(input("Enter the radius in cm: "))

    # process
    T = 6.28
    circumference = T * radius

    # output
    print("")
    print("Circumference = {}cm".format(circumference))


if __name__ == "__main__":
    main()
