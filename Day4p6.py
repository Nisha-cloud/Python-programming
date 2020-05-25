ele=dict()
l=""
s=""
n=int(input("Enter number of value pairs you want to enter:"))
for i in range(n):
print("Enter key for dictionary:")
k=input()
print("Enter the value of dictionary")
val=input()
ele[k]=val
print(element)
print("The 2nd largest value is")
for j in ele:
for k in ele:
if (ele[j]>ele[k] and j!=k):
l=ele[j]
for j in ele:
for k in ele:
if (ele[j]>ele[k] and ele[j]<l):
s=ele[j]
print(s)
