while True:
    name = input("Enter customer name: ")
    total = 0

    while True:
        print("Enter the amount and the quantity")
        amount = float(input("Enter amount: "))
        quantity = int(input("Enter quantity: "))

        total += amount * quantity

        repeat = input("Do you want to add more items? (yes/no): ").lower()
        if repeat == "no":
            break

    print("_" * 40)
    print("Name:", name)
    print("Amount to be paid:", total)
    print("_" * 40)
    print("********** HAPPY SHOPPING **********")

    repeat1 = input("Do you want to go to next customer? (yes/no): ").lower()
    if repeat1 == "no":
        break
