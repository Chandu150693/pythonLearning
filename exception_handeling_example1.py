try:
    x = int(input("Enter a number : "))
    res = 10/x
    print("Res : ", res)
except ValueError as e:
    print("Invalid input. Please enter a valid number",e)
except ZeroDivisionError:
    print("Can't divide by zero.")
else:
    print("No exceptions occurred.")
finally:
    print("This block always runs.")

# username = raw_input("Enter username:")