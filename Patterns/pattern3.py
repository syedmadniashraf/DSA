class solution:
    def pattern(self,n):
        for i in range(1,n+1): # n ka mtlb rows hai or agr 5 likhne pr 5 rows chaiye toh n+1 krna hoga kyuki isme bhi last wala include nhi hota
            for j in range(1,i+1): # i+1 isilie likha kyuki stop include nhi hota usko last ko include ke lie likha ye 
                print(j ,end=" ")
            print()

sol = solution()
n = int(input("Enter n: "))
sol.pattern(n)
