import sqlite3

db = sqlite3.connect('plan.db')
cursor = db.cursor()
async def start_db():
  cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
               id TEXT,
               name TEXT,
               phone_num TEXT
)
''')

async def add_user(id,name,phone_num):
    cursor.execute('''
    INSERT INTO users(
                   id,name,phone_num
    )
                   VALUES(?,?,?)
''',(id,name,phone_num))
    db.commit()

async def show_user():
    cursor.execute('SELECT * FROM users')
    ids = cursor.fetchall()
    return ids





