def add(n1, n2):
    return(n1+n2)

def subtraction(n1,n2):
    return(n1-n2)

def multiplication(n1,n2):
    return(n1*n2)

def division(n1,n2):
    if(n2!=0):
        return(n1/n2)
    else:
        return("cannot divide by zero")




num1=float(input("enter the number 1 :"))
num2=float(input("enter the number 2 :"))
 
choice=input("choose operation(+,-,*,/) :")


if(choice=='+'):
    result=add(num1,num2)
elif(choice=='-'):
    result=subtraction(num1,num2)
elif(choice=='/'):
    result=division(num1,num2)
elif(choice=='*'):
    result=multiplication(num1,num2)

else:
    print("enter the valid input")

print(result)

        
        

