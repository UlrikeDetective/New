import sqlite3

# Connect to the database (or create if it doesn't exist)
conn = sqlite3.connect('cafes.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create a table to store cafe details
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cafes (
        id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT,
        wifi BOOLEAN,
        power BOOLEAN,
        latitude REAL,
        longitude REAL
    )
''')

# Commit changes and close connection
conn.commit()
conn.close()
def add_cafe(name, description, wifi, power, latitude, longitude):
    conn = sqlite3.connect('cafes.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO cafes (name, description, wifi, power, latitude, longitude)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, description, wifi, power, latitude, longitude))

    conn.commit()
    conn.close()

# Example: Add a cafe
add_cafe('Cafe A', 'A cozy cafe', True, True, 37.7749, -122.4194)
add_cafe('Cafe Blue', 'Everything Blue', True, True, 37.7749, -122.4194)
def get_cafes_with_wifi_power():
    conn = sqlite3.connect('cafes.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM cafes WHERE wifi = ? AND power = ?', (True, True))
    cafes = cursor.fetchall()

    conn.close()
    return cafes

# Example: Retrieve cafes with WiFi and power available
cafes_with_wifi_power = get_cafes_with_wifi_power()
print(cafes_with_wifi_power)
