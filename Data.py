#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 15:02:41 2020

@author: Chad
"""

import Variable
import Expression
import random
import copy

# Stores an instance of the algoBOWL problem. 
#
# order: this array stores all of the Variable objects
# in the order that they were read in.
#
# expressions: This array stores all of the expressions from
# the input
#
# variables: This is a dictionary in the form {"int: Variable"}
# This allows Variable objects to be quickly accessed via their
# name.
# 
# score: int. This stores the total number of clauses that have
# been satisfied.
class Data:
    def __init__(self, fileName):
        self.order = []
        self.expressions = []
        self.variables = {}
        self.score = 0;
        
        f = open(fileName, "r")
        flines = f.readlines()
        
        self.nClauses = flines[0].split()[0]
        self.nVars = flines[0].split()[1]
        
        flines.pop(0)
        found = set()
        
        for i in flines:
            line = [int(j) for j in i.split()]
            negate1 = False
            negate2 = False
            if line[0] < 0: negate1 = True
            if line[1] < 0: negate2 = True
            var1 = Variable.Variable(abs(line[0]), random.randint(0,1))
            var2 = Variable.Variable(abs(line[1]), random.randint(0,1))
            
            if abs(line[0]) not in found:
                self.__addVar(var1, found)
            if abs(line[1]) not in found:
                self.__addVar(var2, found)
                
            clause = Expression.Expression(self.variables[var1.name], self.variables[var2.name], negate1, negate2 )
            self.expressions.append(clause)
            self.variables[var1.name].expressions.append(clause)
            self.variables[var2.name].expressions.append(clause)
        
        self.__updateScore()
        self.order.sort()

    def __addVar(self, var, found):
        self.order.append(var.name)
        self.variables[var.name] = var
        found.add(var.name)
        
    # Loops through the expressions array and counts
    # how many are true.
    def __updateScore(self):
        count = 0;
        for i in self.expressions:
            if i.evaluate():
                count += 1
                    
        self.score = count
     
    # Reads in an output file and checks if it is valid.
    # It stores the claimed number of completed expressions.
    # Then it sets each variable equal to the value dictated
    # in the output file. 
    def verify(self, fileName):
        f = open(fileName, "r")
        flines = f.readlines()
        
        claim = int(flines[0])
        flines.pop(0)
        
        for i in self.order:
            self.variables[i].value = int(flines[0])
            flines.pop(0)
            
        self.__updateScore()
        if self.score == claim:
            return True
        
        return False
    
    #Returns an array with the boolean values of each Variable
    #in order
    def __getState(self):
        state = []
        for i in self.order:
            state.append(self.variables[i].value)
        return state
    
    #Takes in a state array and sets the variables to the values
    def __setState(self, state):
        thisState = copy.deepcopy(state)
        for i in self.order:
            self.variables[i].value = thisState[0]
            thisState.pop(0)
    
    #Tries to improve the score iteratively. It changes one variable
    #and sees if that improves the score, if it does it keeps the
    #change. If not it discards the change. It keeps running until
    #the score stops changing.
    def hillClimb(self):
        for i in self.order:
            self.variables[i].value = random.randint(0,1)
        
        oldScore = 0
        
        while oldScore != self.score:
            
            oldScore = copy.deepcopy(self.score);
            randomOrder = [i for i in self.order]
            random.shuffle(randomOrder)
            
            for i in randomOrder:
                var = self.variables[i]
                localScore = var.localScore()
                var.value = not(var.value)
                if not(localScore < var.localScore()):
                    var.value = not(var.value)
            self.__updateScore()
       
    #Runs the hill climb algorithm over and over again and saves the state
    #of the maximum score. This is to avoid local maxima.
    def optimize(self, iterations):
        state = self.__getState()
        bestScore = self.score
        for i in range(iterations):
            self.hillClimb()
            if self.score > bestScore:
                bestScore = self.score
                state = self.__getState()
        self.__setState(state)
        self.__updateScore()
        
    def printState(self):
        print(self.score)
        state = self.__getState()
        for i in state:
            print(i)
            
    def writeOutput(self, file):
        f = open(file,"w")
        f.write(str(self.score) + "\n")
        
        for i in self.__getState():
            f.write(str(int(i)) + "\n")
        
                    
            
        
        