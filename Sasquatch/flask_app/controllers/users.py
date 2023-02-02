from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/user/login')

@app.route('/user/login')
def login():
    if 'user_id' in session:
        return redirect('/dashboard')

    return render_template('index.html')

@app.route('/user/login/process', methods=['POST'])
def login_process():
    user = User.validate_login(request.form)
    if not user:
        return redirect('/user/login')
    session['user_id'] = user.id
    
    return redirect('/dashboard')

@app.route('/user/register/process', methods=['POST'])
def register_process():
    if not User.validate_registration(request.form):
        
        return redirect('/user/login')

    user_id = User.save(request.form)
    session['user_id'] = user_id
    
    return redirect('/dashboard')

@app.route('/user/logout')
def logout():
    session.clear()
    return redirect('/')


# from flask_app import app
# from flask import render_template, redirect, request, session
# from flask_app.models.user import User

# @app.route('/')
# def index():
#     return redirect('/user/login')

# @app.route('/user/login')
# def login():
#     if 'uuid' in session:
#         return redirect('/dashboard')

#     return render_template('index.html')

# @app.route('/user/login/process', methods=['POST'])
# def login_process():
#     user = User.validate_login(request.form)
#     if not user:
#         return redirect('/user/login')
#     # session['user_id'] = user.id
#         # if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
#         # flash("invalid Email/Password", "account_login_err")
#     # DON'T DO THIS.... INSTEAD USE A UUID
#     session['uuid'] = User.validate_login(request.form)
    
#     # return redirect("/")
#     return redirect('/dashboard')

# @app.route('/user/register/process', methods=['POST'])
# def register_process():
#     if not User.validate_registration(request.form):
        
#         return redirect('/user/login')

#     user_id = User.save(request.form)
#     session['uuid'] = user
    
#     return redirect('/dashboard')

# @app.route('/user/logout')
# def logout():
#     session.pop('uuid',0)
#     return redirect('/')