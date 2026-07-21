##############################################################################
#       filter_object = filter(function, iterable)
#              function → condition-checking function
#              iterable → list, tuple, set, etc. 
#       👉 filter() only filters, it does not change values.
#
#
##############################################################################

print("\n ----------- Example 1 : Check greater than 2 -----------------------\n")

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def greater_than_two(n):
    #return n + 2
    return n > 2

result_obj = filter(greater_than_two, numbers_list)
print( type(result_obj) )
print( list(result_obj) )



print("\n ----------------- Example 2 : Check Even Numbers --------------------- \n")

def is_even(n):
    return n % 2 == 0


filter_obj = filter(is_even, numbers_list)

print("filtered even : ", list(filter_obj) )



print("\n ----------------- Example 3 : Filter names with length more than 4 --------------------- \n")

names_list = ["Ram", "Shyam", "Mohan", "Amit"]

def long_name(name):
    return len(name) > 4

result_list = list( filter(long_name, names_list) )

print("result_list : ", result_list)



print("\n ----------------- Example 4 : Filter active users --------------------- \n")

users_list = [
    {"name": "Mahendra", "active": True},
    {"name": "Ravi",     "active": False},
    {"name": "Neha",     "active" : True}
]

def is_active(user):
    return user["active"] == True

active_users = list( filter(is_active, users_list) )
print(active_users)



print("\n ----------------- Example 5 : filter() with TUPLE --------------------- \n")

numbers_tuple = (10, 15, 20, 25, 30)

def is_even(n):
    return n % 2 == 0

even_numbers_obj = filter(is_even, numbers_list)

print("even_numbers : ", list(even_numbers_obj) )


print("\n ----------------- Example 6 : filter() with SET --------------------- \n")


numbers_set = {10, 15, 20, 25, 30}

def is_even(n):
    return n % 2 == 0

even_numbers_obj = filter(is_even, numbers_set)
print('even_numbers_set : ', set(even_numbers_obj) )    # convert object to set



print("\n ----------------- Example 7 : filter() with DICTIONARY (By default,works on keys only) --------------------- \n")
numbers_dict = {
    "a": 10,
    "b": 15,
    "c": 20
}


def check_key(item):
    key, value = item
    return key != "b"

result_dict = dict( filter(check_key, numbers_dict.items() ) )

print(result_dict)



print("\n ----------------- Example 8 : filter() with DICTIONARY (By default,works on keys only) --------------------- \n")


data = {
    "a": 10,
    "b": 15,
    "c": 20
}


def check_value(item):
    key, value = item
    return value > 10

result = dict(filter(check_value, data.items()))

print(result)



