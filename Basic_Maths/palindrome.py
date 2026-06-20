def palindrome(n):
    revNum = 0
    dup = n  # inside loop n changes so to keep original n we use dup var for comparing the revNum
    while(n > 0):
        lastDigit = n % 10
        revNum = revNum * 10 + lastDigit
        n = n // 10
    return dup == revNum

n = int(input("Enter n: "))
if palindrome(n):
    print(f"The {n} is palindrome ")
else:
    print(f"The {n} is not palindrome")