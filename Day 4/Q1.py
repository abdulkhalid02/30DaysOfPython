side_a = int(input("Enter the length of the first side: "))
side_b = int(input("Enter the length of the second side: "))
side_c = int(input("Enter the length of the third side: "))

def triangle_type(a, b, c):
    if a == b == c:
        print ("It is a Equilateral Triangle")
    elif a == b or b == c or a == c:
        print ("It is a Isosceles Triangle")
    else:
        print ("It is a Scalene Triangle")
triangle = triangle_type(side_a, side_b, side_c)