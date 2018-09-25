# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 19:47:53 2018

@author: brian
"""

a=int(input())
b=list(map(int,input().split(" ")))
ans="Yes" if a%2 and b[0]%2 and b[-1]%2 else "No"
print(ans)