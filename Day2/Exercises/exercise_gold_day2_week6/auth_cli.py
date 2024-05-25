users = {
    'user1': 'password1',
    'user2': 'password2',
    'user3': 'password3'
}

def login(users):
    logged_in = None

    while True:
        action = input("Enter 'login' to log in, 'signup' to sign up or 'exit' to quit: ").strip().lower()

        if action == 'exit':
            break

        elif action == 'login':
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()

            if username in users and users[username] == password:
                print("You are now logged in")
                logged_in = username
                break

            else:
                print("Invalid username or password")

        elif action == 'signup':
            while True:
                username = input("Enter a new username: ").strip()
                if username in users:
                    print("Username already exists. Please try again.")
                else:
                    break

            password = input("Enter a new password: ").strip()
            users[username] = password
            print("Signup successful. You can now login.")

    return logged_in

logged_in_user = login(users)
if logged_in_user:
    print(f"Logged in as: {logged_in_user}")

