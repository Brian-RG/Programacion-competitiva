"""def _(lista,ind):
    aux={}
    c=0
    for i in range(int(ind)-1,len(lista)):
            if lista[i] not in aux:
                c+=1
                aux[lista[i]]=1
    #print(aux)
    return c
    """
n,m=map(int,input().split(" "))
listilla=input().split(" ")
prueba=[]
respuesta=[0]*n
res={}
for e in range(m):
    prueba.append(int(input()))
for l in range(len(listilla)-1,-1,-1):
    if listilla[l] not in res:
        res[listilla[l]]=1
        respuesta[(n-l-1)]+=1
    if len(listilla)>=2:
        respuesta[n-l-1]+=respuesta[n-l-2]

for z in range(0,len(prueba)):
    print(respuesta[len(respuesta)-prueba[z]])
