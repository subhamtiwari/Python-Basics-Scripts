lst=[10,20,34,40,56,60]

prod=1
index=0


while index < len(lst):
    prod *= lst[index]
    index +=1
    
print("Product is :{}" .format(prod))



num=int(input("enter the number"))

isdivisble=False;


i=2
while i<num:
    if num%i==0:
        isdivisble=True
        print("{} is divisble by {}" . format(num,i))
    i +=1;
if isdivisble : 
    print("THe number is not a prime number".format(num))
    
else:
    print("{} is a prime number ".format(num))