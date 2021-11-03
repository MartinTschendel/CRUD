from database import cursor, db

def create_user(username, password):
    sql = ("INSERT INTO users(username, password) VALUES (%s, %s)")
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
    sql = ("SELECT * FROM users WHERE id = %s")
    cursor.execute(sql, (id,))
    result = cursor.fetchone()
    print(result)

def update_user_password(id, new_password):
    sql = ("UPDATE users SET password = %s WHERE id = %s")
    cursor.execute(sql, (new_password, id, ))
    db.commit()
    print("Updated password for user with id {}".format(id))

def delete_user(id):
    sql = ("DELETE FROM users WHERE id = %s")
    cursor.execute(sql, (id,))
    db.commit()
    print("Deleted user with id {}".format(id))


#create_user('Chris', 'idiot')
#create_user('Chras', 'brot')
create_user('Chrus', 'arsch')
#delete_user(2)
get_users()
#get_user(2)
#update_user_password(1, 'affe')