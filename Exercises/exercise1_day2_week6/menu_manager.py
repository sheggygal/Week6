import psycopg2
from menu_item import MenuItem


class MenuManager:
    @classmethod
    def get_by_name(cls, connection, name):
        with connection.cursor() as cursor:
            cursor.execute("SELECT item_name, item_price FROM Menu_Items WHERE item_name = %s;", (name,))
            result = cursor.fetchone()

            if result:
                item_name, item_price = result
                return MenuItem(name=item_name, price=item_price)
            else:
                return None

    @classmethod
    def all_items(cls, connection):
        with connection.cursor() as cursor:
            cursor.execute("SELECT item_name, item_price FROM Menu_Items;")
            results = cursor.fetchall()

            items = [MenuItem(name=item_name, price=item_price) for item_name, item_price in results]
            return items


# Example usage
if __name__ == "__main__":
    # Connect to your PostgreSQL database
    connection = psycopg2.connect(
        dbname="cafe",
        user="postgres",
        password="Ekeva12",
        host="localhost",
        port="5432"
    )

    # Get item by name
    item_name = "Latte"
    item = MenuManager.get_by_name(connection, item_name)

    if item:
        print(f"Item found: {item}")
    else:
        print(f"Item with name '{item_name}' not found.")

        # Get all items
    items = MenuManager.all_items(connection)
    print("All items:")
    for item in items:
        print(item)

    # Close the connection
    connection.close()
