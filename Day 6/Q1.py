def sum_of_digits(number):
    num_string = str(number)
    sum = 0
    for digit in num_string:
        sum += int(digit)
    print("The sum of the digits is:", sum)
number = int(input("Enter a positive integer: "))
sum_of_digits(number)
