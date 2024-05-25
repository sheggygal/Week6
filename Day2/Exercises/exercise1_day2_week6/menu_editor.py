# menu_editor.py

import psycopg2
from menu_item import MenuItem
from menu_manager import MenuManager

def show_user_menu():
    while True:
        print("\nProgram Menu:")
        print("(V) View an Item")
        print("(A) Add an Item")
        print("(D) Delete an Item")
        print("(U) Update an Item")
        print("(S) Show the Menu")
        print("(E) Exit")

        choice = input("Please choose an option: ").strip().upper()

        if choice == 'V':
            view_item()
        elif choice == 'A':
            add_item_to_menu()
        elif choice == 'D':
            remove_item_from_menu()
        elif choice == 'U':
            update_item_from_menu()
        elif choice == 'S':
            show_restaurant_menu()
        elif choice == 'E':
            show_restaurant_menu()
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

def view_item():
    item_name = input("Enter the name of the item to view: ").strip().upper()
    connection = connect_db()
    item = MenuManager.get_by_name(connection, item_name)
    if item:
        print(f"Item found: {item}")
    else:
        print(f"No item found with the name '{item_name}'.")
    connection.close()

def add_item_to_menu():
    item_name = input("Enter the name of the item to add: ").strip().upper()
    item_price = int(input("Enter the price of the item: ").strip().upper())
    item = MenuItem(name=item_name, price=item_price)
    connection = connect_db()
    item.save(connection)
    print("Item was added successfully.")
    connection.close()

def remove_item_from_menu():
    item_name = input("Enter the name of the item to remove: ").strip().upper()
    connection = connect_db()
    item = MenuManager.get_by_name(connection, item_name)
    if item:
        item.delete(connection)
        print("Item was deleted successfully.")
    else:
        print(f"No item found with the name '{item_name}'.")
    connection.close()

def update_item_from_menu():
    old_name = input("Enter the name of the item to update: ").strip().upper()
    new_name = input("Enter the new name of the item: ").strip().upper()
    new_price = int(input("Enter the new price of the item: ").strip())
    connection = connect_db()
    item = MenuManager.get_by_name(connection, old_name)
    if item:
        item.update(connection, new_name=new_name, new_price=new_price)
        print("Item was updated successfully.")
    else:
        print(f"No item found with the name '{old_name}'.")
    connection.close()

def show_restaurant_menu():
    connection = connect_db()
    items = MenuManager.all_items(connection)
    print("Restaurant Menu:")
    for item in items:
        print(item)
    connection.close()

def connect_db():
    return psycopg2.connect(
        dbname="cafe",
        user="postgres",
        password="Ekeva12",
        host="localhost",
        port="5432"
    )

if __name__ == "__main__":
    show_user_menu()
