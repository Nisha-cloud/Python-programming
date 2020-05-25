l=[]
n=int(input("Enter the size: "))
for i in range(n):
a=input("Enter a element: ")
l.append(a)
t=tuple(l)
print(t)
s=input("Element whose occurence is asked)
print(t.count(s))