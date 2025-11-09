def prompt(message):
    print(f'==> {message}')

def isint(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def pass_num():
    user_input = input()
    while not isint(user_input):
        user_input = input("That isn't a number. Please enter a number: ")
    return int(user_input)

def valid_op(oper):
    return isint(oper) and int(oper) in [1, 2, 3, 4]

def op():
    op_input = input()
    while not valid_op(op_input):
        op_input = input('''That is not a valid selection. Please select from:
                        1) Add 2) Subtract 3) Multiply 4) Divide''')
    return op_input

def operation(num):
    match (num):
        case '1':
            calculation = num1 + num2
        case '2':
            calculation = num1 - num2
        case '3':
            calculation = num1 * num2
        case '4':
            calculation = num1 / num2
    return calculation


print("Welcome to Calculator.")

prompt('Please input first number.')

num1 = pass_num()

prompt('Please input second number.')

num2 = pass_num()

prompt('''Please select the operation you would like to calculate:
       1) Add 2) Subtract 3) Multiply 4) Divide
       ''')

calc = op()

if calc == '4':
    while num2 == 0:
        prompt('''Cannot divide by zero.
               Please enter a different second number: ''')
        num2 = pass_num()

prompt(f'Your first number is: {num1}')
prompt(f'Your second number is: {num2}')
prompt(f'Your total is: {operation(calc)}')