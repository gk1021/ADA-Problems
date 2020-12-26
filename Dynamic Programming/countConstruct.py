# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 10:09:53 2020

@author: Kunal
"""

def countConstruct(word,letters):
    if word=='':
        return 1
    count=0
    for i in letters:
        if i in word and word.index(i)==0:
            number=countConstruct(word[len(i):], letters)
            if number:
                count+=number
    return count

def countConstructdp(word,letters,di={}):
    if word in di.keys():
        return di[word]
    if word=='':
        return 1
    count=0
    for i in letters:
        if i in word and word.index(i)==0:
            number=countConstructdp(word[len(i):],letters,di)
            if number:
                count+=number
    di[word]=count
    print(di)
    return count

print(countConstruct('happy', ['h','a','pp','i','y','ha','happy']))
print(countConstructdp('happy', ['h','a','pp','i','y','ha','happy']))
        