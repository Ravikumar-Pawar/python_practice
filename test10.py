
s=input("DD MM YYY:")
print(s.split())
list1=list(s.split())
dict={"Jan":"01","Feb":"02","Mar":"03","Apr":"04","May":"05","Jun":"06","Jul":"07","Aug":"08","Sep":"09","Oct":"10","Nov":"11","Dec":"12"}
d=list1[0]
m=list1[1]
y=list1[2]
k=dict[m]
print(y+"-"+k+"-"+d)