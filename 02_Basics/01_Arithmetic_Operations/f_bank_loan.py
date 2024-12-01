"""
Purpose: Bank Loan

    Simple Interest : A = P (1 + rt)

                        A	=	final amount
                        P	=	initial principal balance
                        r	=	annual interest rate
                        t	=	time (in years)

Ref :https://www.calculatorsoup.com/calculators/financial/simple-interest-plus-principal-calculator.php

"""

# 1. Simple Interest

def simple_interest(principal, rate, time):
    simple_interest= principal * rate * time
    return simple_interest

principal = float(input("Enter the principal amount: "))
annual_rate = float(input("Enter the annual interest rate (in %): ")) / 100
time = float(input("Enter the time period (in years): "))
simple_interest = simple_interest(principal, annual_rate, time)
print("Simple Interest: ", simple_interest )


# 2. Compound Interest Calculation

def compound_interest(principal, rate, time, n=12):
    amount = principal * (1 + rate / n) ** (n * time)
    interest = amount - principal
    return interest

principal = float(input("Enter the principal amount: "))
annual_rate = float(input("Enter the annual interest rate (in %): ")) / 100
time = float(input("Enter the time period (in years): "))
compound_interest = compound_interest(principal, annual_rate, time)
print("Compound Interest: ", compound_interest)