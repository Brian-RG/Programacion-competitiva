# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 21:09:52 2018

@author: brian
"""
k=int(input())
s=sorted(list(map(int,list(input()))))
n=sum(s)
if(k>n):
    counter=0
    for i in s:
        if(n<k):
            n+=9-int(i)
            counter+=1
        else:
            break
    print(counter)
else:
    print("0")