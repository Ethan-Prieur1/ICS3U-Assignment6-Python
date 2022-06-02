#!/usr/bin/env python3

# Created by Ethan Prieur
# Created on May 2022
# This is a program that finds the area of a triangle


def calculate_area(base1, base2, height):
    # Calculate area

    # Process
    area = (base1 + base2) / 2 * height

    # Output
    print("The area of the trapezoid is {0} cm²".format(area))


def main():
    # This is the main function

    # Input
    user_base1 = input("Enter The 1st Base of the trapezoid (cm): ")
    user_base2 = input("Enter The 2nd Base of the trapezoid (cm): ")
    user_height = input("Enter Height of the trapezoid (cm): ")
    print("")

    # Process
    try:
        height_int = int(user_height)
        base1_int = int(user_base1)
        base2_int = int(user_base2)
        # Call Functions
        calculate_area(base1_int, base2_int, height_int)
    except Exception:
        print("That's not an integer pal.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
