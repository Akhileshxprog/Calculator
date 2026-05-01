a=int(input("enter first number: "))
c=int(input("enter second number: "))
b= input("Which arithmatic operation would you like to perform: ")
if b=="+":
    result = (a+c)
elif b=="-":
    result = (a-c)
elif b=="*":
    result = (a*c)
elif b=="/":
    result = (a/c)
else:
    result = ("invalid input")
print(f"result: {result}")
