# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 17:24:18 2021

@author: terad
"""

N = int(input())
T = [0]*(N+1)

T[0] = 1
T[1] = 1

for i in range(2,N+1):
    T[i] = T[i-1] + T[i-2]
    
print(T[N])
