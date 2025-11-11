from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from .models import User, db

controllers_bp = Blueprint('controllers_bp', __name__)  # ✅ only once!

@controllers_bp.route('/about')
def about():
    return render_template('about.html')

@controllers_bp.route('/')
def home():
    return render_template('welcome.html')

@controllers_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        pwd = request.form.get('password')   # ✅ matches register.html

        existing_user = User.query.filter(
            (User.username == username) | (User.email == email)
        ).first()

        if existing_user:
            return "User already exists!"

        new_user = User(username=username, email=email)
        new_user.set_password(pwd)
        db.session.add(new_user)
        db.session.commit()
        return "Registration successful! Go to Login."

    return render_template('register.html')


@controllers_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        pwd = request.form.get('pass')   # ✅ matches login.html

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(pwd):
            login_user(user)
            if user.type == 'admin':
                return redirect(url_for('controllers_bp.admin_dashboard'))
            else:
                return redirect(url_for('controllers_bp.user_dashboard'))
        else:
            return "Invalid username or password."

    return render_template('login.html')


@controllers_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('controllers_bp.home'))


@controllers_bp.route('/user_dash')
@login_required
def user_dashboard():
    if current_user.type != 'general':
        return "Unauthorized access!"
    
    # Pass the logged-in user object to template
    return render_template('user_dash.html', this_user=current_user)


@controllers_bp.route('/admin_dash')
@login_required
def admin_dashboard():
    if current_user.type != 'admin':
        return "Unauthorized access!"

    # later we’ll query these counts dynamically
    users_count = User.query.count()
    requested_count = Request.query.filter_by(status='pending').count() if 'Request' in globals() else 0
    granted_count = Request.query.filter_by(status='approved').count() if 'Request' in globals() else 0
    available_count = Ebook.query.filter_by(status='available').count() if 'Ebook' in globals() else 0

    return render_template(
        'admin_dash.html',
        this_user=current_user,
        users_count=users_count,
        requested_count=requested_count,
        granted_count=granted_count,
        available_count=available_count
    )

@controllers_bp.route('/create_ebook', methods=['GET', 'POST'])
@login_required
def create_ebook():
    if current_user.type != 'admin':
        return "Unauthorized access!"

    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        url = request.form.get('url')

        # For now, just print — later this will go into your Ebook model
        print(f"New E-Book Created: {title} by {author} ({url})")

        return redirect(url_for('controllers_bp.admin_dashboard'))

    return render_template('create_eb.html', this_user=current_user)
