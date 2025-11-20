"Loan Calculator"

import os

def prompt(text):
    "Print function"
    print(f'===> {text}')

def auto_or_mortgage(message):
    "Determine auto loan or mortgage"
    prompt(message)
    user_input = input().strip().title()
    while user_input not in ['Auto', 'Mortgage']:
        prompt('That is not a supported loan type. ' \
        'Please select Auto or Mortgage.')
        user_input = input().strip().title()
    if user_input == 'Auto':
        prompt('How many months is your Auto loan for?')
        string = input().strip()
        return auto(string)

    prompt('How many years is your mortgage for?')
    string = input().strip()
    return mortgage(string)

def is_valid_num(num):
    "Verifies valid number input"
    try:
        float(num)
        return True
    except ValueError:
        return False

def loan_value(msg):
    "Establishes initial loan value"
    prompt(msg)
    initial_value = input().strip()
    cleaned_value = initial_value.replace("$", "").replace(",", "")
    while not is_valid_num(cleaned_value) or float(cleaned_value) <= 0:
        prompt(
            'That is not a valid principal amount.'\
            ' Please add valid amount. Example 1000 or $1000')
        initial_value = input().strip()
        cleaned_value = initial_value.replace("$", "").replace(",", "")
    return float(cleaned_value)

def auto(string):
    "Auto loan length validation"
    months = string
    while not is_valid_num(months) or float(months) <= 0:
        prompt('That is not a valid input, please input ' \
        'how many months for your loan term.')
        months = input().strip()
    return int(months)

def mortgage(string):
    "Mortgage length validation"
    years = string
    while not is_valid_num(years) or float(years) <= 0:
        prompt('That is not a valid input, ' \
        'please input how many years for your mortgage term.')
        years = input().strip()
    return int(years) * 12

def interest(message):
    "Interest amount validation"
    prompt(message)
    user_input = input().strip()
    cleaned_user = user_input.replace("%", "")
    while not is_valid_num(cleaned_user) or float(cleaned_user) < 0:
        prompt('That is not a valid input,' \
        ' please input a valid interest rate.')
        user_input = input().strip()
        cleaned_user = user_input.replace("%", "")
    return float(cleaned_user)

def monthly(value, apr, length):
    "Monthly payment calculation"
    if apr == 0:
        payment = value / length
    else:
        apr = apr / 100
        apr = apr / 12
        payment = value * (apr / (1 - (1 + apr) ** (-length) ))
    return payment

def amortization_schedule(
        message, due_monthly, total_balance, apr, remaining_term
        ):
    prompt(message)
    payment = due_monthly
    remaining_balance = total_balance
    term_remaining = remaining_term
    rate_interest = apr/ 100/ 12
    payment_number = 0

    for payment_number in range(1, term_remaining +1):
        interest_charge = remaining_balance * rate_interest
        principal_payment = payment - interest_charge

        if principal_payment > remaining_balance:
            principal_payment = remaining_balance
            actual_payment = interest_charge + principal_payment

        else:
            actual_payment = payment

        remaining_balance = remaining_balance - principal_payment

        print(f'''
            Payment: {payment_number}: ${actual_payment:.2f}\n
            Monthly: ${payment:.2f}\n
            Interest: ${interest_charge:.2f}\n
            principal: ${principal_payment:.2f}\n
            Remaining Balance: ${remaining_balance:.2f}
            ''')

def down_payment_amount(text, loan_amount):
    prompt(text)
    initial_value = input().strip().title()
    while initial_value not in ['Yes', 'No']:
        prompt('That is an invalid response. Please select Yes or No')
        initial_value = input().strip().title()

    if initial_value == 'Yes':
        prompt('How much are you putting down?')
        down_payment = input().strip().replace("$", "").replace(",", "")

        while (not is_valid_num(down_payment) or
               float(down_payment) < 0 or
               float(down_payment) >= loan_amount):
            prompt('That is not a valid down payment amount. '
                   'Must be less than loan amount. Example: 1000 or $1000')
            down_payment = input().strip().replace("$", "").replace(",", "")

        return float(down_payment)

    return 0


def main():
    "main program processing"
    prompt('Welcome to my loan calculator.')

    loan_calc = True

    while loan_calc:
        initial_principal = loan_value(
            'How much money do you need to borrow?'
                               )

        down_payment = down_payment_amount(
            'Do you have a down payment?\n' \
            'Please input Yes or No', initial_principal
        )

        financed_amount = initial_principal - down_payment

        term = auto_or_mortgage(
            'What type of loan are you checking today? Auto or Mortgage?'
                                )

        interest_rate = interest('What is your interest rate?')

        monthly_payment = monthly(financed_amount, interest_rate, term)

        prompt(f'Your initial balance is: ${initial_principal:.2f}')
        prompt(f'Your down payment is: ${down_payment:.2f}')
        prompt(f'Your financed amount is: ${financed_amount:.2f}')
        prompt(f'Your interest rate is: {interest_rate:g} %')
        prompt(f'The duration of your loan is: {term} months')
        prompt(f'Your monthly payment is: ${monthly_payment:.2f}')
        prompt('Would you like to see your amortization schedule?\n' \
        'Yes or No?')

        user_answer = input().strip().title()

        while user_answer not in ['Yes', 'No']:
            prompt('That is an invalid response. ' \
            'Please select Yes or No')
            user_answer = input().strip().title()
        if user_answer == 'Yes':
            amortization_schedule('Your payment breakdown is:',
             monthly_payment, financed_amount, interest_rate, term)

        prompt('Would you like to calculate another loan? Yes or No')

        user_answer = input().strip().title()

        while user_answer not in ['Yes', 'No']:
            prompt('That is an invalid response. ' \
            'Please select Yes or No')
            user_answer = input().strip().title()
        if user_answer == 'No':
            prompt('Thank you for using my loan calculator!')
            loan_calc = False
        else:
            os.system('clear')

main()
