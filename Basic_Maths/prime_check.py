# def checkPrime(n):
#     cnt = 0
#     for i in range(1,n+1):
#         if n % i == 0:
#             cnt = cnt + 1
#     return cnt == 2  # If the number of factors is exactly 2 (1 and the number itself), it's prime

# n = 1483 
# isPrime = checkPrime(n)  

# if isPrime:
#     print(f"{n} is a prime number.")
# else:
#     print(f"{n} is not a prime number.")

# In this TC = O(n)

# 2nd approach

def checkPrime(n):
    cnt = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            cnt = cnt + 1
         # If n is not a perfect square, count its reciprocal factor
            if n // i != i:
                cnt += 1   # Agar pair ka doosra factor alag hai to usko bhi count karo.
    return cnt == 2

n = 1483 
isPrime = checkPrime(n)  

if isPrime:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")

# TC = O(√N) which is faster than O(n)

