# get user weight
user_weight = input("Weight: ")

lb_kg = input("(L)bs or (K)g: ")

if lb_kg.upper() == "L":
    kg = int(user_weight) * .45
    print(f"You are {kg} kilos")
else:
    lb = int(user_weight) / .45
    print(f"You are