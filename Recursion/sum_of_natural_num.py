# Functional recursion

# class solution:
#     def sumOfNaturalNumbers(self,n):
#         if(n == 0):
#             return 0
#         return n + self.sumOfNaturalNumbers(n-1)  # Answer return ho raha hai → Functional Recursion
    
# sol = solution()
# n = int(input("Enter n: "))
# print(sol.sumOfNaturalNumbers(n))

# Time Complexity: O(N)
# Space Complexity: O(N)


# Loop based

# class solution:
#     def sumOfNaturalNumbers(self,n):
#         total = 0

#         for i in range(1,n+1):
#             total += i
#         return total
    
# sol = solution()
# n = int(input("Enter n: "))
# print(sol.sumOfNaturalNumbers(n))

# TC = O(N)
# SC = O(1) because only total and i are used, and no extra memory grows with N.


# Parameterised recursion

# class solution:
#     def sumOfNaturalNumbers(self,i,sum):  # the answer (sum) is carried in the function parameter itself.
#         if(i < 1):
#             print(sum)
#             return 
#         self.sumOfNaturalNumbers(i-1,sum+i)


# sol = solution()
# n = int(input("Enter n: "))
# sol.sumOfNaturalNumbers(n,0)

# TC = O(n)
# SC = O(n)

# Formula based

class solution:
    def sumOfNaturalNumbers(self,n):
        return (n * (n+1)) // 2
    
sol = solution()
n = int(input("Enter n: "))
print(sol.sumOfNaturalNumbers(n))

