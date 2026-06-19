class solution:
    def pattern(self,n):
        for i in range(n):
            for j in range(i+1):
                print(chr(65 + i), end=" ") 
            print()
    
sol = solution()
n = int(input("Enter n: "))
sol.pattern(n)