# -*- coding: utf-8 -*-
"""
Created on Mon May 11 16:11:38 2020

@author: Tanmay Dave
"""


import string

def stripped_text(a_file):
    new_text = []
    fin = open(a_file)

    for line in fin:
        stripped_line = line.lower().translate(string.maketrans("",""), string.punctuation).split()
        new_text += stripped_line
    return new_text