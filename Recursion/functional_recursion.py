class solution:
    def sumOfNaturalNumbers(self,n):
        if(n == 0):
            return 0
        return n + self.sumOfNaturalNumbers(n-1)  # Answer return ho raha hai → Functional Recursion
    
sol = solution()
n = int(input("Enter n: "))
print(sol.sumOfNaturalNumbers(n))

# Time Complexity: O(N)
# Space Complexity: O(N)
