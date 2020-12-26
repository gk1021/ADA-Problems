# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 14:25:35 2020

@author: Kunal
"""
import copy

def beatSum(totalSum,numbers):
    if totalSum==0:
        return []
    if totalSum<0:
        return False
    shortestList=[]
    for i in numbers:
        li1=beatSum(totalSum-i,numbers)
        if type(li1) is type([]):
            li1.append(i)
            #print(li1)
            if len(shortestList)>len(li1) or len(shortestList)==0:
                shortestList=copy.deepcopy(li1)    
    return shortestList

di={}
def beatSumDP(totalSum,numbers):
    if totalSum in di.keys():
        return di[totalSum]
    if totalSum==0:
        return []
    if totalSum<0:
        return False
    shortestList1=False
    for i in numbers:
        li1=beatSumDP(totalSum-i,numbers)
        if type(li1) is type([]):
            li1.append(i)
            if not shortestList1 or len(shortestList1)>len(li1):
                print('before {}'.format(shortestList1))
                shortestList1=copy.deepcopy(li1)
                print('after {}'.format(shortestList1))
    if shortestList1:    
        di[totalSum]=copy.deepcopy(shortestList1)
    else:
        di[totalSum]=False
    return shortestList1

li2=beatSum(5,[2,5,3,4,25])
print(li2)
li2=beatSumDP(100,[2,3,5,25])
print(li2)




