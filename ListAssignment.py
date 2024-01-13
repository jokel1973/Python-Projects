import sqlite3

conn = sqlite3.connect('fileList.db')# Creates the empty database

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_filename STRING)")# Adds the columns
    conn.commit()
conn.close()# closes the connection to the database


conn = sqlite3.connect('fileList.db')
list_tuple = ('information.docx', 'Hello.txt', 'myImage.png', \
'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto. jpg')# gives the list to be looped through
# loop through each object in the tuple to find the files that end in txt.
for x in list_tuple:
    if x.endswith('txt'):
        with conn:
            cur = conn. cursor()
# The value for each row will be one files out of the tuple therefore (x,)
# will denote a one element tuple for each name ending with txt.
            cur.execute("INSERT INTO tbl_files (col_filename) VALUES (?)", (x, ))# inserts the files ending with txt into the database
            print(x)#prints the filenames ending in txt to the console
conn. close()
