# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 01:36:09 2022

@author: salva


Problem:
    
    Write a Python module that computes the number of steps required for the sequence to get 'down to 1.'

Given any positive integer, n at each step do this:

   If n is odd replace n with 3*n+1

  if n is even, replace n with n/2

for example if n =11 the the sequence is  11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1 .... it took 14 steps

print out the number of steps required for the integers 5 through 20
"""

import numpy as np

count = []

for n in range(5, 21):
    numberOfSteps = 0
    while n !=1:
        if (n % 2) == 0:
            n = n / 2
            print('{},' .format(n))
            numberOfSteps = numberOfSteps + 1
        else:
            n = 3 * n + 1
            print('{}, ' .format(n))
            numberOfSteps = numberOfSteps + 1
    print(numberOfSteps)
    count.append(numberOfSteps)
    print(count)

            
    
