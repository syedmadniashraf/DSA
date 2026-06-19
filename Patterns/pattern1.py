# n = int(input("Enter n: "))

# for i in range(n):
#     for j in range(n):
#         print("*",end = "")
#     print()


class solution:
    def pattern(self,n):
        for i in range(n):
            for i in range(n):
                print("*",end="")
            print()

sol = solution()
n = int(input("Enter n: "))
sol.pattern(n)
    