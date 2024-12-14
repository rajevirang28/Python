menu = {}

def add_item():
    name = input("Enter item name: ")
    price = input("Enter item price: ")
    menu[name] = price
    print("Item added.")

def display_item():
    if menu:
        print("Current Menu: ")
        for name, price in menu.items():
            print("Name: ",name,"Price: ",price)
    else:
        print("Menu is empty.")

def search_menu():
    name = input("Enter the item name to search: ")
    if name in menu:
        print("Found: Name: ",name,"Price: ", menu[name])
    else:
        print("Item not found")

def delete_item():
    name = input("Enter item name to delete: ")
    if name in menu:
        del menu[name]
        print("item deleted")
    else:
        print("item not found")

def update_item():
    name = input("Enter the item name to update: ")
    if name in menu:
        new_price = input("Enter the new price: ")
        menu[name] = new_price
        print("Item update")
    else:
        print("Item not found")

while True:
    print("1. Add Item")
    print("2. Display menu")
    print("3. search item")
    print("4. deleted item")
    print("5. update item")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_item()
    elif choice == "2":
        display_item()
    elif choice == "3":
        search_menu()
    elif choice == "4":
        delete_item()
    elif choice == "5":
        update_item()
    elif choice == "6":
        print("Thank You")
        break