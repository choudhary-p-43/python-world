num1=int(input("enter the 1st number"))
num2=int(input("enter the 2nd number"))
op=input("which operator +,-,*,/")
if op=="+": 
    Sum=num1+num2
    print("your answer is: ",sum)
elif op=="-":
    diff=num1-num2
    print("ÿour answer is: ",diff)
    
elif op=="*":
    product=num1*num2
    print("your answer is: ",product)
elif op=="/":
    division=num1/num2
    print("your answer is: ",division)
else:
    print("you type a different opertator")

