from flask_login import UserMixin


def initialize_login():
    from server import login
    global login
    login = login

class User(UserMixin):
    def __init__(self, username, name, surname, email, password, age, gender):
        self.username = username
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.age = int(age)
        self.gender = gender
        print("User object created")

    @login.user_loader
    def load_user(id):
        return User.query.get(int(id)) # change this to return users from DB with the given ID

class Music:
    def __init__(self, name, genre, duration_in_seconds, singer, year):
        self.name= name
        self.genre = genre
        self.duration_in_seconds = duration_in_seconds
        self.singer = singer
        self.year = year
        print("Music object created")


class Movie:
    def __init__(self, title, year, duration_in_minutes, director, genre):
        self.title = title
        self.year = year
        self.genre = genre
        self.duration_in_minutes = duration_in_minutes
        self.director = director
        print("Movie object created")