A=list(map(int,input().split()))
sub=[[]]
for i in range(len(A)):
    for j in range(i+1,len(A)):
        s=A[i:j]
        sub.append(s)
