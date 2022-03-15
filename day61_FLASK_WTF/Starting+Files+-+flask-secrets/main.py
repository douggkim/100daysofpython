from flask import Flask, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap

# TODO 0 : Set up Flask 
app = Flask(__name__)
Bootstrap(app)
app.secret_key = "some secret string"


# TODO 1 : Create FlaskForm
class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Log In')


# TODO 2 : Set up Router
@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('index.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    loginform = LoginForm()
    # return True if submit button is successfully passed
    if loginform.validate_on_submit():
        if loginform.email.data == "admin@email.com" and loginform.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('login.html', form=loginform)


if __name__ == '__main__':
    app.run(debug=True)
