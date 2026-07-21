##################################################
#
#       Runs until condition becomes False
#
#
###################################################

print("-------- Example 1: Basic while -----------------")

i = 1
while i <= 5:
    print(i)
    i += 1


print("-------- Example 2: Password attempt  -----------------")    
password = ""
while password != "admin":
    password = input("Enter Password :  ")
print("Login Successful")


print("-------- Real-Life Example: ATM System -----------------") 

balance = 11000

while True:
    withdraw = int(input("Enter Amount to withdraw: "))
    print("withdraw", withdraw)

    if withdraw <= balance:
        balance -= withdraw
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance")

    choice = input("Do you want to continue? (yes/no): ")
    if choice == "no":
        break

