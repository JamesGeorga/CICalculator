# this funciton is used to build and maintain the menu UI for the program.

import os
import time
from monthly import monthly

def menu(loan_amount, Term, Rate):

    select = 0

    # refresh on call
    os.system('clear') # linux command

    # Title
    print('=========[ Cumuative Interest Calculator v0.0.1 ]=========')
    print('')

    # display saved valueus screen
    print(f"[Loan Amount: ${loan_amount:,}] ", end='')
    print(f"[Term: {Term:,} Years] ", end='')
    print(f"[Interest Rate: {Rate:,}%] ", end='')
    print('\n')

    # display calculations
    print(f"- Required Monthly payments: ${monthly(loan_amount, Term, Rate)} ")
    print(f"- Required Monthly payments: ${monthly(loan_amount, Term, Rate)} ")
    print('\n')

    # Show user the available funcitons
    print('To change loan amount, press 1')
    print('To change the term, press 2')
    print('To change the interest rate, press 3')

    # successful selection
    select = int(input())

    if select == 1:
        print('You selected "Change Values"')
        time.sleep(3)

    return 