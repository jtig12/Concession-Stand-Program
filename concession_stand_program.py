menu = {
    "popcorn": 10.00,
    "hotdog": 3.00,
    "sandwitch": 4.00,
    "meatpie": 6.00,
    "soda": 2.00,
    "water": 1.00
}

cart = []
total = 0

print("---------------------------------")
print("              MENU               ")
print("---------------------------------")

for item, price in menu.items():
    print(f"{item:15} - ${price:.2f}")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)


for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print(f"\nThe total is {total: .2f}")
