import sqlite3

# create a connection to the database
conn = sqlite3.connect('web.db')

# create a cursor object to execute SQL statements
c = conn.cursor()

#enable this to erase the data that is already present in the database
c.execute("DELETE FROM words")

# create a table
# c.execute('''CREATE TABLE words
#              (data text)''')

# insert some data into the table
# word = input("enter the word")
# c.execute("INSERT INTO words VALUES (?)", (word,))
# c.execute("DELETE FROM words WHERE data like '%vijay'")
# c.execute("UPDATE words SET data = 'updated' WHERE data like '%anitha' ")
# save (commit) the changes



conn.commit()

# retrieve the data from the table
for row in c.execute("SELECT * FROM words"):
    print(row)

# close the connection
conn.close()