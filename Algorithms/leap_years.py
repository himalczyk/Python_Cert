ask_for_number = int(input("Type year and confirm with enter: \n"))

if (ask_for_number % 4 == 0 and ask_for_number % 100 != 0) or ask_for_number % 400 == 0:
    print("Leap year")
else:
    print("Not a leap year")