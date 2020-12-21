# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 11:50:12 2020
#checksum problem
here you have given array of numbers and totalsum. Your goal is to find if you
can reach to total sum by adding value of array. one can use number in array multiple times
ex 
totalsum = 4
array= [1,2]
ans - yes. 2+2=4
totalsum=9
array= (2,8)
ans- False
@author: Kunal
"""
import time
#recursive approach
def canSum(totalsum,numbers):
    if totalsum==0:
        return True
    elif totalsum<0:
        return False
    for i in numbers:
        result=canSum(totalsum-i,numbers)
        if result:
            return True
    return False

#dp
di={}
def canSumdp(totalsum,numbers):
    
    if totalsum in di:
        return di[totalsum]
    if totalsum==0:
        return True
    elif totalsum<0:
        return False
    for i in numbers:
        result=canSumdp(totalsum-i,numbers)
        di[totalsum]=result
        #print(di)
        if result:
            return True
    return False
start=time.time()
print(canSum(360,[7,14]))
print(time.time()-start)
start=time.time()
print(canSumdp(3600,[7,14]))
print(time.time()-start)
