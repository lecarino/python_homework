# ---- TASK 1: CREATE NEW DATABASE ----
#Write code to connect to a new SQLite database, ../db/magazines.db and to close the connection.
import sqlite3

#FUNCTIONS: 
# def add_student(cursor, name, age, major):
#     try:
#         cursor.execute("INSERT INTO Students (name, age, major) VALUES (?,?,?)", (name, age, major))
#     except sqlite3.IntegrityError:
#         print(f"{name} is already in the database.")

def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
        print(f"Added publisher: {name}")
    except:
        print(f"{name} is already a publisher in the database")

def add_magazine(cursor, name, publisher_id):
    try:
        cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?,?)", (name, publisher_id))
        print(f"Added magazine: {name}")
    except:
        print(f"{name} is already a magazine in the database")

def add_subscriber(cursor, name, address):
    #AS LONG AS NAME AND ADDRESS ARE NOT IN DB ALREADY
    cursor.execute("SELECT id FROM subscribers WHERE name = ? AND address = ?", (name, address))
    existing_record = cursor.fetchone()

    if existing_record:
        print(f"{name} from adress {address} is already a subscriber") 
    else:
        cursor.execute("INSERT INTO subscribers (name, address) VALUES (?,?)", (name, address))
        print(f"Added subscriber: {name}")
        
def add_subscription(cursor, subscriber_id, magazine_id, expiration_date):
    #subscriber not subscribed to the same magazine twice
    cursor.execute("SELECT id from subscriptions WHERE subscriber_id = ? AND magazine_id = ?", (subscriber_id,magazine_id))
    existing_subscription = cursor.fetchone()

    if existing_subscription:
        print(f"Subscription already exists")
    else:
        cursor.execute("INSERT INTO subscriptions(subscriber_id, magazine_id, expiration_date) VALUES (?,?,?)", (subscriber_id,magazine_id,expiration_date))
        print(f"Subscription added successfully! Subscriber {subscriber_id} subscribed to magazine {magazine_id}")

try:
    # Connect to the database
    with sqlite3.connect("../db/magazines.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

        print("Database successfully connected!")
        #---- TASK 2: DEFINE DATABASE STRUCTURE ----
        '''
        1. Think for a minute.  There is a one-to-many relationship between publishers and magazines.  
        Which table has a foreign key? 
        Where does the foreign key point?  
        How about the subscriptions table: What foreign keys does it have?
            - The "many" side will get a foreign key to access the unique ID of the publisher "one" side. 
            - subscriptions table has two foreign keys to point to subscribers and magazines.
        '''
        #publishers: unique name
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS publishers (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE
            )
            """)
        #magazines: unique name, foreign key
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS magazines (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE,
                publisher_id INTEGER,
                FOREIGN KEY (publisher_id) REFERENCES publishers(id)
            )
            """)
        #subscribers: name and address
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscribers (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                address TEXT NOT NULL
            )           
            """)
        #subscriptions: 2 foreign keys to connect subscribers and magazines (many to many), expiration date (str)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscriptions (
                id INTEGER PRIMARY KEY,
                subscriber_id INTEGER,
                magazine_id INTEGER,
                expiration_date TEXT NOT NULL,
                FOREIGN KEY (subscriber_id) REFERENCES subscribers(id),
                FOREIGN KEY (magazine_id) REFERENCES magazines(id)           
            )
            """)
        print("Tables created successfully.")

        # ---- TASK 3 POPULATE DATA ----
        '''
        Create functions, one for each of the tables, to add entries. 
        Include code to handle exceptions as needed, and to ensure that there is no duplication of information.
        The subscribers name and address columns don't have unique values -- you might have several subscribers with the same name. 
        But when creating a subscriber, check that you don't already have an entry where both the name and the address are the same as for the one you are trying to create.
        '''

        #Insert data for task 3
        print("Publishers...")
        add_publisher(cursor, "Publisher 1")
        add_publisher(cursor, "Publisher 2")
        add_publisher(cursor, "Publisher 3")

        print("\nMagazines...")
        add_magazine(cursor, "Vogue", 1)
        add_magazine(cursor, "Esquire", 2)
        add_magazine(cursor, "People", 3)

        print("\nSubscribers...")
        add_subscriber(cursor, "Larryboy", "123 Python Lane, Los Angeles, CA")
        add_subscriber(cursor, "Bruce Wayne", "1007 Mountain Drive, Gotham")
        add_subscriber(cursor, "Clark Kent", "344 Clinton St, Metropolis")

        print("\nSubscriptions")
        add_subscription(cursor, 1, 2, "2026-12-31") 
        add_subscription(cursor, 2, 1, "2027-01-15") 
        add_subscription(cursor, 3, 3, "2025-10-01") 

        conn.commit()
        # ---- TASK 4: WRITE SQL QUERIES ----

        #1. Write a query to retrieve all information from the subscribers table.
        print("\n ALL SUBSCRIBERS: ")
        cursor.execute("SELECT * FROM subscribers")
        result1 = cursor.fetchall()
        for row in result1:
            print(row)

        #2. Write a query to retrieve all magazines sorted by name.
        print("\n SORTED MAGAZINE NAMES: ")
        cursor.execute("SELECT * FROM magazines ORDER BY name")
        result2 = cursor.fetchall()
        for row in result2:
            print(row)

        #3. Write a query to find magazines for a particular publisher, one of the publishers you created. This requires a JOIN.
        print("\n MAGAZINES FROM PUBLISHER 1")
        cursor.execute("SELECT magazines.name, publishers.name FROM magazines JOIN publishers on magazines.publisher_id = publishers.id WHERE publishers.name = 'Publisher 1' ")
        result3 = cursor.fetchall()
        for row in result3:
            print(row)

except sqlite3.Error as e:
    print(f"database error: {e}")
except Exception as e:
    print(f"exception error: {e}")
finally:
    if conn:
        conn.close()
        print("Database connection successfully closed.")


