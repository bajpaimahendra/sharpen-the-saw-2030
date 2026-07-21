##########################################################################################
#        Set vs Dictionary (Python) — Full Comparison
#
#            🧠 Key Concept
#                Set = Collection of unique items
#                No index → No direct access
#                Use loop or convert to list
#
#     --------------------------------------------------------------------------------------------------------------------------
#    | Feature        | **Set (Python)**                | **Dictionary (Python)**             | **PHP Equivalent**              |
#    | -------------- | ------------------------------- | ----------------------------------- | ------------------------------- |
#    | Definition     | Collection of **unique values** | Collection of **key → value pairs** | PHP array (associative)         |
#    | Syntax         | `{"a", "b"}`                    | `{"key": "value"}`                  | `["key" => "value"]`            |
#    | Structure      | Only values                     | Key + Value                         | Key + Value                     |
#    | Duplicates     | ❌ Not allowed                  | ❌ Keys not allowed (values allowed)| Same as dict                    |
#    | Order          | ❌ Unordered                    | ✅ Ordered (Python 3.7+)            | ✅ Ordered                      |
#    | Indexing       | ❌ Not possible                 | ❌ No index, but key access         | ❌ No index, key access         |
#    | Access method  | ❌ Cannot access directly       | ✅ `dict[key]`                      | `$arr["key"]`                   |
#    | Mutable        | ✅ Yes                          | ✅ Yes                              | ✅ Yes                          |
#    | Add item       | `set.add()`                     | `dict[key] = value`                 | `$arr[] = val` or `$arr["k"]=v` |
#    | Remove item    | `set.remove()`                  | `del dict[key]`                     | `unset($arr["k"])`              |
#    | Empty creation | `set()`                         | `{}`                                | `[]`                            |
#    | Use case       | Unique data, fast lookup        | Structured data                     | Mostly dictionary               |
#    | Performance    | Faster for membership (`in`)    | Slightly slower than set            | Depends                         |
#     --------------------------------------------------------------------------------------------------------------------------
#
#    👉 Set = Unique + Fast + No order
#    👉 Unordered (no index)
#    👉 Mutable (you can add/remove items)
#    Why Set looks like Dictionary ?
#            👉 both use curly braces {}
#            👉 Set (only values)        fruits = {"apple", "banana", "mango"}
#            👉 Dictionary (key-value)   person = {"name": "Mahendra", "age": 30}
#            👉 Set (no access like this)   fruits = {"apple", "banana"} # print(fruits["apple"]) ❌ ERROR
#            👉 If you see : → it's a Dictionary
#            👉 If no : → it's a Set
#            👉 create empty Set, my_empty_set = set()  
#            👉 create empty Dictionary, my_empty_dictionary = {}
#
################################################################################################

print("\n ------- Important Confusion Case ------------- \n")
emails = {}     # empty Dictionary

print( type(emails) )

emails = set()     # empty Set

print( type(emails) )

fruits_set = {"apple", "banana", "apple"}
print("fruits_set : ", fruits_set)


person_dict = {"name": "Mahendra", "age": 30}
print("person_dict : ", person_dict)


emails = {"abc@gmail.com", "cde@gmail.com", "abc@gmail.com"}
print(emails) # {'cde@gmail.com', 'abc@gmail.com'} 'set' removes duplicates only if values are exactly same



# print("\n -------Example-1 : Access Elements from a Set ------------- \n")
# fruits_set = {"apple", "banana", "apple", "mango"}
# print(fruits_set[0])   # ❌ Error 'set' is unordered, so you cannot access elements by index



print("\n -------Example-2 : Access Elements, Using Loop (Most Common) ------------- \n")
fruits_set = {"apple", "banana", "mango"}
for fruit in fruits_set :
    print(fruit)


print("\n -------Example-2 : Access Elements, Using in (Check if element exists) ------------- \n")   
fruits_set = {"apple", "banana", "mango"}
if "apple" in fruits_set:
    print("apple exists") 


print("\n -------Example-3 : Access Elements, Convert to List (If you need index) ------------- \n")   
fruits_set = {"apple", "banana", "mango"}
fruits_list = list(fruits_set)
print("fruits_list : ",fruits_list)
print(fruits_list[1])   # ⚠️ Note: Order is still not guaranteed!



print("\n -------Example-4 : Access Elements, Using pop() (Removes & returns random item) ------------- \n")   
fruits_set = {"apple", "banana", "mango"}
item = fruits_set.pop()
print(item)
print(fruits_set)

print("\n -------Example-5 : Set Operations (Very Important) ------------- \n") 
fruits_set = {"apple", "banana"}

### Add item
fruits_set.add("mango")
print("fruits_set After Add item : ", fruits_set)

### Remove item
fruits_set.remove("banana")
print("fruits_set After Remove item", fruits_set)



print("\n -------Example-6 : Set Operations (Very Important) ------------- \n") 
a = {1, 2, 3}
b = {3, 4, 5}

union_set = a|b
print(union_set)  # Union → {1,2,3,4,5} , PHP : array_merge()

intersection_set = a & b
print(intersection_set)     # Intersection → {3}, PHP : array_intersect()

difference_set = a-b
print(difference_set)   # Difference → {1,2}, PHP : array_diff(), present in set 'a' but not in set 'b'




print("\n -------Example-7 : Real-Life Example , Remove duplicate emails from list ------------- \n") 
emails_list = ['abc@gmail.com', "cde@gmail.com", "abc@gmail.com"]
print('emails_list : ', emails_list)

unique_emails_set = set(emails_list)
print("unique_emails_set : ", unique_emails_set)




