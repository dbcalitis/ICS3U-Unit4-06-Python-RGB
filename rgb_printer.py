#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Oct 2021
# This program is the RGB Printer


def main():
    # This function prints all of the RGB combinations
    # process & output
    for red in range(256):  # red value
        for green in range(256):  # green value
            for blue in range(256):  # blue value
                print("RGB({0},{1},{2})".format(red, green, blue))

    print("\nDone")


if __name__ == "__main__":
    main()
