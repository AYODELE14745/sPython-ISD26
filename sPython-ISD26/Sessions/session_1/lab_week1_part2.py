# Session 1 Section 2 Python Introduction

#%%
#exercise 1 task 1: Variables and Types

var_1 = True #Type = Boolean
var_2 = 1 #Type = integer 
var_3 = 3.14159 #Type = float
var_4 = "Hello World" #Type = Str

print(type(var_1))
print(type(var_2))
print(type(var_3))
print(type(var_4))

#%%
#exercise 1 task 2: Casting Variables
my_int = int(5)
my_float = float(5.5)
my_bool = bool(True)

print(my_int)
print(my_float)
print(my_bool)

my_int_float = float(my_int)
my_float_int = int(my_float)
mybool_int = int(my_bool)

print("after casting")
print(my_int_float)
print(my_float_int)
print(mybool_int)

#%%
#exercise 2 task 1: Arithmetic operators
#Addition
result_addition = 10 + 5
print("Addition", result_addition)

#Subtraction
result_subtraction = 20 - 8
print("Subtraction", result_subtraction)

#Multiplication
result_multiplication = 6 * 4
print("Multiplication", result_multiplication)

#Division
result_division = 15 / 3
print("Division", result_division)

#Floor Division
result_floor_division = 17 // 4
print("floor division", result_floor_division)

#Modulus
result_modulus = 17 % 4
print("modulus", result_modulus)

#Exponentiation
result_exponentiation = 2 ** 3
print("exponentiation", result_exponentiation)


#%%
# Exercise 2 task 2: Calculating the average

numbers = (2, 16, 22)
average = sum(numbers) / len(numbers)
print(f"num1: 2")
print(f"num2: 16")
print(f"num3: 22")
print("average of 3 numbers", average)


# %%
# Exercise 2 task 3: Calculate the area of a rectangle

length = 8
width = 4
print(f"length: 8")
print(f"width: 4")
print(f"area of the rectangle: {length * width}")

# %%
# Exercise 3 task 1: Modify strings

my_string = "This class covers ISD"
print(my_string)

my_uppercase_string = my_string.upper()
print(my_uppercase_string)

my_lowercase_string = my_string.lower()
print(my_lowercase_string)

my_new_string = my_string.replace("ISD", "Interactive Software Design")
print(my_new_string)

my_string_length = my_new_string
print(len(my_new_string))


# %%
# Exercise 3 task 2: f-strings

my_name = "Ayodele Joseph Omitoyaki"
number_of_classes = 3
campus = "Paisley"
my_text = (f"My name is {my_name} and i am studying {number_of_classes} classes in {campus}.")
print(my_text)

# %%
# Section 2: First program in Python

#Temperature Converter
Celcius_input = 20
Celcius_input = float(Celcius_input)
degree_f = (Celcius_input * 9/5) + 32
degree_k = Celcius_input + 273.15


print(f"{Celcius_input} degree celcius is equal to {degree_f:.2f} Fahrenheit.")
print(f"{Celcius_input} degree celcius is equal to {degree_k:.2f} Kelvin.")
print("Thank you for using the Temperature Converter!")
