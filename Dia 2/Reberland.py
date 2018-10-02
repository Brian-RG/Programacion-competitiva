def _(word):
    aux={}
    e=t=word
    prev=""
    while(len(e)>6):
        r=e[-2:]
        y=e=e[:-2]
        if r not in aux:
            aux[r]=1
        elif(r==prev):
            break
        prev=r
        while(len(y)-3>=5):
            r=y[-3:]
            y=y[:-3]
            if(r not in aux):
                aux[r]=1
    while len(t)>7:
        f=t[-3:]
        t=t[:-3]
        c=t
        if(f not in aux):
            aux[f]=1
        while(len(c)-2>=5):
            f=c[-2:]
            c=c[:-2]
            if(f not in aux):
                aux[f]=1
    return sorted(aux)
s=input()

if(len(s)<6):
    print(0)
else:
    b=_(s)
    print(len(b))
    for e in b:
        print(e)