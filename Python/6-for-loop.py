###############################################
#
#       Loop = repeat work automatically
#
#        for variable in sequence:
#            # code
#
#
#################################################

print("------ Example 1: Print numbers 1–5 ------------")
for i in range(1,6):
    print(i)


print("------- Example 2: Even numbers -----------")
for i in range(1,11):
    if i % 2 == 0:
        print(i)


print("------ Example 3: Loop through list ----------------")         
usersList = ['Ram', 'Shyam', 'Amit']
for user in usersList:
    print("Hello ", user)


print("------ Example 4. 'break' (Stop loop) ----------------")   
for i in range(1, 9):
    if i == 5:
        break;
    print(i)



print("------ Example 5. 'continue' (Skip) ----------------")     
for i in range(1, 9):
    if i == 3:
        continue
    print(i)


print("------ Example 6. 'pass' (Do nothing) ----------------")  
for i in range(5):
    #print("Hello")
    pass
    #print("Hi")





