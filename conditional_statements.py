######################################################################
######################################################################
'''SIMPLE IF'''








#######################################################################
#######################################################################
'''IF ELSE'''








#######################################################################
#######################################################################
'''ELIF'''
54. Write a program to check the relation between two integer numbers

num_1= int(input("enter the num 1: "))
num_2= int(input("enter the num 2: "))

if num_1 == num_2:
    print('Both Numbers are equal')
elif num_1 > num_2:
    print("Number 1 is greater than Number 2")
else:
    print("Number 2 is greater")

55. Write a program to check whether a given character is uppercase or lowercase or number. If character is uppercase print uppercase, If character is lowercase print lowercase. If the character is a number, print the ascii number of it.

char = input("Entrer a char: ")
if char.isnumeric():
    print(ord(char))
elif char.isupper():
    print("Char is upper case")
elif char.islower():
    print("char is lower case")
else:
    print("char is nither upper case nor lowercase nor number")

56. Write a program to check whether a given character is a vowel or consonant. If a given character is a vowel, store the character inside the list. If a given character is consonant, display the ASCII value of that character.

character = input("enter a alphabet: ")
vovel= []
if character.lower() in ['a','i','o','u','e']:
    vovel.append(character)
elif character.lower() in "bcdfghjklmnpqrstvwxyz":
    print(ord(character))
else:
    print("It is not an alphabet")

57. Write a program to check whether a given character is uppercase. If it is uppercase, convert it to lowercase.Else PRINT LOWERCASE.

char= input("enter a alphabet: ")

if char.isupper():
    print(char.lower())
else:
    print("It LOWER CASE")

58. Write a program to checkWhether the entered character is a number. If it is a number, print the ASCII value of that number.

character = input("Enter a character: ")

if character.isdigit():
    ascii_value = ord(character)  
    print(f"The ASCII value of '{character}' is: {ascii_value}")
else:
    print(f"The character '{character}' is not a number.")


59. Write a program to check whether given character is uppercase, print its lowercase character or if given character is lowercase print its uppercase character or if given character is special character print the character after adding 8 to the ascii value of that particle special character

char = input("enter the char: ")
if char.isupper():
    print(char.lower())
elif char.islower():
    print(char.upper())
elif char.isnumeric():
    print("Invalid Input")
else:
    print(ord((char))+8)
    
60. Write a program to check whether the last character of a given string is a special character or not.

char = input("enter a string: ")
if char[-1].isalnum():
    print("It is not a special character")
else:
    print("It is a special character")

61. Write a program to check if the middle value of heterogeneous tuple collection is integer or not.

tpl= eval(input("enter a tupple: "))
mid_index= len(tpl) // 2
mid_value = tpl[mid_index]

if type(mid_value) == int:
    print("The middle value is Integer")
else:
    print("The middle value is not integer")

71. Write a program to calculate the electricity bill.According to the following criteria, for 1st 100 units there is no charge, For next 100 units there is ₹5 per unit and after 200 units, the price is rupees 10 per unit.If the input is 350 then total bill amount is Rupees 2000.

units= int(input("Enter the units: "))
Total_Bill= 0.0

if 0 <= units <= 100:
    Total_Bill = 0.0
elif 0<= units <= 200:
    Total_Bill = (units-100)*5
elif units > 200:
    Total_Bill = (units-200)*10 + (100*5)

print(f"The total bill for {units} units is Rs {Total_Bill}")

80. WAP to convert temperature from celsius to kelvin and kelvin to celsius using the elif statement.

print("Temperature Conversion Options: \n1. Celsius to Kelvin \n2. Kelvin to Celsius")
choice = input("Enter the number of your choice (1 or 2): ")
if choice == '1':
        # Convert Celsius to Kelvin
        celsius = float(input("Enter temperature in Celsius: "))
        kelvin = celsius + 273.15
        print(f"{celsius} Celsius is equal to {kelvin:.2f} Kelvin.")
elif choice == '2':
        # Convert Kelvin to Celsius
        kelvin = float(input("Enter temperature in Kelvin: "))
        celsius = kelvin - 273.15
        print(f"{kelvin} Kelvin is equal to {celsius:.2f} Celsius.")
        
else:
        print("Invalid choice. Please enter 1 or 2.")




#######################################################################
#######################################################################
'''NESTED IF'''

82). Write a program to print middle value of the given heterogeneous tuple collection only if the middle value is string and having the length greater than 3 

tpl = eval(input("Enter a Tuple: "))    

mid_index = len(tpl) // 2
middle_value = tpl[mid_index]

if type(middle_value) == str:
    if len(middle_value) > 3:
        print(middle_value)
    else:
        print("It is a string but the length is not greater than 3")
else:
    if type(middle_value) != str:
        print("the mid vale is not string")
      




#######################################################################
#######################################################################
