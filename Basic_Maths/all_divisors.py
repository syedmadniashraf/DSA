# def divisors(n):
#     for i in range(1,n+1):
#         if(n % i == 0):
#             print(f"The divisors are {i}")
        
# n = int(input("Enter n: "))
# divisors(n)

# TC = O(n) [because loops run from 1 to n]


# 2nd approach better

import math

class Solution:
    # Function to get all divisors
    def getDivisors(self, N):
        # Create list to store divisors
        res = []

        # Loop from 1 to square root of N
        for i in range(1, int(math.isqrt(N)) + 1):
            # Check if i divides N
            if N % i == 0:
                # Add i to result
                res.append(i)

                # If N // i is not the same, add that too
                if i != N // i:
                    res.append(N // i)

        res.sort()
        # Return the list of divisors
        return res

# Create object of Solution class
sol = Solution()

# Input number
N = 36

# Get divisors
result = sol.getDivisors(N)

# Print the result
print("Divisors of", N, ":", *result)  # (*) ye na lgate toh list deta isko unpacking operator kehte

# TC = O(√N) which is faster than O(n)