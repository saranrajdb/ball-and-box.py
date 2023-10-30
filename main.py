l=list(map(int,input().split()))
ts=0
for i in range(0,len(l)):
    if (pow(i+1,2) > l[i]):
        dif=pow(i+1,2)-l[i]
        
        ts+=dif
print(ts)