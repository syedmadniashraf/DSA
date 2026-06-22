class solution:
    def printName(self,name,count,n):
        if count ==  n:
            return
        print(name)

        self.printName(name,count + 1,n)
    

sol = solution()
n = int(input("Enter n: "))
name = input("Enter name: ")
sol.printName(name, 0, n)