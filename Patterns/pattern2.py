class solution:
    def pattern(self,n):
        for i in range(n):
            print("*" * (i+1))

sol = solution()
n = int(input("Enter n: "))
sol.pattern(n)