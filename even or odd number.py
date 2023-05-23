#even or odd  number
number = int(input("Please enter a number and I'll tell you if it's even or odd: "))
modulus = number % 2
multipleofFour = number % 4

#doing the calculation to see if the number given gives a modules of zero
if modulus == 0 and multipleofFour == 0:
    print(f"{number} is even and divisible by 4!")
elif modulus == 0 and multipleofFour != 0:
    print(f"{number} is even but not divisible by 4")
else: 
    print(f"{number} is odd")