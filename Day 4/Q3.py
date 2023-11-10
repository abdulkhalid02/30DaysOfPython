a=int(input("Enter the coefficient of a square term : "))
b=int(input("Enter the coefficient of a term : "))
c=int(input("Enter the coefficient of constant term : "))
d=(b**2-4*a*c)
if(d>0):
    print("\nThe Roots are Real and Different.They are ",end="")
    print((-b-((d)**0.5))/(2*a),end=",")
    print((-b+((d)**0.5))/(2*a))
elif(d==0):
    print("\nThe Roots are Real and Same.They are ",end="")
    print(-b/(2*a),-b/(2*a),sep=",")
else:
    print("\nComplex Roots(We have used j instead of i to represent square root of -1).They are ",end="")
    rp = (-b / (2*a))
    im = (abs(d) ** 0.5) / (2*a)
    print('(',rp,"+",im,'i)',end=",",sep="")
    print('(',rp,"-",im,'i)',sep="")
