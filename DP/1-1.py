# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 22:43:45 2021

@author: terad
"""

N,X,Y = map(int,input().split())

As = X
Al = Y
tmp = 0

for _ in range(N-2):
	tmp = (As+Al)%100
	As = Al
	Al = tmp
print(Al)