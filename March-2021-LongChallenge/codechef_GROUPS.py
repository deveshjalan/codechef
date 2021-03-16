# cook your dish here

t=int(input())

for z in range(t):
    i=input()
    l=i.split('0')
    l=[i for i in l if i!='']
    print(len(l))