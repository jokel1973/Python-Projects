


import sqlite3


peopleValues = (('Roin', 'Obvious', 42), ('Luigi', 'Vericotti', 43), ('Arthur', 'Belling', 28))

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS People")
    c.execute("CREATE TABLE People(FirstName TEXT, LastName Text, Age INT)")
    c.executemany("INSERT INTO People VALUES(?, ?, ?)",
                  peopleValues)

# select all first and last names from people over the age 30
    c.execute("SELECT FirstName, LastName FROM people WHERE Age > 30")
    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)

