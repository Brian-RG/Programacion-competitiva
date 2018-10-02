import string 
a,s=map(int,input().split())
a=""
c=0
while(1):
    t=input()
    if(len(t)):
        for i in t:
            t=t[c:]
            if(i in string.ascii_lowercase):
                wo=(string.ascii_lowercase[((string.ascii_lowercase.index(i)-s+26)%26)])
                t=t.replace(i,wo,1)
            elif(i in string.ascii_uppercase):
                wo=string.ascii_uppercase[((string.ascii_uppercase.index(i)-s+26)%26)]
                t=t.replace(i,wo,1)
            c+=1
            if(len(t)):
                a+=t[0]
        a=a+"\n"
    else:
        break
print(a)
    