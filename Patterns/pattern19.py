class solution:
    def pattern(self,n):
        space = 0
        for i in range(n):
            for j in range(n-i):
                print("*", end= "")

            for j in range(space):
                print(" ", end="")
                
            for j in range(n-i):
                print("*", end= "")
            
            space += 2
            print()

        space = 2 * n -2
        for i in range(1,n+1):
            for j in range(i):
                print("*", end="")

            for j in range(space):
                print(" ", end="")

            for j in range(i):
                print("*", end="")

            space -= 2
            print()
            
sol = solution()
n = int(input("Enter n: "))
sol.pattern(n)