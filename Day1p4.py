cp=float(input("Enter C.P. :")) 
sp=float(input("Enter S.P. :"))
p=sp-cp
print("Profit : ",+ p)
p=p+(5/100)*p
nsp=cp+p
print("New S.P. :",+ nsp)