####  1. Numeric Types  ###########################################

a = 10      # int,      → whole numbers
b = 10.5    # float     → decimal numbers
c = 2+3j    # complex   → real + imaginary

####  2. String  ###################################################

name =  "Mahendra" # String → Immutable (cannot change directly)

####  3. List ( same as array in php ) ############################## 

fruits = ["apple", "banana", "mango"] # Index-based, Mutable (can change)

####  4. Tuple  ######################################################

colors = ("red", "green", "blue") # Ordered but immutable i.e. Cannot modify after creation

####  5. Set  ########################################################

emails = {"a@gmail.com", "b@gmail.com", "a@gmail.com"}
print(emails)   # duplicates removed , No duplicates, No indexing (Unordered)


####  6. Dictionary ( Key-value pair, Same as PHP associative array  ###############################


student = {
    "name": "Mahendra",
    "age": 25
}

print(student)


#### 7. Boolean (bool) True / False ###################################################

is_active = True
print(is_active)

#### 8. None Type #####################################################################

# Represents no value
# Same as null in PHP

x = None
print(x)


##### Simple Practice (Do this) ######################################################
# create all data types

print("\n -------------------- Simple Practice (Do this) -------------------------\n")

a_int = 10
b_float = 10.5
name_str = "Mahendra"
fruits_list = []
colors_tuple = ()
emails_set = {}
student_dict = {}
is_active_bool = True
x = None


print( type(a_int) )
print( type(b_float) )
print( type(name_str) )
print( type(fruits_list) )
print( type(colors_tuple) )
print( type(emails_set) )
print( type(student_dict) )
print( type(is_active_bool) )
print( type(x) )











