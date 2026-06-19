class solution:
    def pattern(self,n):
        for i in range(1,n+1):
            for j in range(n - i + 1):
                print("*", end= " ")
            print()

sol = solution()
n = int(input("Enter n: "))
sol.pattern(n)

