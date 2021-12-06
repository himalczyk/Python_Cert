interest_level = int(input("Interest: \n"))
investment_years = int(input("Years in deposit: \n"))
deposit_sum = int(input("Provide the sum: \n"))

total_deposit = deposit_sum * ((1 + interest_level/100) ** investment_years)

print(f"The sum in the deposit after {investment_years} years is: {total_deposit}")