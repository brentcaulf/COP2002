#!/usr/bin/env python3

from decimal import Decimal
import locale as lc

#function that calcualtes the monthly payment
def get_month_payment(loan_amount, yearly_rate, years):
    months = years * 12
    monthly_interest_rate = yearly_rate / 12 / 100
    month_payment = Decimal("0.00")

    month_payment = loan_amount * monthly_interest_rate / (1 - 1 / (1 + monthly_interest_rate) ** months)

    month_payment = month_payment.quantize(Decimal("1.00"))
    
    return month_payment

#main function
def main():
    print("Monthly Payment Calculator")
    print()

    choice = "y"
    while choice.lower() == "y":
        #get user input for loan amount, yearly interest rate, and years
        #then convert it to decimal
        print("DATA ENTRY")
        loan_amount = Decimal(input("Loan amount:          "))
        yearly_rate = Decimal(input("Yearly interest rate: "))
        years = int(input("Years:                "))
        #gets the monthly payment
        month_payment = get_month_payment(loan_amount, yearly_rate, years)
        print()

        #print formatted results
        print("FORMATTED RESULTS")
        result = lc.setlocale(lc.LC_ALL, "")
        if result == "C":
            lc.setlocale(lc.LC_ALL, "en_US")
        print("{:25} {:>15}".format("Loan amount:", lc.currency(loan_amount, grouping=True)))
        print("{:25} {:>15}".format("Yearly interest rate:", str(yearly_rate) + "%"))
        print("{:25} {:>15}".format("Number of years:", years))
        print("{:25} {:>15}".format("Monthly payment:", lc.currency(month_payment, grouping=True)))
        print()
        

        choice = input("Continue? (y/n): ")
        print()


if __name__ == "__main__":
    main()
