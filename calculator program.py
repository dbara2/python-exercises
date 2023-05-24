#calculator program
print("This program will ask you for 2 numbers and do a mathematical equation of your choice between them")
first_number = int(input("Please enter the first number: "))
second_number = int(input("Please enter the second number: "))
mathematical_equation = input("Please enter the operation wanted (+, -, *, /) ")

#if loops for each mathematical equation
if mathematical_equation == '+':
    result = first_number + second_number
elif mathematical_equation == '-':
    result = first_number - second_number
elif mathematical_equation == '*':
    result = first_number * second_number
elif mathematical_equation == '/':
    result = first_number / second_number
else:
    print('Error, your input was not recognized')
#printing the result, formated to include the result variable with a string
print(f"Your result is {result}!")
