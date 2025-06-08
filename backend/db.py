import sqlite3

def init_db():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location TEXT NOT NULL,
            temperature REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_weather(location, temp):
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute("INSERT INTO weather (location, temperature) VALUES (?, ?)", (location, temp))
    conn.commit()
    conn.close()

def get_all_weather():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute("SELECT * FROM weather")
    rows = c.fetchall()
    conn.close()
    return [{"id": row[0], "location": row[1], "temperature": row[2]} for row in rows]

def update_weather(weather_id, new_temp):
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute("UPDATE weather SET temperature = ? WHERE id = ?", (new_temp, weather_id))
    conn.commit()
    updated = c.rowcount
    conn.close()
    return updated > 0

def delete_weather(weather_id):
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute("DELETE FROM weather WHERE id = ?", (weather_id,))
    conn.commit()
    deleted = c.rowcount
    conn.close()
    return deleted > 0
