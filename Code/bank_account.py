interest_level = int(input("Oprocentowanie: \n"))
investment_years = int(input("Lata na lokacie: \n"))
deposit_sum = int(input("Wprowadz kwote: \n"))

total_deposit = deposit_sum * ((1 + interest_level/100) ** investment_years)

print(f"Suma na lokacie po {investment_years} latach to: {total_deposit}")