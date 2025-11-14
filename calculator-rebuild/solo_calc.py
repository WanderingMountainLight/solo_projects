"""My Simple Calculator Program"""

def prompt(message):
    """Display a formatted message to the user"""
    print(f'==> {message}')

def is_valid_num(num):
    """Checks if provided string can be converted to a float"""
    try:
        float(num)
        return True
    except ValueError:
        return False

def pass_num():
    """Passes a valid number from user input"""
    user_input = input().strip()
    while not is_valid_num(user_input):
        prompt("That isn't a number. Please enter a number: ")
        user_input = input().strip()
    return float(user_input)

def valid_op(oper):
    """Checks user input to insure valid selection"""
    return is_valid_num(oper) and float(oper) in [1, 2, 3, 4]

def op():
    """Error handling for invalid operation selection"""
    op_input = input().strip()
    while not valid_op(op_input):
        prompt('''That is not a valid selection. Please select from:
                        1) Add 2) Subtract 3) Multiply 4) Divide''')
        op_input = input().strip()
    return op_input

def operation(number1, number2, op_choice):
    """Operation evaluation"""
    match (op_choice):
        case '1':
            return number1 + number2
        case '2':
            return number1 - number2
        case '3':
            return number1 * number2
        case '4':
            return number1 / number2


print("Welcome to Calculator.")

prompt('Please input first number.')

num1 = pass_num()

prompt('Please input second number.')

num2 = pass_num()

prompt('''Please select the operation you would like to calculate:
        1) Add
        2) Subtract
        3) Multiply
        4) Divide
       ''')

calc = op()

if calc == '4':
    while num2 == 0.0:
        prompt('''Cannot divide by zero.\nPlease enter a different second number: ''')
        num2 = pass_num()

prompt(f'Your first number is: {num1}')
prompt(f'Your second number is: {num2}')
prompt(f'Your total is: {operation(num1, num2, calc)}')
