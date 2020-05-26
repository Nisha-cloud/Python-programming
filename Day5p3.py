def knapsack(a,b,v,n)
if n==0 or a==0:
return 0
for i in range(n):
for j in range(i+1,n):
if b[x]+b[y]==a:
return v[x]+v[y]

v=[]
b=[]
a=int(input("Enter max weight:"))
n=int(input("Enter number of items:"))
for i in range(n):
val=int(input("Enter the value:"))
wt=int(input("Enter the weight:"))
v.append(val)
b.append(wt)
print(v)
print(b)
print("The value for max weight is:")
print(knapsack(a,b,v,n))
