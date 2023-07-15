import sqlite3

# create a connection to the database
conn = sqlite3.connect('userlogin.db')

# create a cursor object to execute SQL statements
c = conn.cursor()

#enable this to erase the data that is already present in the database
c.execute("DELETE FROM users")

# create a table
# c.execute('''CREATE TABLE users
#              (username text, password text)''')

# Define the SQL query to add a new column to the table
# add_column = "ALTER TABLE users ADD COLUMN email VARCHAR(50)"

# Execute the query
# c.execute(add_column)

# username = input("Enter your username: ")


# c.execute("INSERT INTO users (username) VALUES (?)", (username,))


# password = input("Enter your password: ")


# c.execute("UPDATE users SET password=? WHERE username=?", (password, username))

# save (commit) the changes
# conn.commit()

# retrieve the data from the table
for row in c.execute("SELECT * FROM users"):
    print(row)

# print("fetching....")



# Execute the query
# c.execute("SELECT username FROM users ")

# # Fetch the result
# result = c.fetchall()

# # Extract the last entered user name
# if result:
#     print(result[len(result)-1])
# else:
#     last_user_name = None

# print("checking now....")

# username = 'v@x.y'
# c.execute("SELECT * FROM users WHERE username=?", (username,))
# row = c.fetchone()

# check if the row exists (i.e., the username is in the database)
# if row is not None:
#     print("The username is in the database!")
#     print(row)
# else:
#     print("The username is not in the database.")
# close the connection
conn.close()