"""My Simple Calculator Program"""
import json

with open('calculator_messages.json', 'r', encoding='utf-8') as file:
    all_messages = json.load(file)

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

def pass_num(message):
    """Passes a valid number from user input"""
    user_input = input().strip()
    while not is_valid_num(user_input):
        prompt(message['invalid_num'])
        user_input = input().strip()
    return float(user_input)

def valid_op(oper):
    """Checks user input to insure valid selection"""
    return is_valid_num(oper) and float(oper) in [1, 2, 3, 4]

def prompt_for_operation(msg):
    """Error handling for invalid operation selection"""
    prompt(msg['operation_selection'])
    op_input = input().strip()

    while not valid_op(op_input):
        prompt(msg['valid_op'])
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

def main():
    """Main calculation processing"""
    prompt('Language:\n1) English\n2) Spanish\n3) Portugese\n4) German')
    lang_choice = input().strip()

    while lang_choice not in ['1', '2', '3', '4']:
        prompt('''That is an invalid selction, please select:
            \n1) Enlgish\n2) Spanish\n3 Portugese\n4) German''')
        lang_choice = input().strip()

    lang_map = {'1': 'english', '2': 'spanish', '3': 'portuguese', '4': 'german'}
    lang = lang_map[lang_choice]

    messages = all_messages[lang]
    prompt(messages['welcome'])

    continue_calc = True

    while continue_calc:

        prompt(messages['first_num'])

        num1 = pass_num(messages)

        prompt(messages['second_num'])

        num2 = pass_num(messages)

        calc = prompt_for_operation(messages)

        if calc == '4':
            while num2 == 0.0:
                prompt(messages['div_by_zero'])
                num2 = pass_num(messages)

        prompt(f"{messages['result_first']} {num1}")
        prompt(f"{messages['result_second']} {num2}")
        prompt(f"{messages['result_total']} {operation(num1, num2, calc)}")
        prompt(messages['continue_calculation'])

        answer = input()

        user_answer = answer.strip().title()

        while user_answer not in [messages['yes_response'], messages['no_response']]:
            prompt(messages['continue_invalid_input'])
            user_answer = input().strip().title()

        if user_answer == messages['no_response']:
            prompt(messages['thank_you'])
            continue_calc = False
main()
