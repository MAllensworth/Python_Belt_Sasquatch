# from flask_app import app
# from flask import render_template, redirect, request, session
# from flask_app.models.sighting import Sighting
# from flask_app.models.user import User

# def check_session():
#     if 'user_id' not in session:
#         return redirect('/user/login')
#     user = User.get_by_id({"id":session['user_id']})
#     if not user:
#         return redirect('/user/logout')
#     return user

# def validate_sighting_form(form):
#     if not Sighting.validate_sighting(form):
#         return False
#     return True

# @app.route('/dashboard')
# def dashboard():
#     user = check_session()
#     return render_template('dashboard.html', user=user, sightings=Sighting.get_all())

# @app.route('/sightings/new')
# def create_sighting():
#     user =check_session()
#     return render_template('sighting_new.html', user=user)

# @app.route('/sightings/new/process', methods=['POST'])
# def process_sighting():
#     user = check_session()
#     if not validate_sighting_form(request.form):
#         return redirect('/sightings/new')

#     data = {
#         'user_id': session['user_id'],
#         'name': request.form['name'],
#         'location': request.form['location'],
#         'description': request.form['description'],
#         'date_made': request.form['date_made'],
#         'num_sasquatch': request.form['num_sasquatch'],
#     }
#     Sighting.save_sighting(data)
#     return redirect('/dashboard')

# @app.route('/sightings/<int:id>')
# def view_sighting(id):
#     user = check_session()
#     return render_template('sighting_view.html', user=user, sighting=Sighting.get_by_id({'id': id}))

# @app.route('/sightings/edit/<int:id>')
# def edit_sighting(id):
#     user = check_session()
#     return render_template('sighting_edit.html', user=user, sighting=Sighting.get_by_id({'id': id}))

# @app.route('/sightings/edit/process/<int:id>', methods=['POST'])
# def process_edit_sighting(id):
#     user = check_session()
#     if not validate_sighting_form(request.form):
#         return redirect(f'/sightings/edit/{id}')

#     data = {
#         'id': id,
#         'name': request.form['name'],
#         'location': request.form['location'],
#         'description': request.form['description'],
#         'date_made': request.form['date_made'],
#         'num_sasquatch': request.form['num_sasquatch'],
#     }
#     Sighting.update_sighting(data)
#     return redirect('/dashboard')

# @app.route('/sightings/delete/<int:id>')
# def delete_sighting(id):
#     check_session()
#     Sighting.delete_sighting({'id':id})
#     return redirect('/dashboard')


from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.sighting import Sighting
from flask_app.models.user import User

def check_session():
    if 'user_id' not in session:
        return redirect('/user/login')
    user = User.get_by_id({"id":session['user_id']})
    if not user:
        return redirect('/user/logout')
    return user

def validate_sighting_form(form):
    if not Sighting.validate_sighting(form):
        return False
    return True

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    user = check_session()
    return render_template('dashboard.html', user=user, sightings=Sighting.get_all())

@app.route('/sightings/new')
def create_sighting():
    if 'user_id' not in session:
        return redirect('/')
    user = check_session()
    return render_template('sighting_new.html', user=user)

@app.route('/sightings/new/process', methods=['POST'])
def process_sighting():
    if 'user_id' not in session:
        return redirect('/')
    user = check_session()
    if not validate_sighting_form(request.form):
        return redirect('/sightings/new')

    data = {
        'user_id': session['user_id'],
        'name': request.form['name'],
        'location': request.form['location'],
        'description': request.form['description'],
        'date_made': request.form['date_made'],
        'num_sasquatch': request.form['num_sasquatch'],
    }
    Sighting.save_sighting(data)
    return redirect('/dashboard')

@app.route('/sightings/<int:id>')
def view_sighting(id):
    if 'user_id' not in session:
        return redirect('/')
    user = check_session()
    return render_template('sighting_view.html', user=user, sighting=Sighting.get_by_id({'id': id}))

@app.route('/sightings/edit/<int:id>')
def edit_sighting(id):
    if 'user_id' not in session:
        return redirect('/')
    user = check_session()
    return render_template('sighting_edit.html', user=user, sighting=Sighting.get_by_id({'id': id}))

@app.route('/sightings/edit/process/<int:id>', methods=['POST'])
def process_edit_sighting(id):
    if 'user_id' not in session:
        return redirect('/')
    user = check_session()
    if not validate_sighting_form(request.form):
        return redirect(f'/sightings/edit/{id}')

    data = {
        'id': id,
        'name': request.form['name'],
        'location': request.form['location'],
        'description': request.form['description'],
        'date_made': request.form['date_made'],
        'num_sasquatch': request.form['num_sasquatch'],
    }
    Sighting.update_sighting(data)
    return redirect('/dashboard')

@app.route('/sightings/delete/<int:id>')
def delete_sighting(id):
    if 'user_id' not in session:
        return redirect('/')
    check_session()
    Sighting.delete_sighting({'id':id})
    return redirect('/dashboard')