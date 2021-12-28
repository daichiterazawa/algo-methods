# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 17:30:54 2021

@author: terad
"""

N = int(input())
H = [0] * (N+3)
H[1] = 1
H[2] = 2
H[3] = 4

if N >= 4: 
    for n in range(4,N+1):
        H[n] = H[n-1] + H[n-2] + H[n-3]
    
print(H[N])
    
    