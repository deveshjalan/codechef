# cook your dish here

def reduce(matrix,r,c,x):

    for i in range(r):
        temprow=[0]*c
        acc=0
        for j in range(c):
            acc+=temprow[j]
            if(j+x<c):
                temprow[j+x]= -(matrix[i][j]-acc)
            if(j+x-1<c):
                acc=matrix[i][j]
            matrix[i][j]-=acc

    for j in range(c):
        tempcol=[0]*r
        acc=0
        for i in range(r):
            acc+=tempcol[i]
            if(i+x<r):
                tempcol[i+x]= -(matrix[i][j]-acc)
            if(i+x-1<r):
                acc=matrix[i][j]
            matrix[i][j]-=acc
    return matrix


def checkMatrix(matrix,r,c,x):
    for i in range(r-x+1,r):
        for j in range(c-x+1,c):
            if matrix[i][j]!=0:
                return "NO"
    return "YES"



t=int(input())

for z in range(t):
    a=input().split()
    a=[int(b) for b in a]
    r=a[0]
    c=a[1]
    x=a[2]
    MAT1=[]
    for i in range(r):
        row=input().split()
        row=[int(b) for b in row]
        MAT1.append(row)
    for i in range(r):
        row=input().split()
        row=[int(b) for b in row]
        for j in range(len(row)):
            MAT1[i][j]-=row[j]

    MAT1=reduce(MAT1,r,c,x)
    #print(MAT1)
    ans=checkMatrix(MAT1,r,c,x)
    print(ans)