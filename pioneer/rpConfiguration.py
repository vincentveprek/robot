#!python3.6
# Copyright © 2016-2017 Petr Vepřek
"""rpConfiguration.py"""

gpio = {
    'Buzzer': 12,
    'Red LED': 16,
    'Yellow LED': 20,
    'Green LED': 21
}

def main():
    print("Configuration")
    print("gpio =", gpio)

if '__main__' == __name__:
    main()
