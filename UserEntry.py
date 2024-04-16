from flask import session
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

class UserEntry:
    def __init__(self):
        self.db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='heartdb'
        )

    def register_user(self, name, email, password):
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM user WHERE email = %s',(email,))
        exist_user = cursor.fetchone()
        if exist_user:
            cursor.close()
            print("user exixts!!!")
            return False
        else:
            cursor.execute("INSERT INTO user (name, email, password) VALUES (%s,%s,%s)",(name,email,password))
            self.db.commit()
            cursor.close()
            print("success")
            return True

    def login_user(self, email, password):
        try:
            cursor = self.db.cursor()
            cursor.execute('SELECT * FROM user WHERE  email = %s', (email,))
            user = cursor.fetchone()
            if user:
                cursor.execute('SELECT password FROM user WHERE email = %s',(email,))
                password1 = cursor.fetchone()
                if password == password1[0]: #checking the password with hashed
                    session['email'] = email
                    #print("login successful")
                    cursor.close()
                    return True
                else:
                    #print("password incorrect!!")
                    cursor.close()
                    return False
            else:
                #print("the user doesnt exists, register now !!")
                return None
        except Exception as e:
            print(f'error occured:{e}')
            return None
#for testing module

#ue = UserEntry()
#ue.login_user("john@example.com", "123456")