# Dictionaires are used to store key value pairs

# Define dictionairy

# customer = {
#     "name": "John Smith",
#     "age": 30,
#     "is_verified": True
# }
#
# print(customer.get("birthdate", "Jan 1 1980"))


phone_number = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

user_input = input("Phone: ")

for i in user_input:
    print(phone_number.get(f"{i}"), end=" ")
print()