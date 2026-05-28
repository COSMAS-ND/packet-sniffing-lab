import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

username = input("Enter username: ")
cursor.execute("SELECT * FROM users WHERE username = ?" , (username, ))
print("Query executed safely")
