def stolen(val,n):
if n==0:
return 0
if n==1:
return val[0]
if n==2:
return max(val[0],val[1])
a=[0]*n
a[0]=val[0]
a[1]=max(val[0],val[1])
for i in range(2,n):
a[i]=max(val[i]+a[i-2],a[i-1])
return a[-1]
