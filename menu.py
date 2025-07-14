
# this funciton is used to build and maintain the menu UI for the program.

import os
import time

def menu(loan_ammount, Term, Rate):

    select = 0

    # refresh on call
    os.system('clear') # linux command

    # Title
    print('[ Cumuative Interest Calculator v0.0.1 ]')
    print('')

    # display saved valueus screen
    print('[Loan Ammount: $',loan_ammount, '] ', end='')
    print('[Term: ',Term, 'Years ] ', end='')
    print('[Interest Rate: ',Rate, '% ] ', end='')
    print('\n')

    # Show user the available funcitons
    print('To change values, press 1')
    print('To calculate Minimum monthly repayments, press 2')

    # successful selection
    select = int(input())

    if select == 1:
        print('You selected "Change Values"')
        time.sleep(3)
    if select == 2:
        print('You selected "Calculate Time"')
        time.sleep(3)



    return 