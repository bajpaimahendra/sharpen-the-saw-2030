################## 1- Comparison Operators (Most Used) #############################################
#           
#        | Operator | Meaning          |
#        | -------- | ---------------- |
#        | `==`     | equal            |
#        | `!=`     | not equal        |
#        | `>`      | greater          |
#        | `<`      | smaller          |
#        | `>=`     | greater or equal |
#        | `<=`     | smaller or equal |
#
################# 2- Logical Operators (Combine Conditions) ##########################################
#
#        | Operator | Meaning           |
#        | -------- | ----------------- |
#        | `and`    | both must be True |
#        | `or`     | any one True      |
#        | `not`    | reverse           |
#
################## 3- Arithmetic Operators (Used in Conditions) ########################################
#
#        | Operator | Meaning        |
#        | -------- | -------------- |
#        | `+`      | add            |
#        | `-`      | subtract       |
#        | `*`      | multiply       |
#        | `/`      | divide         |
#        | `%`      | remainder      |
#        | `//`     | floor division |
#
################## 4- Assignment Operators #################################################################
#
#        | Operator | Meaning             |
#        | -------- | ------------------- |
#        | `=`      | assign              |
#        | `+=`     | add and assign      |
#        | `-=`     | subtract and assign |
#
################# 5- Membership Operators ####################################################################
#
#        | Operator | Meaning        |
#        | -------- | -------------- |
#        | `in`     | exists         |
#        | `not in` | does not exist |
#
################ 6- Identity Operators #########################################################################
#
#        | Operator | Meaning     |
#        | -------- | ----------- |
#        | `is`     | same object |
#        | `is not` | not same    |
#
#################################################################################################################
print("----------- Example-1: Salary Check ---------------")
salary = 100000
if salary > 90000:
    print("Good Salary")
else:
    print("Low Salary")


print("----------- Example-2: Login (== and !=) ---------------")
password = "admin123"
if password != "admin123":
    print("Login Success")
else:
    print("Wrong Password")


print("----------- Example-3: Age + ID Check (and) ---------------")
age = 20
has_id = True
if age >= 18 and has_id:
    print("Allowed")
else:
    print("Not Allowed")


print("----------- Example-4: Weekend Check (or) ---------------")    
day = "Sunday"
if day == 'Saturday' or day == 'Sunday':
    print("Holiday")
else:
    print("Working day")


print("----------- Example-5: NOT operator ---------------") 
is_logged_in = False
if not is_logged_in:
    print("Please Login")
else:
    print("Welcome")



print("----------- Example-6: remainder (%) ---------------") 
num =10
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


print("----------- Example-7: add and assign ---------------") 
balance = 1000
balance += 500 # 1500
if balance >= 1500:
    print("Updated Balance ", balance)


print("----------- Example-8: 'in' / 'not in' Operators ---------------") 
role = "admin"
if role in ['admin', 'manager']:
    print("Access granted")
else:
    print("Access denied")


print("----------- Example-9: 'is' / 'is not' Operators ---------------") 
a = None
if a is None:
    print("No Value")


print("----------- Example-10: All Operators Combined ---------------")     
age = 25
balance = 5000
role = "admin"
is_active = True
if (age >= 18 and balance > 1000) and role in ['admin', 'manager'] and is_active:
    print("Access granted")
else:
    print("Access denied")







    










