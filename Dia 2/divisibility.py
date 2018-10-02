def _(word):
    aux=set()
    e=t=word
    prev=""
    while(len(e)>6):
        r=e[-2:]
        y=e=e[:-2]
        aux.add(r)
        if(r==prev):
            break
        prev=r
        while(len(y)-3>=5):
            r=y[-3:]
            y=y[:-3]
            aux.add(r)
    while len(t)>7:
        f=t[-3:]
        t=t[:-3]
        c=t
        aux.add(f)
        while(len(c)-2>=5):
            f=c[-2:]
            c=c[:-2]
            aux.add(f)
    return aux
s=input()

if(len(s)<6):
    print(0)
else:
    b=_(s)
    print(len(b))
    for e in b:
        print(e)