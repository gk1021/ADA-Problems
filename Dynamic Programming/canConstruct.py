# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 09:54:48 2020

@author: Kunal
"""

def canConstruct(word,letters):
    if word=='':
        return True
    for i in letters:
        if i in word and word.index(i)==0:
            if canConstruct(word[len(i):], letters):
                return True
    return False

def canConstructdp(word,letters,Created='',di={}):
    if word in di.keys():
        return di[word]
    if word=="":
        return True
    for i in letters:
        if i in word and word.index(i)==0:
            if canConstructdp(word[len(i):], letters,di):
                di[word]=True
                return True
    di[word]=False
    print(di)
    return False



print(canConstruct('happy', ['h','a','pp','i','y']))
print(canConstructdp('happy', ['h','a','pp','i','y']))
        

