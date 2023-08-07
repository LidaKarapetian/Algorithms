#!usr/bin/python

#Python program to check if a number is prime or not

num = int(input("Enter the number to check if it is prime or not: "))
flag = True

for i in range(2, int(num ** 1/2) + 1):    
    if(num % i) == 0:
        flag = False
        break

if flag == False:
    print(num, "is not prime number")
else:
    print(num, "is prime number")
    
    
# Python program to find the greatest common divisor of numbers

n = int(input("Enter the first number: "))
m = int(input("Enter the second number: "))
gcd = 0              #the greatest common divisor

if n > m:
    small_num = m
else:
    small_num =  n

for i in range(1, small_num + 1):
    if((n % i == 0) and (m % i == 0)):
        gcd = i

print("The greatest common divisor is ", gcd)


# Python program to find the least common multiple of numbers

lcm = (n * m) // gcd    #formula to find the least common multiple
print("The least common multiple is ", lcm)


# Python program to print the Fibonacci sequence's memeber

n = int(input("Enter the number: "))
n1 = 1
n2 = 1
for i in range(2, n):
    n1, n2 = n2, n1 + n2

print(n2)

#Python program to find the factorial of number

def fact(n):
    if type(n) != int:
        print("Sorry only int")
        return None
    if n < 1:
        return 1
    f = 1
    for i in range(1, n+1):
        f *= i
    return f





