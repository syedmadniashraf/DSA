# class solution:
#     def printNum(self, current, n):
#         if current > n:
#             return
#         print(current)

#         self.printNum(current + 1,n)

# sol = solution()
# n = int(input("Enter n: "))
# sol.printNum(1,n)


# Backtracking


class solution:
    def printNum(self, current):
        if current < 1:
            return
        self.printNum(current - 1)  # recursive call
        print(current)

sol = solution()
n = int(input("Enter n: "))
sol.printNum(n)

# Trick:
    # print() before recursive call --> normal recursion
    # print() after recursive call --> backtracking


# Time Complexity = O(n)
# Space Complexity = O(n) (recursive call stack ki wajah se).