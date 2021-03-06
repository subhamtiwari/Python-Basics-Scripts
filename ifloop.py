num =10 
if num>10:
    print("the number is postitive")
print("The num is negative")



numm=10
if numm-10:
    print("the number is positive and o is always false")
print("if the condition is zero the it will print false")


num1 = 10
num2 = 50
num3 = 15

if (num1 >= num2) and (num1 >= num3):           #logical operator   and
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print("Largest element among three numbers is: {}".format(largest))