class Solution:
    # Function to print the pattern of alphabets
    def pattern(self, N):
        # Outer loop for the number of rows
        for i in range(N):
            
            # Inner loop to print alphabets from A to A + i
            for j in range(N-i):
                print(chr(65 + j), end=" ")  # Print the alphabet character followed by a space

            # Move to the next line after printing the current row
            print()

sol = Solution()
N = int(input("Enter N: "))
sol.pattern(N)
