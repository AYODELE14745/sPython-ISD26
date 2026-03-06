# Python Functions, Scope and Errors
## Section 1: Functions and scope
### Exercise 1: Functions in Python
#%% 
### Creating Funtions

def greet_user():
    print("Hello")

# %%
### Function Parameters

def gree_user(name):
    print(f"Hello {name}!")

def greet_user(first_name, last name):
    print(f"Hello {first_name} {last_name}!")

# %%
### Keywird Arguments

gree_user(last_name="Omitoyaki", first_name="Ayodele")

# %%
### Default Values

def greet_user(first_name, last_name, university="UWS"):
    print(f"Hello {first_name} {last_name} from {university}!")

# %%
## Task 1: Greeting message

friend_list = ["John", "Jane", "Jack"]
greet_friends = friend_list
for i in range(0, 1, 2):
    print(f"Hello {friend_list[0]}!")
    print(f"Hello {friend_list[1]}!")
    print(f"Hello {friend_list[2]}!")

#%%
### Return

def add_numbers(num1, num2):
    return num1 + num2
result = add_numbers(5, 10)
print(result)

#%% 
def add_and_multiply_numbers(num1, num2):
    sum = num1 + num2
    product = num1 * num2
    return sum, product

sum, product = add_and_multiply_numbers(5, 10)
print(sum)
print(product)

# %%
## Task 2: Tax Calculation

def calculate_tax(income, tax_rate):
    tax_amount = income * tax_rate
    return tax_amount
tax_amount = calculate_tax(60000, 0.3)
print(tax_amount)

# %%
## Task 3: Compound Interest Calculator Function

def compound_interest(principal, duration, interest_rate):
    if interest_rate < 0 or interest_rate > 1:
        print("Please enter a decimal number between 0 and 1")
        return None
    
    if duration < 0:
        print("Please enter a positive number of years")
        return None

    for year in range(1, duration + 1):
        total_for_the_year = principal * (1 + interest_rate) ** year
        print(f"The total amount of money earned by the investment in year {year} is {total_for_the_year:.2f} £")

    return int(total_for_the_year)

# %%
### Exercise 2: Variable Scope
def new_funtion():
    my_new_variable = 5

new_funtion()

my_new_variable = 0

def new_function():
    my_new_variable = 5

new_function()

print(my_new_variable)

#%%
## Section 2: Assertions and Errors
### Exercise 3: Assertions

assert compound_interest(1000, 5 0.03) == 1159

#%%
### Task 1: Assertion

assert 10 > 9, "10 is not greater than 9"
#%%
assert 9 > 10, "9 is not greater than 10"

# %%
### Exercise 4: Identifying and Fixing Common Errors

print("Hello World!")


# %%
print("My favorite color is Blue")
# %%
Number1 = 5
Number2 = 3
result = Number1 + Number2
print("The sun is:", result)
# %%
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
# %%
time = 11
if time <= 12:
    print("Good morning!")
