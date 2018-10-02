import sys
sys.setrecursionlimit(100000)
def _(lista,m,counter=1,visitado={}):
    temporal = []
    for i in lista:
        l = i-1
        r = i*2
        if r < 2*m:
            if r not in visitado:
                temporal += [r]
                visitado[r] = 0
        if l > 0:
            if l not in visitado:
                temporal += [l]
                visitado[l] = 0

    lista=temporal
    if m in visitado:
        return counter
    else:
        return _(lista,m,counter+1)
n,m = map(int,input().split())
if m<n:
    print(n-m)
else:
    print(_([n],m))
