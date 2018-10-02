import operator
n=int(input())
s=input()
d=n%4
if(d):
    print("===")
else:
    q=s.count("?")
    a=s.count("A")
    g=s.count("G")
    c=s.count("C")
    t=s.count("T")
    if a==g==c==t and not q: print(s)
    else:
        aux=["A","G","C","T"]
        au=[]
        dic={"A":0,"G":0,"C":0,"T":0}
        for e in dic:
            dic[e]=s.count(e)
        prev=dic[max(dic.items(), key=operator.itemgetter(1))[0]]
        for f in range(0,len(dic)):
            tmp=max(dic.items(), key=operator.itemgetter(1))[0]
            c=dic[tmp]
            if(c==prev):
                del dic[tmp]
                au.append(tmp)
            else:
                break
        if(len(au)==len(aux)):
            for o in range(0,n):
                s=s.replace("?",aux[o%len(aux)],1)
            print(s)
        else:
            for e in au:
                aux.remove(e)
            if(len(au)>1):
                for p in range(0,len(au)):
                    s=s.replace("?",au[p%len(au)],1)
            q=s.count("?")
            if(q%len(aux)):
                print("===")
            else:
                for i in range(1,q+1):
                    s=s.replace("?",aux[i%len(aux)],1)
                print(s)
