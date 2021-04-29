#!/usr/bin/env/ python3

# Created by Malcolm Tompkins
# Created on April 28, 2021
# Calculates the cost of pizza with user input diameter
import constants


def main():
    # Function that calculates cost of pizza
    diameter = int(input("Input the diameter of pizza (inch): "))
    # User input
    subtotal = constants.MATS * diameter + constants.LABOR + constants.RENT
    total = subtotal + (subtotal * constants.HST)
    # Process
    print("The cost for a {0} inch pizza: ${1:,.2f}".format(diameter, total))
    # Output


if __name__ == "__main__":
    main()
