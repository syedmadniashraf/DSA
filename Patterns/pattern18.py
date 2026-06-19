class solution:
    def pattern(self,n):
        for i in range(n):
            for ch in range(ord('A') + n-1-i, ord('A') + n):
                print(chr(ch),end="")
            print()

sol = solution()
n = int(input("Enter n: "))
sol.pattern(n)

