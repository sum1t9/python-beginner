#take two input and store it in num1 ,num2
num1, num2 = input('Enter two Numbers').split()
#convert string into integer
num1=int(num1)
num2=int(num2)
#addition
sum = num1 + num2
#subtraction
diff = num1 - num2
#multiply
mul = num1 * num2
#divide
div = num1 / num2
#modulus
mod = num1 % num2
#print
print("{} + {} = {}".format(num1,num2,sum))
print("{} - {} = {}".format(num1,num2,diff))
print("{} * {} = {}".format(num1,num2,mul))
print("{} / {} = {}".format(num1,num2,div))
print("{} % {} = {}".format(num1,num2,mod))