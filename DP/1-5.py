# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 17:41:29 2021

@author: terad
"""

N,M = map(int,input().split())
A = list(map(int,input().split()))
T = [0] * N

for i in range(1,N):
    num = 10**9
    for m in range(1,min(M+1,i+1)):
        if num >= m*A[i]+T[i-m]:
            num = m*A[i]+T[i-m]
        T[i] = num

print(T[N-1])
        