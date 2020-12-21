# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 18:41:24 2020
Fibonaci ADA with DP,Recursion and Iteration
@author: Kunal
"""

import time

#Recursion
def fib_rec(value):
    if value==1:
        return 0
    if value==2:
        return 1
    return (fib_rec(value-1)+fib_rec(value-2))


#DP
dp={}
def fib_dp(value):
    if value in dp.keys():
        return dp[value]
    if value==1:
        return 0
    if value==2:
        return 1
    dp[value]=(fib_dp(value-1)+fib_dp(value-2))
    return dp[value]


#Iterative
def fib_it(value):
    li=[0,1]
    if value==1:
        return 0
    if value==2:
        return 1
    for i in range(2,value):
        li.append(li[i-1]+li[i-2])
    return li[value-1]

start = time.process_time()
print(fib_rec(40))
print(time.process_time() - start)

start = time.process_time()
print(fib_dp(40))
print(time.process_time() - start)

start = time.process_time()
print(fib_it(40))
print(time.process_time() - start)

