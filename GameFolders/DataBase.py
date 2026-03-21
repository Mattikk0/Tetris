import sqlite3
from datetime import date

conn = sqlite3.connect("high_scores.db")
def connect_and_setup():
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scores (
        game_id INTEGER PRIMARY KEY AUTOINCREMENT,
        points INTEGER,
        game_date TEXT
    )
    """)
    conn.commit()

def add_game(points):
    cursor = conn.cursor()
    curr_date = str(date.today().strftime("%d-%m-%Y"))
    cursor.execute(f"""
    INSERT INTO scores (points, game_date) VALUES ({points}, '{str(curr_date)}') """)
    conn.commit()

def display_scores():
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM scores ORDER BY points DESC LIMIT 10
    """)
    conn.commit()
    return cursor.fetchall()