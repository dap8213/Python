#Database import
import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name Text, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts (name, phone, email) VALUES ('Tim', 65831, 'timtimmy@hotmail.com')")
db.execute("INSERT INTO contacts VALUES ('Brian', 1234, 'brian@yahoo.com')")


#To retrieve information from the database
cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")
def print_DB():
    for name, phone, email in cursor:
        print(name)
        print(phone)
        print(email)
        print("-" * 20)

print_DB()
print_DB()
cursor.close()
db.close()