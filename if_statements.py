# is_hot = False
# is_cold = True
#
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")
# print("Enjoy your day")
#

# Price of house is 1 million

price = 100000000
good_credit = True


if good_credit:
    print("Put down 10%")
    down_payment = price * 0.1
else:
    print("Put down 20%")
    down_payment = price * 0.2
print(f"Down payment: ${round(down_payment)}")