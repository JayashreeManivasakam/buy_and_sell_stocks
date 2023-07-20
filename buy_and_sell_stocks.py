l=list(map(int,input().split()))
n=len(l)
m=[]
result=0
for j in range (0,n-1):
    dif=[]
    for i in range(j,n-1):
        d=abs(l[i+1]-l[j])
        dif.append(d)
    m.append(max(dif))
result=max(m)
print(result)
