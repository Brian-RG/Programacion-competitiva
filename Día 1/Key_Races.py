# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 21:34:52 2018

@author: brian
"""

s,v1,v2,t1,t2=list(map(int,input().split(" ")))
f=(s*v1)+(2*t1)
p=(s*v2)+(2*t2)
if(f<p):
    print("First")
elif(p<f):
    print("Second")
else:
    print("Friendship")