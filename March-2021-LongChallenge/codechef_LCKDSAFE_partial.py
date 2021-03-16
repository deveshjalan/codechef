
from functools import reduce
t=int(input())

for z in range(t):
    count=int(input())
    a=input().split()
    a=[int(b) for b in a]
    ans=count*(count-1)/2
    temp=1
    for i in range(1,count):
        if a[i]==a[i-1]:
            temp+=1
        else:
            if temp>1:
                ans= ans- temp*(temp-1)/2
            temp=1
    if temp>1:
        ans= ans- temp*(temp-1)/2
    print(int(ans))
    




    '''
    for i in range(count):
        AND=a[i]
        OR=a[i]
        MAX=a[i]+    
        for j in range(i,count):
            
            AND=AND&a[j]
            OR=OR|a[j]
            if(MAX<a[j]):
                MAX=a[j]
            if AND^OR>=MAX:
                ans+=1
                #print(str(i)," ",str(j))
    print(ans)
    '''