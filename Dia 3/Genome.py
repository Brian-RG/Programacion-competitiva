import operator
n=int(input())
s=input()
aux=set(["A","G","C","T"])
au=set()
dic={"A":0,"G":0,"C":0,"T":0}
for e in dic:
    dic[e]=s.count(e)
    au.add(max(dic.items(), key=operator.itemgetter(1))[0])
print(max(dic.items(), key=operator.itemgetter(1))[0])