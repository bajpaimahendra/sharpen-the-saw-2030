###############################################
#   Variables                                 
#       - variable is a memory location
#       - No type declaration! /   No need to define data-type / loosly coupled language
#   Python → no $ 
#   PHP → must use $    
# Both languages are dynamically typed.
#
########################## QnA #########################################################
# Q-1   What is an f-string?
#       f-string = formatted string
#       It is a way to insert variables directly inside a string using {}
#       print(f"My name is {name} and I am {age}")
# Q-2   Why is it called "f-string"?
#       Because we write f before the string:
#       f"..."
#       The f tells Python: "Hey, this string contains variables → replace {} with values"
#
#########################################################################################

# EXAMPLE-1 variable assignment and print
# # no var, no $, no type

name = 'Mahendra'   # string  
age = 30            # int
salary = 500.50     # float
is_active = True    # boolean

# print variable value, like echo in php
print(name, age, salary, is_active)


# EXAMPLE-2 check data-type of variable
print( type(name) );   # <class 'int'>     echo gettype($x); // integer

# EXAMPLE-3 Multiple Assignment
a, b, c = 1, 2, 3
print(a, b, c) 


# EXAMPLE-4 Constants , Python doesn’t enforce constants — just naming convention (UPPERCASE)
# define("PI", 3.14);PHP (actual constant)
PI = 3.14  
print (PI)  

print("----- EXAMPLE-5 Type-Conversion / Type-Casting ------")
### PHP $x = "10"; $y = (int)$x;
x = "9"
print(x); print(type(x))
y = int(x)
print(y); print(type(y))


print("----- EXAMPLE-6  string concatenation ------")
name ='Mahendra'
age = 30
print(f"My name is {name} and I am {age}") # use f-strings (clean + powerful)
print("My name is {} and I am {}".format(name, age))

# Note : 👉 {} is used for: 
#    1- Insert variables in strings (f-strings)
#    2- Create dictionaries
#    3- Create sets


print('---------- EXAMPLE-7 String + Number Behavior ----------')
age = 25
#print ( "my age "+" is "+age )   # ❌ Error
print ( "my age "+" is "+str(age) )


print('---------- Exercise 1 ----------')
name ='Mahendra'; age = 30; # two statement in same line , terminated by semicolon(;)
print(name, age)



print('---------- Exercise 2 ----------')
a = 10
b = 20
a, b = b, a  # swap 
print(a, b)

print('---------- Exercise 3 ----------')
num = "50"
print( int(num)+10 )

print('---------- Exercise 4 ----------')
price = 99.5
quantity = 2
total = price*quantity
print("Total : ", total)


















