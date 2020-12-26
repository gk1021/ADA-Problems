# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 17:30:04 2020

@author: Kunal
"""

def hasSum(totalSum,numbers):
    if totalSum==0:
        return []
    if totalSum<0:
        return False
    for i in numbers:
        li1=hasSum(totalSum-i,numbers)
        if type(li1) is type([]):
            li1.append(i)
            return(li1)
        
    return False

di={}
def hasSumDP(totalSum,numbers):
    if totalSum in di.keys():
        return di[totalSum]
    if totalSum==0:
        return []
    if totalSum<0:
        return False
    for i in numbers:
        li1=hasSumDP(totalSum-i,numbers)
        if type(li1) is type([]):
            li1.append(i)
            di[totalSum]=li1
            return(di[totalSum])
        
    return False

li2=hasSum(760,[2,5,3,4])
print(li2)
li2=hasSumDP(760,[2,5,4,3])
print(li2)



#m=3
#li=list(map(int,input().split(','*int(input()))))
#print(li)

