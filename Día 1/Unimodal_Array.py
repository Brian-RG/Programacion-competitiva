# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 20:04:04 2018
@author: brian
"""

n=int(input())
b=list(map(int,input().split(" ")))
s=""
if not (len(b)-1):
    print("Yes")
else:
    for i in range(1,n):
        if s=="":
            if(b[i]>b[i-1]):
                s="a"
            elif(b[i]==b[i-1]):
                s="r"
            else:
                #print("No")
                s="d"
        elif s=="a":
            if(b[i]==b[i-1]):
                s="r"
            elif(b[i]<b[i-1]):
                #print("No")
                s="d"
        elif s=="r":
            if(b[i]<b[i-1]):
                s="d"
            elif(b[i]==b[i-1]):
                continue
            else:
                #print("No")
                s="f"
                break
        elif s=="d":
            if(b[i]<b[i-1]):
                continue
            else:
                s="f"
                break
            
    print("Yes" if not(s=="f") else "No")        