n = 5
for i in range(n, 0, -1):
    # Print leading spaces
    print(' ' * (n - i), end='')
    
    # Print numbers
    for j in range(i):
        print(n, end=' ')
    
    # Print a newline
    print()