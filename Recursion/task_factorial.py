class solution:
    def fact(self,n):
        if(n == 0 or n == 1):
            return 1
        return n * self.fact(n-1)

sol = solution()
n = int(input("Enter n: "))
print(sol.fact(n))

# TC = O(n)
# SC = O(n) (recursive stack space)