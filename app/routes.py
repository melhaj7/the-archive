from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user
import sqlalchemy as sa
# import requests
from app import app, db
from app.forms import LoginForm
from app.models import User


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(sa.select(User).where(
            User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


# @app.route('/books', methods=['GET'])
# def get_title():
#     api_url = 'https://openlibrary.org/works/OL45804W.json'
#     res = requests.get(api_url)

#     if res.status_code == 200:
#         data = res.json()
#         title = data.get('title', 'title not found')
#         return render_template('book.html', title=title, description=data.get('description', 'No desc found!'))
#     else:
#         return f'error{res.status_code}! failed to fetch data'
