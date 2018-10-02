
h1, h2 = list(map(int,input().split()))
u1, u2 = list(map(int,input().split()))
pasos = 0
for i in int(input())*'_':
    a, b, c= list(map(int,input().split()))
    if (a * h1 + b * h2 + c) * (a * u1 + b * u2 + c) < 0:
        pasos+=1
print(pasos)
