user_input= str(input("Type 1 if you are Male or 2 if you are Female "))

print(" Your response was : ", user_input)

user_input = int(user_input)

if user_input == 1:
    print("you are male")
elif user_input == 2:
    print("You are Female")
else:
    print("Please remember code is case sensitive \n please type only male or female")


