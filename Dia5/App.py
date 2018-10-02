N,K=map(int,input().split())
times=set()
if(K):
    for i in range(N):
        A,E,D=map(int,input().split())
        if(i<K):
            times.add(sum([A,E,D]))
    print(max(times))
else:
    print(0)