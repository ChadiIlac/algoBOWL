#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 09:14:31 2020

@author: Chad
"""

import copy

#This represents a clause in the problem.
#One expression exists per clause in the 
#problem. 
class Expression:
    def __init__(self, var1, var2 , negate1, negate2):
        self.var1 = var1
        self.var2 = var2
        self.negate1 = negate1
        self.negate2 = negate2
        
    def evaluate(self):
        """Evaluates the expression. If either
        variable are supposed to be negated they
        are set to their opposite value, then the
        or statement is returned"""
        
        val1 = copy.deepcopy(self.var1.value)
        val2 = copy.deepcopy(self.var2.value)
        if self.negate1:
            val1 = not(val1)
        if self.negate2:
            val2 = not(val2)
            
        return val1 or val2
            