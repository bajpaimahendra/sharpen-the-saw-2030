#####################################################################
#   What is a Data Structure ?
#        - data structure is a container that holds data.    
#        - ways to store, organize, and manage data efficiently so you can access and modify it easily.
#        - Python provides four primary built-in data structures for organizing and managing collections of data: 
#            1- Lists
#            2- Tuples
#            3- Sets
#            4- Dictionaries
#####################################################################

print("\n --------- 1. List (Like PHP Indexed Array) -------------------------\n")
fruits_list = ["apple", "banana", "mango"]
fruits_list[0] = "orange" # Update element
print("Entire List : ", fruits_list)

# Features
#   - Ordered(Indexed)
#   - Mutable (can change)
#   - Allows duplicates

empty_list = []
print(" \n Empty List : ", empty_list)
print("Variable Type : ", type(empty_list) )





print("\n --------- 2. Tuple (Immutable List) ----------------------------------\n")
# 👉 PHP: No direct equivalent (closest = array but mutable)
fruits_tuple = ("apple", "banana", "mango")
# fruits_tuple[0] = "orange" ❌ Error (immutable)
print("Entire Tuple : ", fruits_tuple)

#  Features
#    Ordered
#    ❌ Cannot change (immutable)
#    Faster than lists
# 👉 PHP: No direct equivalent (closest = array but mutable)

#    can we remove element from tuple ?
#        No, because they are immutable (unchangeable).
#        To to do this Convert to a List, remove() item, convert to tuple(temp_list)





print("\n --------- 3. Set (Unique Values Only) ----------------------------------\n")
emails_set = {"a@gmail.com", "b@gmail.com", "a@gmail.com"}
print("emails_set : ", emails_set)   # Output: {'a@gmail.com', 'b@gmail.com'}

# Features
#    Unordered i.e. No indexed
#    No duplicates
#    Fast lookup
# 👉 PHP: No direct built-in (use array + array_unique)






print("\n --------- 4. Dictionary (Like PHP Associative Array) ----------------------------------\n")
user_dict = {
    "name" : "Mahendra",
    "age"  : 30
}

print("User Dictionary : ", user_dict)

# Features
#    Key → Value pair
#    Fast lookup
#    Very important (used everywhere)



