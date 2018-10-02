n=int(input())
b=[]
z=[]
ans=""
for e in range(n):
    p,x,y=map(int,input().split())
    if(p==1):
        b.append((x,y))
    else:
        e,r=b[x-1]
        j,k=b[y-1]
        if(j<e<k or j<r<k):
            z.append("YES")
            #ans+="YES\n"
        else:
            z.append("NO")
            #ans+="NO\n"
for x in z:
    print(x)
