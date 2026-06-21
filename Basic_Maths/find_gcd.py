def find_gcd(a,b):
    while a > 0 and b > 0:
        if(a > b):
            a = a % b
        else:
            b = b % a
    if(a == 0):
        return b
    return a 

a = int(input("Enter n1: "))
b = int(input("Enter n2: "))

gcd = find_gcd(a,b)
print(gcd)


# TC: O(log(min(a, b)))
# Therefore, min(a, b) is used because the running time of the GCD algorithm mainly depends on the size of the smaller number.


# def find_gcd(n1,n2):
#     gcd = 1
#     for i in range(1,min(n1,n2) + 1):
#         if n1%i==0 and n2%i==0:
#             gcd = i
#     return gcd
# n1,n2 = 20, 15
# gcd = find_gcd(n1,n2)
# print(n1, n2, gcd)

# It will find gcd from last to 0 so it will be better code

# def findGcd(n1,n2):
#     for i in range(min(n1,n2),0,-1):
#         if n1%i==0 and n2%i==0:
#              # If i is a common factor,return it as the GCD
#             return i
       # If no common factors are found,return 1 (as 1 is always a divisor of any number)
#     return 1
# n1 = 20
# n2 = 15
# gcd = findGcd(n1, n2)
# print(n1,n2,gcd)