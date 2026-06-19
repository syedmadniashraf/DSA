def pattern17(N):
    # Loop for each row
    for i in range(N):

        # Print leading spaces
        print(" " * (N - i - 1), end="")

        # Initialize character to start from 'A'
        ch = ord('A')
        breakpoint = (2 * i + 1) // 2

        # Print characters in row
        for j in range(1, 2 * i + 2):
            print(chr(ch), end="")
            if j <= breakpoint:
                ch += 1
            else:
                ch -= 1

        # Print trailing spaces (optional in Python, handled above)
        print()

# Driver code
if __name__ == "__main__":
    N = 5
    pattern17(N)
