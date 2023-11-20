def print_number_arrow(n):
    for i in range(1, n+1):
        nums = list(range(1, i+1))
        print(','.join(map(str, nums)))
    for i in range(n-1, 0, -1):
        nums = list(range(1, i+1))
        print(','.join(map(str, nums)))
n = int(input("Enter a positive integer: "))
print_number_arrow(n)
def print_number_arrow(n):
    for i in range(1, n+1):
        nums = list(range(1, i+1))
        print(','.join(map(str, nums)))
    for i in range(n-1, 0, -1):
        nums = list(range(1, i+1))
        print(','.join(map(str, nums)))
n = int(input("Enter a positive integer: "))
print_number_arrow(n)
