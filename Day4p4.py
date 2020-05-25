ele={}
a={}
n=int(input("Enter the number of key value pairs to enter:"))
for i in range(n):
s=input("Enter the key:")
t=input("Enter the value:")
ele[s]=t
print("The dictionary is:")
print(ele)
for s,t in ele.items():
if t not in a.t():
a[s]=t
print("After removal of duplicate items:",a)