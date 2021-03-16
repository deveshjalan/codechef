
def calcNext(a,count):
    stk=[]
    stk.append(0)
    nexx=[0]*count
    for i in range(1,count):
        while(len(stk)>0 and a[stk[-1]]<=a[i]):
            nexx[stk[-1]]=i
            stk.pop()
        stk.append(i)
    for values in stk:
        nexx[values]=-1
    return nexx

def calcPrev(a,count):
    stk=[]
    stk.append(0)
    prev=[0]*count
    for i in reversed(range(0,count)):
        if(len(stk)==0):
            s.append(i)
            continue
        
        while(len(stk)>0 and a[stk[-1]]<=a[i]):
            prev[stk[-1]]=i
            stk.pop()
        stk.append(i)
    for values in stk:
        prev[values]=-1
    return prev


def findMaxDist(a,count):
    nexx=calcNext(a,count)
    prev=calcPrev(a,count)
    print(nexx)
    print(prev)

    maxx=0
    i=0
    while i<count:
        if(nexx[i]!=-1):
            nxt=nexx[i]
            cur=nxt
            prevSlope=float(a[nxt]-a[i])/float(nxt-i)
            num=nexx[i]-i
            while(nxt!=-1):
                nxt_nxt=nexx[nxt]
                if(nxt_nxt==-1): 
                    break
                if (float(a[nxt_nxt]-a[i])/float(nxt_nxt-i))<prevSlope:
                    nxt=nxt_nxt
                    continue
                nxt=nxt_nxt
                num=nxt_nxt-i
                cur=nxt
                prevSlope=float(a[nxt_nxt]-a[i])/float(nxt_nxt-i)
            maxx=max(maxx,num)
            if cur!=-1:
                i=cur-1
        i+=1

    i=count-1
    while i>=0:
        if(prev[i]!=-1):
            nxt=prev[i]
            cur=nxt
            prevSlope=float(a[nxt]-a[i])/float(nxt-i)
            num=i-prev[i]
            while(nxt!=-1):
                nxt_nxt=prev[nxt]
                if(nxt_nxt==-1): 
                    break
                if (float(a[nxt_nxt]-a[i])/float(nxt_nxt-i))>prevSlope:
                    nxt=nxt_nxt
                    continue
                nxt=nxt_nxt
                num=i-nxt_nxt
                cur=nxt
                prevSlope=float(a[nxt_nxt]-a[i])/float(nxt_nxt-i)
            maxx=max(maxx,num)
            if cur!=-1:
                i=cur+1
        i-=1

    return maxx

t=int(input())

for z in range(t):
    count=int(input())
    a=input().split()
    a=[int(b) for b in a]
    
    ans=findMaxDist(a,count)
    print(ans)