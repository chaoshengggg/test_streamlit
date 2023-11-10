from deta import Deta
import os
import streamlit_authenticator as stauth
import bcrypt



DETA_KEY = 'c0uj8mh2gqe_4xTZsSAGuWCsEPaCvQyuAqHUfMhgwsyc'
#DETA_KEY = os.getenv('DETA_KEY')

deta = Deta(DETA_KEY)
db = deta.Base('test_db')

def insert_user(username, email, password, datetime):
    try:
        salt = bcrypt.gensalt()
        byte_password = password.encode('utf-8')
        hashed_password = bcrypt.hashpw(byte_password, salt)
        hashed_password_str = hashed_password.decode('utf-8')
        #print("Inserting user:", {'key': username, 'email': email, 'password': hashed_password_str})
        result = db.put({'key': username, 'email': email, 'password': hashed_password_str,'datetime': datetime})
        return result
    except Exception as e:
        print(f"Error occurred during user insertion: {e}")


def update_user(username, updates):
    return db.update(updates, username)



def fetch_all_users():
    res = db.fetch()
    return res.items

