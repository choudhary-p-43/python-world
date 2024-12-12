def Fibonacci(num):
    
    if num<0:
        print("wrong number")
    elif num==0:
        return 0
    elif num==1 or num==2:
        return 2
    else:
        return Fibonacci(num-1)+Fibonacci(num-2)

print(Fibonacci(9))       
