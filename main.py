# This program is designed to calculate the cumulative interest of a sum of money. Given an percentage
# interest rate.

from menu import menu

def main():
    end = 0

    # Default input values
    loan_amount = 300000
    Term = 10
    Rate = 5.84


    while not end:
        # run the main menu 
        print('Loading the menu')
        menu(loan_amount, Term, Rate)

    return # end main

if __name__ == "__main__":
    main()