import string 
b,s=map(int,input().split())
a=""
c=0
for e in range(b):
    f=input()
    for i in range(0,len(f)):
        t=f[i:]
        l=t[0]
        if l in string.ascii_lowercase:
            wo=(string.ascii_lowercase[((string.ascii_lowercase.index(l)-s+26)%26)])
            t=t.replace(l,wo,1)
        elif l in string.ascii_uppercase:
            wo=(string.ascii_uppercase[((string.ascii_uppercase.index(l)-s+26)%26)])
            t=t.replace(l,wo,1)
        a+=t[0]
    a+="\n"
print(a)
