# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 12:15:16 2018

@author: brian
"""
seq=[]
n,a,b,k=(int(x) for x in input().split(" "))
for c in input():
    seq.append(c+"1")
#n,a,b,k=va0
'''
if(n+1>k):
    for e in range(n+1-k):
        seq.append("-1")
'''
s=0
f=(10**9)+9
for i in range(n+1):
    if(i<len(seq)):
        s+=int(seq[i])*(a**(n-i)*b**(i))
    else:
        s+=int((-1)*(a**(n-i)*b**(i)))
print(abs(s%f))