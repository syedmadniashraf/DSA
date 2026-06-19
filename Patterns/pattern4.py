class solution:
    def pattern(self,n):
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(i, end= " ")
            print()

sol = solution()
n = int(input("Enter n: "))
sol.pattern(n)