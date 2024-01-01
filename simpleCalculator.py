def calculator(a,b,operator):
    if operator == '+':
        print(a+b)
    elif operator == '-':
        print(a - b)
    elif operator == '*':
        print(a *b)
    elif operator == '/':
        print(a / b)
    else:
        print("Invalid operator")

num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
op = str(input("Enter any one of four basic operator"))
calculator(num1,num2,op)