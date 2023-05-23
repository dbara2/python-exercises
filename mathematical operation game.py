#mathematical equation game
#user inputs 2 numbes and what mathematical equation they want done, program does the calculation and gives result
print('This program will ask you for 2 number and do a mathematical operation of them')
first_number = int(input("Please enter the first number "))
second_number = int(input("Please enter the second number "))
math_operation = input("Please enter the operation wanted (+, -, *, /) ")

if math_operation == '+':
    result = first_number + second_number
elif math_operation == '-':
    result = first_number - second_number
elif math_operation == '*':
    result = first_number * second_number
elif math_operation == '/':
    result = first_number / second_number
else:
    print("input not recognized")
print("Your result is " , result)