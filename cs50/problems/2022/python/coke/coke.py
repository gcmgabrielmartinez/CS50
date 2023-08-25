amount = 50

while amount > 0 :
    print(f"Amount Due: {amount}")
    insert = int(input("Insert Coin: ").strip())
    if insert in [25, 10, 5]:
        amount -= insert

print(f"Change Owed: {-amount}")
