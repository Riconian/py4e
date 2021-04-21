# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 12:20:21 2021

@author: lofth
"""


score = input("Enter Score: ")
try:
    a = float(score)
    if a >= 0.9:
            print("A")
    elif a >= 0.8:
            print("B")
    elif a >= 0.7:
            print("C")
    elif a >= 0.6:
            print("D")
    elif a < 0.6:
            print("E")
except:
    print("Please enter a valid score")
    quit()
