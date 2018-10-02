x=int(input())
mod=1e7
ans={}
for e in range(x):
    f=int(input())
    ans[(pow(2,(f//3)-1,int(mod)))]=1
for i in ans:
    print(i)