# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 21:51:15 2021

@author: terad
"""

N = int(input())
dp = [[0]*(N+2) for _ in range(N)]
dp[0][1:N+1] = list(map(int,input().split()))

for i in range(1,N):
	for j in range(1,N+1):
		dp[i][j] += dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]
		dp[i][j] %= 100

print(dp[N-1][N]) 