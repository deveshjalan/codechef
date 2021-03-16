# cook your dish here
def calcMinimumCost(N,E,H,A,B,C):

    check=1000000000000000000000
    ans=1000000000000000000000
    LOOP_L=min(E,H,N)+1
    for c in range(LOOP_L):
        maximumA=int((E-c)/2)
        maximumB=int((H-c)/3)
        a=0
        b=0
        if(A>B):
            b=min(N-c,maximumB)
            a=min(N-b-c,maximumA)
        elif B>A:
            a=min(N-c,maximumA)
            b=min(N-a-c,maximumB)
        else:
            if(maximumA+maximumB<N-c):
                continue
            a=int((N-c)/2)
            b=N-c-a
        if(a+b+c!=N):
            continue
        ans=min(ans,a*A+b*B+c*C)
        #print(ans)
    if ans==check:
        return -1
    else:
        return ans

t=int(input())

for z in range(t):
    a=input().split()
    a=[int(b) for b in a]
    #print(a)
    N=a[0]
    E=a[1]
    H=a[2]
    A=a[3]
    B=a[4]
    C=a[5]

    ans=calcMinimumCost(N,E,H,A,B,C)
    print(ans)