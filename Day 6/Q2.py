def print_first_n_integers(n):
    numbers = list(range(1, n + 1))
    result = ','.join(map(str, numbers))
    print(result)
n = int(input("Enter a positive integer: "))
print_first_n_integers(n)
