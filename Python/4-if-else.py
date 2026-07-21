################################################################
#       👉 Clean indentation = important (no {} like PHP)
#
#        if condition:
#            # runs if condition is True
#        else:
#            # runs if condition is False
#
#
################################################################

print('------- Example-1 --------------------------')
age = 18
if age >= 18:
    print('You can vote')
else:
    print('You can not vote')


print('------- Example-2 --------------------------')
password = '1234'   
if '1234'== password:   # == means compare values
    print('Login Successful')
else:
    print('Wrong Password')


print('------- Example-3 Even or Odd--------------------------')
number =7
if number % 2 ==0:  # % = remainder
    print('Even Number')
else:
    print('Odd Number')


print('------- Example-4  elif Multiple Conditions ----------------------')
marks = 75
if marks >= 90:
    print('Grade A')
elif marks >= 60:
    print('Grade B')
else:
    print('Failed')




print('------- Example-5  Taking Input ----------------------')
age = input('Enter your age :')
age = int(age)
if age >= 18:
    print('Adult')
else:
    print('Minor')


print('------- Example-6  Nested if  ----------------------')
age = 12
has_id = True
if age >= 18:
    print('Adult')
    if has_id:
        print('Entry Allowed')
    else:
        print('ID requried')
else:
    print('Underage')



















