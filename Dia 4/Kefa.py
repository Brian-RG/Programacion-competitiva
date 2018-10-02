class Nodo:
    c=[]
    def __init__(self,cat,num,hijos=[]):
        self.cat=cat
        self.num=num
        self.hijos=[]
    def giveson(self,Nodo):
        self.hijos.append(Nodo)
    def hascat(self):
        return self.cat
    def prueba(self):
        for e in self.hijos:
            print(e)
    def gethijos(self):
        if len(self.hijos):return self.hijos
        else: return None
    def buscahijos(self,counter,m):
        if(self.gethijos()!=None):
            for e in self.hijos:
                if e.hascat():
                    counter+=1
                counter=e.buscahijos(counter,m)
        else:
            if(counter<=m):
                c.append(counter)
        return counter



n,m=map(int,input().split())
nodos=[]
c=[]
f=input().split()
for i in range(0,len(f)):
    nodos.append(Nodo(int(f[i]),i))
for e in range(1,n):
    x,y=map(int,input().split())
    nodos[x-1].giveson(nodos[y-1])

print(nodos[0].gethijos())
for o in nodos[0].gethijos():
    counter=nodos[0].hascat()
    if(o.hascat()):
        counter+=1
    o.buscahijos(counter,m)
print(len(c))
