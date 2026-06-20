def countDigits(n):
    cnt = 0
    while(n > 0):
        lastDigit = n % 10
        cnt = cnt + 1
        n = n // 10

    return cnt

if __name__ == "__main__":
    N = 329823
    print("N:", N)
    digits = countDigits(N)
    print("Number of Digits in N:", digits)

# For above TC will be: O(log10 (n)) --> because we are dividing n by 10 so base will be 10

# If we divide n by 2 TC will be: O(log2 (n)) --> we take log base with which we divide the n


# 2nd approach

import math

n = int(input("Enter n: "))

digit = int(math.log10(n) + 1)
print(f"No of digits: {digit}")

# For this TC will be: O(1) --> because all opearations executing once and there is no loop