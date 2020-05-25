a=[]
d=0
s=""
n=int(input("Enter the size : "))
for i in range(n):
b=input("Enter the element : ")
a.append(b)
print(a)
t=tuple(a)
for j in t:
if t.count(j)>d:
d=t.count(j)
for j in t:
for k in t:
if (t.count(j)==d and t.count(k)==d and j!=k):
if j<k:
s=j
else:
s=k
print("The winner is : ",s)
