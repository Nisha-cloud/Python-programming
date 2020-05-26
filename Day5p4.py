
def greatest(a):
n=len(a)
rmax=a[n-1]
a[n-1]=-1
for i in range(n-2,-1,-1):
b=a[i]
a[i]=rmax
if rmax<b:
rmax=b

def print(a):
for i in range(0,len(a)):
print a[i]
