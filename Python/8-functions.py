#############################################################
#
#   Function is a reusable block of code
#
#   Function's Basic Syntax
#            def function_name(parameters):
#                # code block
#                return value   # optional
#
#   Important Concepts (Must Know)
#            ----------------------------------------   
#            | Concept   | Meaning                  |
#            | --------- | ------------------------ |
#            | Parameter | Input given in function  |
#            | Argument  | Actual value passed      |
#            | Return    | Output from function     |
#            | Global    | Access outside variable  |
#            | Local     | Inside function variable |
#            ----------------------------------------
#
##############################################################

print("---- Example 1. Simple Function (No Parameter) --------")
### greet()     # Error

def greet():
    print("Hello Mahendra")

greet()


print("---- Example 2. Function with Parameter --------")
def greet(name):
    print(f"Hello {name}")

greet("Mahendra")


print("---- Example 3. Function with Return Value --------")
def add(a, b):
    return a+b

relult = add(2, 3)
print(relult)    


print("---- Example 4. Default Parameter --------")

def greet(name="Guest"):
    print(f"Hello {name}")

greet()
greet("Bajpai")


print("---- Example 5. Multiple Return Values --------")
def calc(a, b):
    return a+b, a-b, a*b, a/b

c, d, x, y = calc(6,2)
print(f"Additinon {c} Substraction {d}  Multiplication {x} Division {y}")




print("---- Example 6. Function with Condition --------")
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print( check_even_odd(10) )
print( check_even_odd(9) )    


print("---- Example 7. Function with Loop --------")
def print_numbers(n):
    for i in range(1, n+1):
        print(i)

print_numbers(11)


print("---- Example 8. Real-Life Example (ATM style like your practice) --------")
balance = 9000
def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        return f"Withdraw of {amount} successful. Remaining balance: {balance}"
    else:
        return f"Withdraw of {amount} declined. Isufficient balance"

print( withdraw(2000) )
print( withdraw(8000) )



print("---- Example 9. Real-World Example (Salary Bonus) --------")
def calculate_bonus(salary):
    if salary > 51000:
        bonus = salary * 0.10
    else:
        bonus = salary * 0.05

    return bonus

print( calculate_bonus(60000) )
print( calculate_bonus(30000) )



print("---- Example 10. Function Called Inside Loop --------")
def square(num):
    return num * num

for i in range(1, 10):
    print("Square of ", i, " = ", square(i) )












