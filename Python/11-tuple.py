#######################################################################
#
#        What is a Tuple in Python ?
#
#        tuple is a collection (like a list) but
#        👉 but Tuple is immutable (cannot be changed after creation)
#        👉 Ordered (index-based)
#        👉 Immutable (no add/remove/update)
#        👉 Allows duplicate values
#        👉 Faster than list (because fixed)
#
#        Python Tuple vs PHP Array
#         -----------------------------------------------------
#        | Feature      | Python Tuple    | PHP Array          |
#        | ------------ | --------------- | ------------------ |
#        | Mutability   | ❌ Immutable     | ✅ Mutable        |
#        | Syntax       | `( )`           | `[ ]` or `array()` |
#        | Type         | Fixed structure | Flexible           |
#        | Performance  | Faster          | Slower             |
#        | Modification | Not allowed     | Allowed            |
#         -----------------------------------------------------
#
#       👉 Difference between List & Tuple:
#              --------------------  
#            | List    | Tuple     |
#            | ------- | --------- |
#            | Mutable | Immutable |
#            | `[]`    | `()`      |
#            | Slower  | Faster    |
#             ---------------------
#    can we remove element from tuple ?
#        No, because they are immutable (unchangeable).
#        To to do this Convert to a List, remove() item, convert to tuple(temp_list)
#
#
########################################################################

print("\n ----------  Example-1 : Tuple is Immutable ---------------- \n")
fruits_tuple = ("apple", "banana", "mango")
# fruits[1] = "Orange"     # Error: 'tuple' object does not support item assignment
print(fruits_tuple)



print("\n ----------  Example-2 : Accessing Tuple Elements ---------------- \n")
fruits_tuple = ("apple", "banana", "mango")

print(fruits_tuple[0])  # apple
print(fruits_tuple[1])  # banana


print("\n ----------  Example-3 : Loop Through Tuple ---------------- \n")
fruits_tuple = ("apple", "banana", "mango")
for fruit in fruits_tuple:
    print(fruit)


print("\n ----------  Example-4 : index (key) + value ---------------- \n")
fruits_tuple = ("apple", "banana", "mango")
for index, fruit in enumerate(fruits_tuple):
    print(index, fruit)


print("\n ----------  Example-5 : Custom Start Index ---------------- \n")
fruits_tuple = ("apple", "banana", "mango")
for index, fruit in enumerate(fruits_tuple, start = 1):
    print(index, fruit)










