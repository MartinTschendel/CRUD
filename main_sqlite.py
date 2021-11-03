from database_sqlite import cursor, db
from setup_sqlite import cursor, db

def create_user(username, password):
    sql = ("INSERT INTO users(username, password) VALUES (?, ?)")
    cursor.execute(sql, (username, password,))
    db.commit()
    user_id = cursor.lastrowid
    print("Added user {}".format(user_id))

def get_users():
    sql = ("SELECT * FROM users ORDER BY username DESC")
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row)

def get_user(id):
    sql = ("SELECT * FROM users WHERE id = ?")
    cursor.execute(sql, (id,))
    result = cursor.fetchone()
    print(result)

def update_user_password(id, new_password):
    sql = ("UPDATE users SET password = ? WHERE id = ?")
    cursor.execute(sql, (new_password, id, ))
    db.commit()
    print("Updated password for user with id {}".format(id))

def delete_user(id):
    sql = ("DELETE FROM users WHERE id = ?")
    cursor.execute(sql, (id,))
    db.commit()
    print("Deleted user with id {}".format(id))

def drop_close():
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.close()
    db.close()

create_user('Chris', 'nice')
create_user('Chras', '12234')
create_user('Chrus', 'sun898')
create_user('chres', 'peppl')
#delete_user(2)
get_users()
#get_user()
#update_user_password(1, 'affe')
drop_close()