"Loan Calculator"

#import os

def prompt(text):
    "Print function"
    print(f'===> {text}')

def auto_or_mortgage(message):
    "Determine auto loan or mortgage"
    prompt(message)
    user_input = input().strip().title()
    while user_input not in ['Auto', 'Mortgage']:
        prompt('That is not a supported loan type. Please select Auto or Mortgage.')
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
    while not is_valid_num(cleaned_value):
        prompt('''That is not a valid principle amount. Please add valid amount.
               Example 1000 or $1000''')
        initial_value = input().strip()
        cleaned_value = initial_value.replace("$", "").replace(",", "")
    return float(cleaned_value)

def auto(string):
    "Auto loan length validation"
    months = string
    while not is_valid_num(months):
        prompt('That is not a valid input, please input how many months for your loan term.')
        months = input().strip()
    return float(months)

def mortgage(string):
    "Mortgage length validation"
    years = string
    while not is_valid_num(years):
        prompt('That is not a valid input, please input how many years for your mortgage term.')
        years = input().strip()
    return float(years) * 12

def interest(message):
    "Interest amount validation"
    prompt(message)
    user_input = input().strip()
    cleaned_user = user_input.replace("%", "")
    while not is_valid_num(cleaned_user):
        prompt('That is not a valid input, please input a valid interest rate.')
        user_input = input().strip()
        cleaned_user = user_input.replace("%", "")
    return float(cleaned_user)

def monthly(value, apr, length):
    "Monthly payment calculation"
    apr = apr / 100
    apr = apr / 12
    payment = value * (apr / (1 - (1 + apr) ** (-length) ))
    return payment

def main():
    "main program processing"
    prompt('Welcome to my loan calculator.')

    loan_calc = True

    while loan_calc:
        principle = loan_value('How much money do you need to borrow?')

        term = auto_or_mortgage('What type of loan are you checking today? Auto or Mortgage?')

        interest_rate = interest('What is your interest rate?')

        monthly_payment = monthly(principle, interest_rate, term)

        prompt(f'Your initial balance is: ${principle:.2f}')
        prompt(f'Your interest rate is: {interest_rate}%')
        prompt(f'The duration of your loan is: {term} months')
        prompt(f'Your monthly payment is: {monthly_payment:.2f}')

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
            loan_calc = True

main()
