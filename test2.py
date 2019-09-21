import operator
def reverse(s):
    str=" "
    for i in s:
        str=i+str
    return str
s=input()
r=reverse(s)
for i in s:
   print( l=[ord(i)])
for j in r:
   print( m=[ord(j)])

d1=[l[i+1]-l[i] for i in range(len(l)-1)].sort()
print(d1)

d2=[m[i+1]-m[i] for i in range(len(m)-1)].sort()
print(d2)
if d1==d2:
    print("Funny")
else:
    print("Not Funny")