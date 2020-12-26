# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 14:19:17 2020

@author: Kunal
"""
import copy
def allConstruct(word,letters):
    if word=='':
        return []
    result=[]
    for i in letters:
        
        if i in word and word.index(i)==0:
            lin=allConstruct(word[len(i):], letters)
            if len(lin)==0:
                lin=[[]]
            print(i,lin)
            for j in lin:
                j.append(i)
            #lin.append(i) 
            print(lin)
            result.extend(lin) 
            print(result)
             
    return result

def allConstructdp(word,letters,di={}):
    if word in di.keys():
        return di[word]
    if word=='':
        return []
    result=[]
    for i in letters:
        
        if i in word and word.index(i)==0:
            lin=allConstructdp(word[len(i):], letters)
            if len(lin)==0:
                lin=[[]]
            print(i,lin)
            for j in lin:
                j.append(i)
            #lin.append(i) 
            print(lin)
            result.extend(lin) 
            print(result)
    print('word {} dic {}'.format(word,result))
    di[word]=copy.deepcopy(result)         
    print(di)
    return result


#print(allConstruct('happy', ['h','a','pp','i','y','ha','happy']))
print(allConstructdp('happy', ['h','a','pp','i','y','ha','happy']))
