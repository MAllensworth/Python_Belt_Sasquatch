from flask import Flask, session, redirect
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

# @app.route('/user/logout')
# def logout():
#     if 'user_id' in session:
#         session.clear()
#     return redirect('/user/login')


# app.secret_key="this is a secret"

app.secret_key = "allensworthkeykey"