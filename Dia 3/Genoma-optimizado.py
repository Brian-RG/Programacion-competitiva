n=int(input());s=input()
if(n%4):print("===")
else:
    m=n//4;q,a,g,c,t = [s.count(x) for x in '?AGCT']
    for x,y in zip("AGCT", [a,g,c,t]):s=s.replace("?",x,m-y)
    print(s if s.count("A")==s.count("G")==s.count("C")==s.count("T") else "===")
