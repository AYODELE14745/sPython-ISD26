#%%  Introduction to Python Programming II
# Section 1: Comparisons and Conditionals 
## Exercise 1: Comparison Operators

x = 10
y = 3

print(x == y)

x = 10
y = 3

print(x != y)

x = 10
y = 3

print(x > y)

x = 10
y = 3

print(x < y)

x = 10
y = 3

print(x >= y)

x = 10
y = 3

print(x <= y)

# %%
## Exercise 2: Logical Operators

x = 10

print(x > 5 and x < 20)

x = 10

print(x > 5 or x < 9)

x = 10

print(not(x > 5 and x < 20))

# %%
## Exercise 3: if-Conditionals

age = 19
age_group = "child"

if age > 18:
    age_group = "adult"

print(f"The age group is {age_group}")

age = 17
age_group = "child"

if age > 18:
    age_group = "adult"

print(f"The age group is {age_group}")

#%%
## Exercise 4: if-else Conditionals

wind_speed = 30

if wind_speed < 10:
    print("It is a calm day")
else:
    print("It is a windy day")

wind_speed = 8

if wind_speed < 10:
    print("It is a calm day")
else:
    print("It is a windy day")

#%%
## Exercise 5: if-elif-else Conditionals

grade = 45

if grade < 40:
    print("You failed")
elif grade < 50:
    print("You passed")
elif grade < 55:
    print("You got a good pass")
else:
    print("You got an exellent pass")

# %%
## Exercise 5: Summary task

Temperature_1 = 30
Temperature_2 = 40

if Temperature_1 > Temperature_2:
    print("Temperature are equal")
else:
    print("Temperatures are not equal")

#%%
# Section 2: Python Lists
## Exercise 1: Creating a list

City_list = ["Glasgow", "London", "Edinburgh"]

# %%
## Exercise 2: Accessing a list

City_list = ["Glasgow", "London", "Edinburgh"]

City_list[1:3]

#%%
City_list = ["Glasgow", "London", "Edinburgh"]

City_list[2]

# %%
## Exercise 3: Modifying a list

City_list = ["Glasgow", "London", "Edinburgh"]

City_list.append("Manchester")
print(City_list)

#%%
City_list = ["Glasgow", "London", "Edinburgh"]

City_list[1] = "Birmingham"
print(City_list)

# %%
## Exercise 4: Summary Task
### Task 1: Create

Colours = ["Red", "Blue", "White"]
print(Colours)

# %%
### Task 2: Access

Colours = ["Red", "Blue", "White"]

Colours[1]

# %%
### Task 3: Modify

Colours = ["Red", "Blue", "White"]

Colours[0] = "Green"
print(Colours)

# %%
### Task 4: Print length

Colours = ["Red", "Blue", "White"]

print(len(Colours))

# %%
### Task 5: Conditional ***** not done yet

Colours = ["Red", "Blue", "White"]

if "Red" in Colours:
    print("Red is in the list")

# %%
### Task 6: Using Slicing

Colours = ["Red", "Blue", "White"]

Selected_colours = Colours[1:4]
print(Selected_colours)

# %%
# Section 3: Python Loops
##Exercise 1: While loops

i = 0
while i < 5:
    print(i)
    i += 1

#%%
##Exercise 2: For loops

City_list = ["Glasgow", "London", "Edinburgh"]

for city in City_list:
    print(city)

# %%
##Exercise 3: Loop Keywords: Range, break and continue

for i in range(5):
    if i == 3:
        break
    print(i)

# %%
##Exercise 3: Loop keyword: Continue

for i in range(5):
    if i == 2:
        continue
    print(i)

# %%
##Exercise 4: Summary tasks
### Task – Even Numbers 

Numbers = list(range(1, 11))

for i in Numbers:
    if i % 2 == 0:
        print(i)

# %%
### Task – Sum of Squares 

sum_of_squares = 0

for i in range(1, 6):
    sum_of_squares += i ** 2

print(sum_of_squares)


# %%
### Task – Countdown

countdown = 10

while countdown >= 1:
    print(countdown)
    countdown -= 1
print("Liftoff!")

# %%
# Section 4: Obtaining User Input 
## Exercise 1:  User Input Tasks 
### Task 1: User Input and Conditional Statements 

age = int(input("How old are you?"))
if age < 18:
    print("You are a minor")
elif 18 <= 18 <= 65:
    print("You are an adult")
else:
    print("You are a senior citizen")

# %%
### Task 2: Temperature Converter 

print("Welcome to the Temperature Converter!")
Celcius_input = float(input("Enter temperature in degree celsius:"))
degree_f = (Celcius_input * 9/5) + 32
degree_k = Celcius_input + 273.15

print("The temperature you have entered is", Celcius_input, "degree celsius.")
print("Converted Temperature:")
print(Celcius_input, "degree celsius is equal to", degree_f, "Fahrenheit.")
print(Celcius_input, "degree celsius is equal to", degree_k, "kelvin.")


print("Thank you for using the Temperature Converter!")
