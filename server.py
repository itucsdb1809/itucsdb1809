# Intellect app
# Last 3 Works Done
# (06.11.18) A successful signup operation: Front-end variables (Form) -> Models methods -> Database record
# (07.11.18) Fix Heroku App crash
# (5.12.18)  Fix find user SQL for user sign in.
#
# Upcoming Project Works:
# Sequence I is finished -> though, check "login_user"
#
# Sequence II
#   Movies, Musics form and buttons (MyLists Page /Frontend) (2-4 hrs)
#   > Add the pages
#   > Simplify movies, musics pages
#   > Implement forms (add, update, delete, list) - UI side -
#   > Implement SQL operations  - Backend side -
#   Fix Foreign keys (1-1,5 hr)

# Sequence III
#   Improve UI (1 hr)
#   Wrap-up, and Heroku tests (1 hr)
#   Documentation, presentation (2-4 hrs)

from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from flask_login import login_user, LoginManager

from forms import *
from config import Config
import models
from db_table_operations import *
from werkzeug.security import generate_password_hash
from models import User, Music, Movie

app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)

global login
login = LoginManager(app)

def get_login():
    return login

@app.route("/")
def home_page():
#   tab.insert_user("username", "name", "surname", "password", 70, "gender")
    return render_template("homepage.html")


@app.route('/mylists')
def mylists_page():
    return render_template("mylists.html")

@app.route('/mylists/musics')
def musics_page():
    return render_template("musics.html")

@app.route('/mylists/movies')
def movies_page():
    return render_template("movies.html")

@app.route('/mylists/movies/add')
def movies_page():
    form = MovieAddForm(request.form)
    return render_template("add_movies.html", form=form)

@app.route('/signin', methods=['GET', 'POST'])
def signin_page():
    form = LoginForm()
    if form.validate_on_submit():
        found_user = find_user_by_username(form.username.data)
        user = User(found_user[1], found_user[2], found_user[3], found_user[4],
                    found_user[5], found_user[6], found_user[7])
        if user is None or not check_password(user.password, form.password.data):
            print("User signing failed")
            return redirect('/signin')
       # login_user(user, remember=form.remember_me.data) # will be reanalyzed
        print("User signed successful")
        return redirect('/')
    return render_template("signin.html", form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.name.data, form.surname.data, form.email.data,
                    form.password.data, form.age.data, form.gender.data)
        insert_user(user)
    return render_template("signup.html", form=form)

if __name__ == "__main__":
    # login_manager = LoginManager()
    # login_manager.init_app(app)
    # login_manager.login_view = 'login'
    app.run()
