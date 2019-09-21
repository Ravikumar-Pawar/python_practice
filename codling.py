def tostring(list):
    return ''.join(list)

def permutation(a, l, r,):
    list1=[]
    if l==r:
        list1.append(tostring(a))
        for i in list1:
            print(i,end=' ')
    else:
        for i in range(l,r+1):
            a[l],a[i]=a[i],a[l]
            permutation(a,l+1,r)
            a[l], a[i] = a[i], a[l]
s='ABC'
n=len(s)
a=list(s)
permutation(a,0,n-1)
