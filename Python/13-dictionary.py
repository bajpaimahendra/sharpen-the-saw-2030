#####################################################################
#       What is a Dictionary in Python ?
#           dictionary in Python is a collection of key-value pairs.
#        👉 Dictionary → key-value (like PHP associative array)
#
#        Python Dictionary vs PHP Array
#         -------------------------------------------------------   
#        | Feature   | Python Dictionary     | PHP Array         |
#        | --------- | --------------------- | ----------------- |
#        | Type      | dict                  | array             |
#        | Structure | key → value           | key → value       |
#        | Syntax    | `{}`                  | `[]` or `array()` |
#        | Key Type  | string, int, tuple    | string or int     |
#        | Order     | Ordered (Python 3.7+) | Ordered           |
#        | Access    | `dict["key"]`         | `$arr["key"]`     |
#         -------------------------------------------------------
#
#####################################################################

print("\n ----- Example-1 :  Comparison whith PHP -------- \n")

########## PHP #########

# $user = [
#     "name" => "Mahendra",
#     "age" => 25
# ];

# echo $user["name"];

########### Python #######

user = {
    "name": "Mahendra",
    "age": 25
}
print(user["name"])



print("\n --------- Exmple-2 : Accessing Values -------------- \n ")
user = {
    'name' : 'Mahendra',
    'age' : 25
}
print(user['name'])
print( user.get('age') ) # 👉 .get() is safer (no error if key missing)



print("\n --------- Exmple-3 : Adding Values -------------- \n ")
user = {
    "name" : "Mahendra"
}
user["age"] = 25  # Add value

print(user)


print("\n --------- Exmple-4 : Updating Values -------------- \n ")
user = {
    "name" : "Mahendra",
    "age"  : 25
}

user["name"] = "Bajpai"

print(user)





print("\n --------- Exmple-5 : Delete Values -------------- \n ")
user = {
    "name" : "Mahendra",
    "age"  : 25
}
del user["age"]
print(user)


print("\n --------- Exmple-6 : Loop Through Dictionary -------------- \n ")
user = {
    "name" : "Mahendra",
    "age"  : 25
}

for key, value in user.items():
    print(key, value)



print("\n --------- Exmple-7 : Loop Through Dictionary -------------- \n ")
marks = {
    "maths" : 80,
    "science" : 90,
    "english" : 85 
}
total = 0
for key_subject, value_scroe in marks.items():
    total += value_scroe

print( "Total : ", total )








