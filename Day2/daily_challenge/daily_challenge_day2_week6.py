import psycopg2
import requests
import random


# Function to connect to the database
def connect_db():
    return psycopg2.connect(
        dbname="countries",
        user="postgres",
        password="Ekeva12",
        host="localhost",
        port="5432"
    )


# Function to create the table if it doesn't exist
def create_table(connection):
    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Countries (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                capital VARCHAR(100),
                flag TEXT,
                subregion VARCHAR(100),
                population BIGINT
            );
        """)
    connection.commit()


# Function to fetch data from the REST Countries API
def fetch_countries():
    response = requests.get("https://restcountries.com/v3.1/all?fields=name,capital,flags,subregion,population")
    response.raise_for_status()
    return response.json()


# Function to select 10 random countries
def select_random_countries(countries, num=10):
    return random.sample(countries, num)


# Function to insert countries into the database
def insert_countries(connection, countries):
    with connection.cursor() as cursor:
        for country in countries:
            name = country.get("name", {}).get("common", "")
            capital = country.get("capital", [""])[0] if country.get("capital") else None
            flag = country.get("flags", {}).get("png", "")
            subregion = country.get("subregion", "")
            population = country.get("population", 0)

            cursor.execute("""
                INSERT INTO Countries (name, capital, flag, subregion, population)
                VALUES (%s, %s, %s, %s, %s)
            """, (name, capital, flag, subregion, population))
    connection.commit()


# Main function to orchestrate the tasks
def main():
    connection = connect_db()
    create_table(connection)

    countries = fetch_countries()
    random_countries = select_random_countries(countries)

    # Print the selected countries
    print("Selected countries:")
    for country in random_countries:
        print(
            f"Name: {country.get('name', {}).get('common', '')}, Capital: {country.get('capital', [''])[0] if country.get('capital') else 'N/A'}, Flag: {country.get('flags', {}).get('png', '')}, Subregion: {country.get('subregion', '')}, Population: {country.get('population', 0)}")

    insert_countries(connection, random_countries)

    connection.close()
    print("10 random countries have been inserted into the database.")


if __name__ == "__main__":
    main()
