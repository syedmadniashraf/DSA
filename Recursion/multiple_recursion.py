# fibionacci series (dynamic programming (bottom up approach))
# Smaller subproblems are solved first and used to compute larger ones.
# No recursion is used.

def fibonacci(n):
    if n == 0:
        print(0)
    elif n == 1:
        print("0 1")
    else:
        fib = [0] * (n+1)
        fib[0] = 0
        fib[1] = 1

        for i in range(2,n+1):
            fib[i] = fib[i-1] + fib[i-2]
        print(f"The Fibonacci Series up to {n}th term:")
        print(" ".join(str(num) for num in fib))

n = int(input("Enter n: "))
fibonacci(n)

# TC = O(n)
# SC = O(n)

# Better approach

# def main(n):
#     # If n is 0, only the first term is printed
#     if n == 0:
#         print(f"The Fibonacci Series up to {n}th term:")
#         print(0)
#     else:
#         second_last = 0  # (i-2)th term
#         last = 1         # (i-1)th term

#         print(f"The Fibonacci Series up to {n}th term:")
#         print(f"{second_last} {last}", end=" ")

#         for i in range(2, n + 1):
#             cur = last + second_last  # Current ith Fibonacci number
#             second_last = last        # Move window
#             last = cur
#             print(cur, end=" ")

# n = int(input("Enter n: "))
# main(n)

# TC = O(n)
# SC = O(1) --> because only a constant number of variables (second_last, last, cur) are used.

# Multiple recursion

def fibonacci(n):
    if n <= 1:
        return n
    else:
        last = fibonacci(n-1)
        s_last = fibonacci(n-2)
        return last + s_last
n = int(input("Enter n: "))
fibonacci(n)

# TC = O(2ⁿ) --> (Har node se lagbhag 2 branches nikal rahi hain)
#                (Recursive call tree exponentially grow karta hai)

# SC = O(n)