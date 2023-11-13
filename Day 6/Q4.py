def sum_common_divisible(a, b):
    sum = 0
    for num in range(1000, 2001):
        if num % a == 0 and num % b == 0:
            sum += num
    return sum
a = int(input("Enter the first positive integer: "))
b = int(input("Enter the second positive integer: "))
result = sum_common_divisible(a, b)
print(result)