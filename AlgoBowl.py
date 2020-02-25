#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AlgoBOWL
@author: Chad
"""

from Data import Data
from time import perf_counter

def main():    
    
    skip = {138, 148, 150}
    
    n = 136;
    for i in range(162 - 136 + 1):
        if n in skip:
            n += 1
            continue
        print("\n", "Calculating Output for group " + str(n))
        dataLarge = Data("inputs/input_group" + str(n) + ".txt")
        print("Initial score: ", dataLarge.score)
        start = perf_counter()
        dataLarge.optimize(1)
        end = perf_counter()
        print("Final score: " + str(dataLarge.score))
        print("Calculation time: ", end - start, "\n")
        #dataLarge.writeOutput("outputs/output_from_141_to_" + str(n) + ".txt")
        n += 1
    
    n = 136
    for i in range(162 - 136 + 1):
        inputData = Data("inputs/input_group" + str(n) + ".txt")
        if inputData.verify("outputs/output_from_141_to_" + str(n) + ".txt"):
            print("Output" + str(n) + ": Valid")
        else:
            print("Output" + str(n) + ": Invalid")
        n += 1

main()