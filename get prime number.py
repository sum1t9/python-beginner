def is_prime(num):
    for i in range(2,num):
        if(num % i) == 0:
            return False
    return True

def getprimes(max):
    listofprimes = []
    for num1 in range(2,max):
        if is_prime(num1):
            listofprimes.append(num1)
    return listofprimes

number = int(input("Search for primes upto "))
final_list = getprimes(number)
for prime in final_list:
    print(prime)