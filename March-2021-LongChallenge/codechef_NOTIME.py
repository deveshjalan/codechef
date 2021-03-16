l1=input().split()
l2=input().split()
l1=[int(i) for i in l1]
l2=[int(i) for i in l2]

diff=l1[1]-l1[2]

flag=0
for i in l2:
    if i>=diff: 
        flag=1
if flag==0: print("NO")
else : print("YES")
