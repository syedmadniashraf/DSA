class Solution:
    def pattern10(self, n):
        # Outer loop for rows
        for i in range(1, 2 * n):
            
            # First half me stars = row number
            stars = i

            # Second half me stars decrease honge
            if i > n:
                stars = 2 * n - i

            # Print stars
            for j in range(stars):
                print("*", end="")

            # Next line
            print()


sol = Solution()
n = int(input("Enter n: "))
sol.pattern10(n)