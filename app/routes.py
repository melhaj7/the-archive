from flask import render_template, flash, redirect, url_for
import requests
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Logging user: {}, remember me: {}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


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
