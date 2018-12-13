a=int(input("Enter the First number of the series "))
b=int(input("Enter the second number "))
n=int(input("Enter the term upto "))
print(a,b,end=" ")
while(n-2):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    n=n-1
