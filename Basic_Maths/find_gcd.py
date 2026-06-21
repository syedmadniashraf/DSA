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