# This program is designed to calculate the cumulative interest of a sum of money. Given an percentage
# interest rate.

import time
from menu import menu

def main():

    # variables
    end = 0
    select = 0
    call_menu = 0

    # Default input values
    loan_amount = 300000
    Term = 10
    Rate = 5.84


    while not end:
        # display the menu UI
        print('Loading the menu')
        menu(loan_amount, Term, Rate)

        # Show user the available funcitons
        match call_menu:
            case 0: # starting functions
                print('To change loan amount, press 1')
                print('To change the term, press 2')
                print('To change the interest rate, press 3')
            case 1: # user wants to change the loan amount
                print('*Run the change value code*')

        # check successful selection
        select = int(input())
        call_menu = select

        match select:
            case 1:
                print('You selected "Change loan"')
                time.sleep(2)
            case 2:
                print('You selected "Change term"')
                time.sleep(2)
            case 3:
                print('You selected "Change rate"')
                time.sleep(2)
            case _:
                print('invalid selection')
                time.sleep(2)


    return # end main

if __name__ == "__main__":
    main()