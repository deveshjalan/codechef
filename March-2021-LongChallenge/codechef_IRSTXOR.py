t=int(input())

for z in range(t):
    a=input()
    a=str(bin(int(a)))[2::]
    l=len(a)
    b="1"*(l-1)
    b="0"+b
    b=int(b,2)
    c=b^int(a,2)
    print(b*c)













