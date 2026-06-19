class solution:
    def pattern(self,n):
        for i in range(n):
            for j in range(n-i-1):
                print(" ",end="")
            for j in range(2*i+1):
                print("*",end="")
            for j in range(n-i+1):
                print(" ",end="")
            print()

sol = solution()
n = int(input("Enter n: "))
sol.pattern(n)