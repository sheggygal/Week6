import psycopg2


# Function to connect to the database
def connect_db():
    return psycopg2.connect(
        dbname="Users",
        user="postgres",
        password="Ekeva12",
        host="localhost",
        port="5432"
    )


# Function to create users table if it doesn't exist
def create_table(connection):
    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(100) NOT NULL
            );
        """)
    connection.commit()


# Function to add a new user to the database
def add_user(connection, username, password):
    with connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO users (username, password)
            VALUES (%s, %s)
        """, (username, password))
    connection.commit()


# Function to check if a user exists
def get_user(connection, username):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        return cursor.fetchone()


def login(connection):
    logged_in = None

    while True:
        action = input("Enter 'login' to log in, 'signup' to sign up or 'exit' to quit: ").strip().lower()

        if action == 'exit':
            break

        elif action == 'login':
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()

            user = get_user(connection, username)
            if user and user[2] == password:
                print("You are now logged in.")
                logged_in = username
                break
            else:
                print("Invalid username or password.")

        elif action == 'signup':
            while True:
                username = input("Enter a new username: ").strip()
                if get_user(connection, username):
                    print("Username already exists. Please try again.")
                else:
                    break

            password = input("Enter a new password: ").strip()
            add_user(connection, username, password)
            print("Signup successful. You can now login.")

    return logged_in


def main():
    connection = connect_db()
    create_table(connection)

    logged_in_user = login(connection)
    if logged_in_user:
        print(f"Logged in as: {logged_in_user}")

    connection.close()


if __name__ == "__main__":
    main()
