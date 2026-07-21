###################################################################################
#    What is a List in Python?
#    👉 A list is a collection (array-like structure)
#
#    Python List vs PHP Array
#
#        ------------------------------------------------------------------
#        | Feature     | Python List            | PHP Array                 |
#        | ----------- | ---------------------- | ------------------------- |
#        | Syntax      | `[1, 2, 3]`            | `[1, 2, 3]`               |
#        | Type        | List                   | Array (mixed type)        |
#        | Index start | 0                      | 0                         |
#        | Key-value   | ❌ Not default         | ✅ Yes (associative array)|
#        | Mixed data  | ✅ Yes                 | ✅ Yes                    |
#        | Functions   | `.append(), .remove()` | `array_push(), unset()`   |
#        -------------------------------------------------------------------
#
#        👉 List in Python and PHP Array are same :
#
#            Ordered ✅
#            Changeable (mutable) ✅
#            Allows duplicate values ✅

#           List → ordered, indexed (0,1,2)
#           Dictionary → key-value (like PHP associative array)
#
#
###################################################################################

### python 

print("---- Example-1 : Basic Example -----------")
fruits_list = ["apple", "banana", "mango"]
print(fruits_list[0])  # apple


### PHP 
# $fruits = ["apple", "banana", "mango"];
# echo $fruits[0]; // apple



print("---- Example-2 : Add item -----------")
fruits_list = ["apple", "banana"]
fruits_list.append("manago")
print(fruits_list)


print("---- Example-3 : Remove item -----------")
fruits_list = ["apple", "banana", "mango"]
fruits_list.remove("banana")
print(fruits_list)


print("---- Example-4 : Update value -----------")
fruits_list = ["apple", "banana", "mango"]
fruits_list[1] = "orange"
print(fruits_list)



print("---- Example-5 : Loop through list -----------")
fruits_list = ["apple", "banana", "mango"]
for fruit in fruits_list:
    print(fruit)




print("---- Example-6 : get index (key) + value Using enumerate() (BEST way) -----------")   
fruits_list = ["apple", "banana", "mango"]
for index, fruit in enumerate(fruits_list):
    print(index, fruit)



print("---- Example-7 : get index (key) + value Using range (less preferred) -----------")   
fruits_list = ["apple", "banana", "mango"]
for i in range( len(fruits_list) ):
    print(i, fruits_list[i])



print("\n---- Example-8 : Even numbers from list -----------\n")   
numbers_list = [1,2,3,4,5,6,7,8,9]
even_numbers = []
odd_numbers = []
for number in numbers_list:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Even numbers List : ", even_numbers)
print("Odd numbers List  : ", odd_numbers)




print("---- Example-9 : ATM Transactions (List + Loop) -----------")   
transactions = []
while True:
    amount = int( input("Enter transactions amount : ") )
    transactions.append(amount)
    choice = input("Add more ? (yes/no) : ")
    if choice == "no":
        break
print("All Transactions", transactions)
total = sum(transactions)
print("Total amount : ", total)












