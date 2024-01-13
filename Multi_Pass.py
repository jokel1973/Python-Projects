import sqlite3

rosterValues = [
    ('Jean-Baptiste Zorg', 'Human', 122),
    ('Korben Dallas', 'Meat Popsicle', 100),
    ('Aknot', 'Mangalore', -5)
]

with sqlite3.connect('DB_PythonChallenge.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS Roster")
    c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")
    c.executemany("INSERT INTO Roster VALUES(?, ?, ?)", rosterValues)

   
    c.execute("UPDATE Roster SET Species=? WHERE Name=? AND IQ=?",
              ('Human', 'Korben Dallas', 100))
    c.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'")
    
    # Fetch all the results
    rows = c.fetchall()

    # Display the results
    for row in rows:
        name, iq = row
        print(f"Name: {name}, IQ: {iq}")

# Additional code can be added here if needed
