#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:06:13 2020

@author: Chad
"""

import random

def main():
    n = 1000
    m = 50000
    
    f = open("GeneratedInput.txt","w")
    f.write("x y" + "\n")
    
    for i in range(m):
        x1 = random.randint(1,n)
        x2 = random.randint(1,n)
        while x1 == x2:
            x2 = random.randint(1,n)
            
        if(random.randint(0,1) == 1):
            x1 *= -1
        if(random.randint(0,1) == 1):
            x2 *= -1
            
        lineOut = str(x1) + " " + str(x2) + "\n"
        f.write(lineOut)
    
main()

