from flask import session
import mysql.connector

class FeedBack():
    def __init__(self):
        self.db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database = 'heartdb'
        )

    def submit_feedback(self, name, email, phone, message):
        cursor = self.db.cursor()
        try:
            cursor.execute('INSERT INTO feedback (name,email,phone,message) VALUES (%s,%s,%s,%s)', (name, email, phone, message))
            self.db.commit()
            cursor.close()
            print("test")
            return True
        except Exception as e:
            print(f"Error submitting feedback: {e}")
            self.db.rollback()
            cursor.close()
            return False

            
#for testing module
#feedback = FeedBack()
#feedback.submit_feedback('likith','likithbopanna222@gmail.com','0123456789','hi hello iam under the water, please save me')