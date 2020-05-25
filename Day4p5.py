def p(List,String=""):
Set=set(List)
stringList=[]
if len(Set)==1:
String+="".joint(List)
return list([String])
for i in Set:
List1=list(List)
S=String+i
List1.remove(x)
stringList.extend(p(List1,S))
return stringList
string=input("Enter a string :")
n=int(input("Enter list size:"))
l1=[]
rw=[]
for i in range(n):
le=input("Enter the element:")
l1.append(le)
print(l1)
List=p(list(string))
rw="".joint(List).intersection(l1)
print(rw)
