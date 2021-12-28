# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 21:38:06 2021

@author: terad
"""

A = list(map(int,input().split()))
dp = [[0] * len(A) for _ in range(len(A))]
dp[0] = A

for i in range(1,len(A)):
	for j in range(len(A)):
		if 1<=j:
			dp[i][j] += dp[i-1][j-1]

		dp[i][j] += dp[i-1][j]

		if j<=len(A)-2:
			dp[i][j] += dp[i-1][j+1]
print(dp[-1][-1])