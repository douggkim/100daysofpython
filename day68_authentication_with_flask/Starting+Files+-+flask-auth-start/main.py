from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, URL

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# define the callback for login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# Line below only required once, when creating DB.
# db.create_all()
# class RegisterForm(FlaskForm):
#     title = StringField("name", validators=[DataRequired()])
#     email = StringField("email", validators=[DataRequired()])
#     password = PasswordField("password", validators=[validators.DataRequired(),
#                                                      validators.EqualTo('confirm', message='Passwords must match')
#                                                      ])
#     confirm = PasswordField('Repeat Password')
#
#     submit = SubmitField("Submit Post")


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        check_if_existing = db.session.query(User).filter_by(email=request.form["email"]).first
        if check_if_existing is not None:
            flash("You are already a member!")
            return redirect(url_for('login'))
        else:
            new_user = User(name=request.form["name"],
                            email=request.form["email"],
                            password=generate_password_hash(request.form["password"],
                                                            method='pbkdf2:sha256',
                                                            salt_length=8))
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('secrets', name=request.form["name"]))
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return render_template("secrets.html", name=current_user.name)
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = db.session.query(User).filter_by(email=email).first()
        if user is not None:
            if check_password_hash(pwhash=user.password, password=password) :
                login_user(user)

                flash("Logged in successfully")
                next = request.args.get('next')

                return redirect(next or url_for('secrets', name=user.name))
            else:
                flash("The password does not match the email")
                return render_template('login.html')
        else:
            flash("The email does not exist")
            return render_template('login.html')

    return render_template("login.html")


@app.route('/secrets/<string:name>')
@login_required
def secrets(name):
    return render_template("secrets.html", name=name)


@app.route("/download")
@login_required
def download():
    return send_from_directory('static', 'files/cheat_sheet.pdf')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
