import math
#Program to requesting user to select investment or bond calculator. Investment calculator outputs amount invested after given initial input, interest rate, years of investment and type of investment.
#Bond calculates repayment options on a house
#Checks are made to make sure user only inputs investment or bond.
investment_or_bond = input("""Choose either 'investment' or 'bond' from the menu below to proceed:

investment - to calculate the amount of interest you'll earn on your investment'
bond       - to calculate the amount you'll have to pay on your home loan: """).lower()

if investment_or_bond != "investment" and investment_or_bond != "bond":
    print("You did not choose an appropriate answer. Please try again.")


total_invested = ()
if investment_or_bond == "investment":
    deposit_amount = float(input("How much money are you depositing? "))
    interest_rate = float(input("What will your interest rate be? "))
    years_investing = float(input("How many years are you planning to invest for? "))
    interest = input("Do you want simple or compound interest? ")
    if interest == "simple":
        total_invested = round(deposit_amount * (1 + (interest_rate/100)*years_investing),2)
    elif interest == "compound":
        total_invested = round(deposit_amount *  math.pow((1+(interest_rate/100)), years_investing),2)
    print(f"You will have invested £{total_invested}.")
else:
    value_of_house = float(input("What is the current value of the house? "))
    interest_rate_bond = float(input("What will the interest rate be? "))
    months_to_repay = float(input("How many months do you plan to take to repay the bond? "))
    monthly_interest_rate = (interest_rate_bond/100)/12
    monthly_repayments = round((monthly_interest_rate * value_of_house)/(1- ((1 + monthly_interest_rate)**(-months_to_repay))),2)
    print(f"You will have to repay £{monthly_repayments} each month.")