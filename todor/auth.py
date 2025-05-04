from flask import Blueprint ,render_template,redirect,url_for,request,flash
from werkzeug.security import generate_password_hash,check_password_hash

from .models import User
from . import db

# Create a blueprint for authentication

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form[username]
        password = request.form[password]

        user = User(username=username, password=generate_password_hash(password))
        user_name = User.query.filter_by(username=username).first()
        if user_name == None:
            db.session.add(user)
            db.session.commit()
            flash('User created successfully', 'success')
            return redirect(url_for('auth.login'))

    return render_template('auth/register.html')

@bp.route('/login')
def login():
    return render_template('auth/login.html')
