A=[[1,2,3],[4,5,6],[7,8,9]]
B= [[1,2],[3,4],[5,6]]
m,n,p,q=2,3,3,2
result=[]
for i in range(m):
    row=[]
    for j in range(q):
        s=0
        for k in range(n):
            s+=A[i][k]*B[k][j]
        row.append(s)
    result.append(row)
print(f"Result : {result}")