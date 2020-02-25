#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 14:26:19 2020

@author: Chad
"""
#This class stores a boolean variable
#One variable object exists per unique
#variable in the problem. The variable
#name is stored as an int and it's 
#value is stored as a bool. The variable
#stores all the expressions that it is
#a part of.
class Variable:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.expressions = []
        
    def addExpression(self, expression):
        self.expressions.append(expression)
        
    def localScore(self):
        count = 0
        for i in self.expressions:
            if i.evaluate():
                count += 1
        return count