from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey, Boolean
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from bs4 import BeautifulSoup
import requests
from forms import CreateTodo, RegisterForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'lSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)


# Configure Flask-Login's Login Manager
login_manager = LoginManager()
login_manager.init_app(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLES

class Users(UserMixin, db.Model):
    __tablename__ = "users"
    # This will act like a List of BlogPost objects attached to each User.
    # The "author" refers to the author property in the Todos class.
    todos = relationship("Todo", back_populates="user")
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(100))

class Todo(db.Model):
    __tablename__ = "todos"
    user = relationship("Users", back_populates="todos")
    user_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    body: Mapped[str] = mapped_column(Text, nullable=False)



with app.app_context():
    db.create_all()

#CREATE GRAVATAR
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(Users, user_id)

# hashing user password when creating new user
@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if request.method == "POST":
        email= form.email.data
        result= db.session.execute(db.select(Users).where(Users.email == email))
        user=result.scalar()
        if user:
            flash("You already have an account")
            return redirect(url_for("login"))
        hashed_and_salted_password = generate_password_hash(
            form.password.data,
            method="pbkdf2:sha256",
            salt_length=8
        )
        new_user=Users(
            email= email,
            name= form.name.data,
            password=hashed_and_salted_password
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("home"))
    return render_template("register.html", form=form, logged_in=current_user.is_authenticated)


# TODO: Retrieve a user from the database based on their email. 
@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email=form.email.data
        password=form.password.data
        result=db.session.execute(db.select(Users).where(Users.email == email))
        if result:
            user = result.scalar()
            if not user:
                flash("That email does not exist, please try again.")
                return redirect(url_for('login'))
            elif not check_password_hash(user.password, password):
                flash("Wrong password. Try again.")
                return redirect(url_for("home"))
            else:
                login_user(user)
                return redirect(url_for("home"))

            flash("Wrong email. Try again.")
    return render_template("login.html", form=form, logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():

    logout_user()
    return redirect(url_for('home'))


@app.route('/', methods=["GET", "POST"])
def home():

    return redirect(url_for("add_todo"))


@app.route("/new-todo", methods=["GET", "POST"])
def add_todo():
    user = str(current_user)[7::2]

    result = db.session.execute(db.select(Todo).where(Todo.user_id == user))
    todos = result.scalars().all()


    form = CreateTodo()
    if form.validate_on_submit():
        new_post = Todo(

            body=form.body.data,
            user=current_user,
        )
        db.session.add(new_post)
        db.session.commit()

        return render_template("index.html", form=form, all_tasks=todos, logged_in=current_user.is_authenticated)
    return render_template("index.html", form=form, task=todos, logged_in=current_user.is_authenticated)



if __name__ == "__main__":
    app.run(debug=True, port=5002)
