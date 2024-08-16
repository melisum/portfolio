from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey, Boolean


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location URL', validators=[DataRequired(), URL()])
    img = StringField('Image URL', validators=[DataRequired(), URL()])
    loc= StringField('Which part of the city is the coffee located in? ', validators=[DataRequired()])
    socket= SelectField('Are there sockets?', validators=[DataRequired()], choices=["✘","🔌"])
    toilet=SelectField('Is there a toilet?', validators=[DataRequired()], choices=["✘", "🚽"])
    wifi = SelectField('Wifi?', validators=[DataRequired()], choices=["✘","📶"] )
    calls = SelectField('Is it possible to make calls?', validators=[DataRequired()], choices=["✘","☎️"])
    seats = StringField('How many seats are there?', validators=[DataRequired()])
    price = StringField('How much does in espresso cost? ', validators=[DataRequired()])
    submit = SubmitField('Submit')



# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)
# CONFIGURE TABLES
class Cafes(db.Model):
    __tablename__ = "cafe"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    map_url: Mapped[str] = mapped_column(String(100), unique=True)
    img_url: Mapped[str] = mapped_column(String(100), unique=True)
    location: Mapped[str] = mapped_column(String(100))
    has_sockets: Mapped[str] = mapped_column(Boolean)
    has_toilet: Mapped[str] = mapped_column(Boolean)
    has_wifi: Mapped[str] = mapped_column(Boolean)
    can_take_calls: Mapped[str] = mapped_column(Boolean)
    seats: Mapped[str] = mapped_column(String(100))
    coffee_price: Mapped[str] = mapped_column(String(100))


with app.app_context():
    db.create_all()
# all Flask routes
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET","POST"])
def add_cafe():
    form = CafeForm()
    if form.socket.data == "✘":
        socket=False
    else:
        socket = True
    if form.toilet.data == "✘":
        toilet = False
    else:
        toilet = True
    if form.wifi.data == "✘":
        wifi=False
    else:
        wifi=True
    if form.calls.data == "✘":
        calls=False
    else:
        calls=True

    if form.validate_on_submit():
        cafe = Cafes(
            name=form.cafe.data,
        map_url=form.location.data,
        img_url=form.img.data,
        location=form.loc.data,
        has_sockets=socket,
        has_toilet=toilet,
        has_wifi=wifi,
        can_take_calls=calls,
        seats=form.seats.data,
        coffee_price=form.price.data,
        )
        db.session.add(cafe)
        db.session.commit()

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    # result = db.session.execute(db.select(Cafes))
    cafe_list = Cafes.query
    return render_template('cafes.html', cafes=cafe_list)



if __name__ == '__main__':
    app.run(debug=True)



