# temperature = 35
#
# if temperature > 30:
#     print("It's a hot day")
# else:
#     print("It's not a hot day")

min = 3
max = 50

user_name = input("Name: ")

if(len(user_name) < 3):
    print("Name must be at least 3 characters")
elif(len(user_name) > 50):
    print("Name cannot be more than 50 characters")
else:
    print("name looks goo