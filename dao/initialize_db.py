import sqlite3
# Run this file ones to create the db schema needed.
# It creates the HISTORY table to store the user search history.
db = sqlite3.connect('discord.db')
cursor = db.cursor()
try:
    # drop_table_history = '''DROP TABLE HISTORY;'''
    # cursor.execute(drop_table_history)
    # db.commit()
    create_table_history = '''CREATE TABLE HISTORY (
                            USER TEXT NOT NULL,
                            QUERY TEXT NOT NULL);'''
    cursor.execute(create_table_history)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
cursor.close()
db.close()