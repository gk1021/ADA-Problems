# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 19:14:35 2020

@author: Kunal
"""
import time

#Recursion
def traversal_grid(n,m):
    s=0
    if n==0 or m==0:
        return 0
    if n==1 and m==1:
        return 1
    s+=traversal_grid(n-1, m)
    s+=traversal_grid(n, m-1)
    return s

#DP
di={}
def traversal_grid_dp(n,m):
    if (n,m) in di.keys():
        return di[(n,m)]
    if n==0 or m==0:
        return 0
    if n==1 and m==1:
        return 1
    di[(n,m)]=0
    di[(n,m)]+=traversal_grid_dp(n-1, m)
    di[(n,m)]+=traversal_grid_dp(n, m-1)
    #print(di)
    return di[(n,m)]
 
start = time.process_time()
print(traversal_grid(10, 10))
print(traversal_grid(1, 1))
print(traversal_grid(4, 0))
print(traversal_grid(2, 3))
print(time.process_time() - start)

start = time.process_time()
print(traversal_grid_dp(10, 10))
print(traversal_grid_dp(1, 1))
print(traversal_grid_dp(4, 0))
print(traversal_grid_dp(2, 3))
print(time.process_time() - start)
