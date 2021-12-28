# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 17:18:10 2021

@author: terad
"""
N = int(input())
A = list(map(int,input().split()))
T = [0] * N
T[0] = 0
T[1] = A[1]

for n in range(2,N):
    T[n] = min(T[n-1]+A[n], T[n-2]+2*A[n])

print(T[N-1])
