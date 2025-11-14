"""My Simple Calculator Program"""
import json

with open('calculator_messages.json', 'r', encoding='utf-8') as file:
    messages = json.load(file)

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
        prompt(messages['invalid_nums'])
        user_input = input().strip()
    return float(user_input)

def valid_op(oper):
    """Checks user input to insure valid selection"""
    return is_valid_num(oper) and float(oper) in [1, 2, 3, 4]

def op():
    """Error handling for invalid operation selection"""
    op_input = input().strip()
    while not valid_op(op_input):
        prompt(messages['valid_op'])
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


prompt(messages['welcome'])

continue_calc = True

while continue_calc:

    prompt(messages['first_num'])

    num1 = pass_num()

    prompt(messages['second_num'])

    num2 = pass_num()

    prompt(messages['operation_selection'])

    calc = op()

    if calc == '4':
        while num2 == 0.0:
            prompt(messages['div_by_zero'])
            num2 = pass_num()

    prompt(f'Your first number is: {num1}')
    prompt(f'Your second number is: {num2}')
    prompt(f'Your total is: {operation(num1, num2, calc)}')
    prompt(messages['continue_calculation'])

    answer = input()

    user_answer = answer.strip().title()

    while user_answer not in ['Yes', 'No']:
        prompt(messages['continue_invalid_input'])
        user_answer = input().strip().title()

    if user_answer == 'No':
        prompt(messages['thank_you'])
        continue_calc = False
