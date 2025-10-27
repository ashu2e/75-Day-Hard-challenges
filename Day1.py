# Mini Shopping Cart Project
# Created by Ashutosh Singh

# Step 1: Store items and prices
store = {
    "apple": 50,
    "banana": 20,
    "milk": 30,
    "bread": 25,
    "egg": 10,
    "chocolate": 40
}

# Step 2: Empty cart
cart = []

# Step 3: Display available items
def show_menu():
    print("\n----- WELCOME TO MINI SHOP -----")
    print("Available Items:")
    for item, price in store.items():
        print(f"{item.capitalize()} - ₹{price}")
    print("--------------------------------")

# Step 4: Display cart items
def show_cart():
    if not cart:
        print("\nYour cart is empty.")
    else:
        print("\n🛒 Items in your cart:")
        total = 0
        for item in cart:
            print(f"- {item.capitalize()} - ₹{store[item]}")
            total += store[item]
        print(f"Total Amount: ₹{total}")

# Step 5: Main program loop
while True:
    show_menu()
    print("\nChoose an option:")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Checkout and Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        item = input("Enter item name to add: ").lower()
        if item in store:
            cart.append(item)
            print(f"{item.capitalize()} added to cart!")
        else:
            print("❌ Item not available!")

    elif choice == "2":
        item = input("Enter item name to remove: ").lower()
        if item in cart:
            cart.remove(item)
            print(f"{item.capitalize()} removed from cart.")
        else:
            print("❌ Item not in your cart!")

    elif choice == "3":
        show_cart()

    elif choice == "4":
        show_cart()
        print("\nThank you for shopping with us! 😊")
        break

    else:
        print("Invalid choice! Please select again.")
