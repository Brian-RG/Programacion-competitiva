"""
Created on Mon Sep 24 12:10:05 2018

@author: BrianRG
"""

def weird(a,b):
    if(not a or not b):
        return (a,b)
    if(a>=2*b):
        a%=(2*b)
        return weird(a,b)
    if(b>=2*a):
        b%=(2*a)
        return weird(a,b)
    return(a,b)
"""  
def weirdo(a,b):
    while(a and b):
        if(a>=2*b):
            a%=(2*b)
        if(b>=2*a):
            b%=(2*a)
        else:
            if(a>=2*b):
                a-=2*b
                continue
            break
    return a,b
"""
a,b=input().split(" ")
a,b=weird(int(a),int(b))
print(a,b)