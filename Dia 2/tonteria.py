# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 13:54:14 2018

@author: brian


def freq_listing(word):
    frequency={}
    for c in word:
        if c in frequency:
            if c==" ":
                pass
            else:
                frequency[c]+=1
        else:
            if c==" ":
                pass
            else:
                frequency[c]=1
    return frequency


def main():
    palabra=input("Introduce una palabra:")
    print(freq_listing(palabra))

if __name__=="__main__":
    main()
from math import factorial
n,ans,s = int(input()),1,0
for i in range(n) :
  a = int(input())
  ans=(ans*factorial(s+a-1)//factorial(s)//factorial(a-1))%1000000007
  s+=a
print(ans)
"""

a,b=map(int,input().split())
if b%a:
    print(0)
else:
    c=b//a
    d=set()
    for i in range(1,int(pow(c,0.5)+1)):
        if c%i==0:
            d.add(i)
            d.add(c//i)
    d=sorted(list(d))
    f=d[::]
    for i in range(len(f)):
        f[i]=pow(2,d[i]-1,M)
        for j in range(i):
            if d[i]%d[j]==0:
                f[i]-=f[j]
    print(f[-1]%M)