#!python3.6
# Copyright © 2016-2017 Petr Vepřek
"""rpUtilities.py"""

import enum

class Color(enum.Enum):
    (
        Red, Green, Blue, # primary
        Cyan, Magenta, Yellow, # secondary
        Orange, Rose, Aqua, Lime, Purple, Indigo # tertiary
    ) = range(12)

def main():
    print("Color =", list(Color))

if '__main__' == __name__:
    main()
