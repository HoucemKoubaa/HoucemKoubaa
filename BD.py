import sqlite3

try:
    conn = sqlite3.connect('tp_cicd.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE user(
        login TEXT PRIMARY KEY,
        pwd TEXT,
        nom TEXT,
        prenom TEXT
    )
    ''')

    conn.commit()

except Exception as e:
    print(e)  # or log the error message

finally:
    if 'conn' in locals() or 'conn' in globals():
        conn.close()