import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

username = input("Enter username: ")
cursor.execute("SELECT ? ", (username,))
print("Query executed safely")
