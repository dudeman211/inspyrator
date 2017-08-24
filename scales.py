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

# Scale Modes
ionian = [2, 2, 1, 2, 2, 2, 1]  # The "Major" scale.


def make_new_chrom(scale_key, a_chrom):
    """
    Rearranges the notes to start on given element.
    """

    new_chrom = a_chrom[scale_key:] + a_chrom[:scale_key]
    new_chrom.append(a_chrom[scale_key])  # Append first note to end of list.

    return new_chrom

key_to_use = input("In which key would you like to work in? >").upper()
new_chromatic = make_new_chrom(chromatic.index(key_to_use), chromatic)

print(new_chromatic)
