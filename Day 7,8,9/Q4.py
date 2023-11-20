def validate_phone_number(number):
    if number[0] not in ['6', '7', '8', '9']:
        return "invalid"
    if len(number) != 10:
        return "invalid"
    for digit in set(number):
        if number.count(digit) > 7:
            return "invalid"
    for i in range(len(number) - 4):
        if len(set(number[i:i+5])) == 1:
            return "invalid"
    return "valid"
phone_number = input("Enter a phone number: ")
result = validate_phone_number(phone_number)
print(result)
