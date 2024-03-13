budget = int(input("Enter your budget: "))
shakes = {
    1: {'flavor': 'Vanilla', 'price': 5},
    2: {'flavor': 'Chocolate', 'price': 6},
    3: {'flavor': 'Strawberry', 'price': 4}
}



while True:

    print("milkshake options:")
    print("1: Vanilla - £5")
    print("2: Chocolate - £6")
    print("3: Strawberry - £4")

    choice = input("Enter the number of your choice (or Q to quit): ")

    print("milkshake options:")
    for choice, shake in shakes.items():
        print(f"{choice}: {shake['flavor']} - ${shake['price']}")