# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 12:19:49 2021

@author: lofth
"""

#45 hours at a rate of 10.50 - output 498.75


sh = input("Enter Hours:")
fr = input("Enter Rate:")
try:
    fh = float(sh)
    fr = float(fr)
except:
    print("Error, please enter numeric input")
    quit()
 
print(fh, fr)
if fh > 40:
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
    
else: 
    xp = fh * fr
print("Pay:",xp)
    