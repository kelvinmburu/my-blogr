from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# Create a flask instance
app = Flask(__name__)
# Add database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# Secret key
app.config['SECRET_KEY'] = "kigonyisecrit"
# Initialize database connection
db = SQLAlchemy(app)


# Create users models
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Create a string representation
    def __repr__(self):
        return '<Name %r>' % self.name
    
    
# Create a user form class
class UserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Submit')


# Create a form class
class NamerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    form = UserForm()
    return render_template('add_user.html', form=form)

# Create a route decorator
@app.route("/")
def index():
    return render_template('index.html')

# Users page
@app.route("/user/<name>")
def user(name):
    return render_template('user.html', name=name)


# Custom errors page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


# Creates name page
@app.route('/name', methods=['GET',  'POST'])
def name():
    name = None
    form = NamerForm()
    
    # Validate form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form submitted successfully!")
    return render_template('name.html', name=name, form=form)
