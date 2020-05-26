def replace(n):
n+=calc(n)
return n
def calc(n)
s=0
decpla=1
if(n==0):
s+=(5*decpla)
while(n>0):
if(n%10==0):
s+=(5*decpla)
n//=10
decpla*=10

a=int(input("Enter a number:"))
print("Number aftwer replacinmg 0 with 5:")
print(replace(a))