n=int(input());s=input()
if(n%4):print("===")
else:
    m=n//4;q,a,g,c,t = [s.count(x) for x in '?AGCT']
    for x,y in zip("AGCT", [a,g,c,t]):s=s.replace("?",x,m-y)
    print(s if s.count("A")==s.count("G")==s.count("C")==s.count("T") else "===")


n, p, q = list(map(int,input().split()))
s = input()
f=False
for i in range(len(s)//p+1):
    r = p*i
    if (len(s)-r)%q==0 and (len(s)-r)//q>0:

        f=True
        c=0
        print(i+(len(s)-r)//q)
        for i in range(1,i+1):
            print(s[c:c+p])
            c+=p
        for i in range(1,len(s)-r//q+1):
            print(s[c:c+q])
            c+=q
        break
    if len(s)%p==0:
        f = True
        print(len(s)//p)
        print(*[s[i:i+p] for i in range(0,len(s),p)],sep='\n')
        break
    if len(s)%q==0:
        f = True
        print(len(s)//q)
        print(*[s[i:i+q] for i in range(0,len(s),q)],sep='\n')
if not f:
    print(-1)
