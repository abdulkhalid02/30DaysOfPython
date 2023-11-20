string1=input("Enter the string : ")
string2=string1.lower()
string2=sorted(string2) 
print("Sorted string is ",end="")
for i in string2:
    print(i,end="")