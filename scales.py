#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Scales.py: Builds the different scale modes from the 12-note chromatic scale.
"""


__author__ = "Sal Bruno"
__copyright__ = "Copyright 2017, Sal Bruno"
__license__ = "MIT"
__version__ = "0.01a"
__status__ = "Prototype"

# The 12 note chromatic scale.
chromatic = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

# Base scale mode
base_mode = [2, 2, 1, 2, 2, 2, 1]  # The "Major" scale.

# Seven modes of the Major scale.
modes = [
    'ionian (Major)',
    'dorian',
    'phrygian',
    'lydian',
    'mixolydian',
    'aeolian (minor)',
    'locrian'
    ]


def is_valid_key(user_key, chrom):
    """
    Checks for valid user input.
    """

    if(len(user_key) != 1 and len(user_key) != 2):
        return False
    elif(user_key not in chrom):
        return False
    else:
        return user_key


def make_new_chrom(scale_key, chrom):
    """
    Rearranges the notes to start on given element.
    """

    new_chrom = chrom[scale_key:] + chrom[:scale_key]
    new_chrom.append(chrom[scale_key])  # Append first note to end of list.

    return new_chrom


key_to_use = input("In which key would you like to work in? >").upper()

while(not is_valid_key(key_to_use, chromatic)):
    print("I'm sorry, that is not valid input.")
    key_to_use = input("In which key would you like to work in? >").upper()

if(is_valid_key(key_to_use, chromatic)):
    new_chromatic = make_new_chrom(chromatic.index(key_to_use), chromatic)

    print(new_chromatic)
