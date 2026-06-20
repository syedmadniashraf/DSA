def armstrong(n):
    org = n
    sum = 0
    digit = len(str(n))
    while(n > 0):
        lastDigit = n % 10
        sum = sum + (lastDigit**digit)
        n = n // 10
    return org == sum

n = int(input("Enter n: "))
if armstrong(n):
    print(f"The {n} is armstrong number")
else:
    print(f"The {n} is not armstrong number")