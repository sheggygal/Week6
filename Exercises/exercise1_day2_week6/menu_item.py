import psycopg2

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"MenuItem(name={self.name}, price={self.price})"

    def save(self, connection):
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s) RETURNING item_id;",
                (self.name, self.price)
            )
            self.item_id = cursor.fetchone()[0]
        connection.commit()

    def delete(self, connection):
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM Menu_Items WHERE item_name = %s;", (self.name,))
        connection.commit()

    def update(self, connection, new_name=None, new_price=None):
        updates = []
        params = []
        if new_name:
            updates.append("item_name = %s")
            params.append(new_name)
        if new_price:
            updates.append("item_price = %s")
            params.append(new_price)

        params.append(self.name)
        query = f"UPDATE Menu_Items SET {', '.join(updates)} WHERE item_name = %s;"

        with connection.cursor() as cursor:
            cursor.execute(query, params)
        connection.commit()

        # Update the object attributes if the update was successful
        if new_name:
            self.name = new_name
        if new_price:
            self.price = new_price

    def __repr__(self):
        return f"MenuItem(name={self.name}, price={self.price})"


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

    # Create a MenuItem object
    item = MenuItem(name="Latte", price=4)

    # Save the item to the database
    item.save(connection)
    print(f"Saved item with ID: {item.item_id}")

    # Update the item
    item.update(connection, new_price=5)
    print(f"Updated item: {item}")

    # Delete the item
    item.delete(connection)
    print(f"Deleted item: {item}")


    # Close the connection
    connection.close()
