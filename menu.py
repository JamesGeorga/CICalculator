# This funciton is used to build, maintain and refresh the menu UI for the program.

import os
import platform
from monthly import monthly

def menu(loan_amount, Term, Rate):

    # refresh on call
    if platform.system() == "Windows":
        os.system("cls")  # Windows command
    else:
        os.system("clear")  # Linux/macOS command

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