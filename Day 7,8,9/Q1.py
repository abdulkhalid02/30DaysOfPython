num=int(input("Enter the positive integer : "))
temp=0
print("The prime factors are ",end="")
if (num%2==0):
    print(2,end=",")
for i in range(3,num+1,2):
    temp=0
    for o in range(2,i):
        if(i%o==0):
            temp=1              
    if (num%i==0) and (temp!=1):
        print(i,end=",")