# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 21:17:11 2021

@author: terad
"""

N,M = map(int,input().split())
D = set(map(int,input().split()))
#到達果報なマスには1
X = [0] * (N+1)
X[0] = 1

for n in range(1,N+1):
	for d in D:
		if  n >= d:
			if X[n-d] == 1:
				X[n] = 1
print('Yes' if X[N] == 1 else 'No')