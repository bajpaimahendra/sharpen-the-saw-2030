####################################################
#
#    What is map() in Python ?
#
#    Python syntax
#        object = map(function, iterable)
#
#        👉  Accept a function name
#        👉  returns a map object
#        👉  applies every item of iterable (list)
#        👉   map() → applies function
#
#   https://chatgpt.com/g/g-p-69c6734c95d081918b05c8e85d2449c5-python/c/69ccd253-dcd8-83a5-9013-4d6617482688
#
####################################################

print("\n -------- Example-1: Basic Understanding ---------\n")
numbers_list = [1,2,3,4,5]
def square(num):
    return num * num

result_obj = map(square, numbers_list)
print( type(result_obj) )
print(result_obj)

for value in result_obj:    # loop over object
    print(value)

    

print("\n -------- Example-2: Basic Understanding ---------\n")
result_list = list(result_obj) # convert object to list
print( type(result_list) )
print(result_list)


print("\n -------- Example-3: Tuple Example (without lambda) ---------\n")

def square(num):
    return num * num

numbers_tuple = (1,2,3,4,5)

result_obj_1  = map(square, numbers_tuple)
result_obj_2 = result_obj_1
print('converted tuple : ',  tuple(result_obj_1) )    # convert object to tuple again
print('converted list : ',  list(result_obj_2) )      # [] empty output, because map() returns an iterator (one-time use)


print("\n -------- Example-4: Set Example (without lambda) ---------\n")

def square(num):
    return num * num

numbers_set = {1,2,3,4,5}

result_obj_1 = map(square, numbers_set)

print( set(result_obj_1) ) # convert object to set again





print("\n -------- Example-5: Dictionary Example (values only) ---------\n")

def square(num):
    return num * num

numbers_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5
}

result_obj = map( square, numbers_dict.values() ) # values() gives only values

print('converted list', list(result_obj) )            # convert object to list again
# print('converted Dictionary', dict(result_obj) )    # Error , because values() gives only values






print("\n -------- Example-5: Dictionary Example (values only) ---------\n")
def update_item(item):
    key = item[0]
    value = item[1]
    return (key, value * value)

numbers_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5
}

result_obj = map( update_item, numbers_dict.items() ) # items() gives (key, value)sss

#print('converted list', list(result_obj) )            # convert object to list again
#print('converted Dictionary', dict(result_obj) )      # items() gives (key, value)
