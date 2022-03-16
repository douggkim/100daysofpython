from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, HiddenField
from wtforms.validators import DataRequired
from search_movie import SearchMovie

# TODO 1 :SET UP FLASK

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie.db"
db = SQLAlchemy(app)

Bootstrap(app)


# TODO 2 : SET UP DB

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(700))
    rating = db.Column(db.Integer, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(700))
    img_url = db.Column(db.String(500), nullable=True)


db.create_all()
search_movie = SearchMovie()


# TODO 3 : CREATE WTF FORM for editing rating

class EditForm(FlaskForm):
    rating_form = IntegerField('Your Rating Out of 10 e.g. 7.5')
    review_form = StringField('Your Review')
    id_form = HiddenField('id')
    submit = SubmitField('Done')


class AddForm(FlaskForm):
    title_form = StringField('Movie Title', validators=[DataRequired(message="Enter the title of the movie, plz")])
    submit = SubmitField('Add Movie')


# TODO 3 : CREATE ROUTERS
@app.route("/")
def home():
    movies = db.session.query(Movie).order_by(Movie.rating.desc())
    print(movies)
    ranking = 1
    for movie in movies:
        movie.ranking = ranking
        ranking += 1
        db.session.commit()
    return render_template("index.html", movies=movies)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        search_keyword = form.title_form.data
        return redirect(url_for('select', search_keyword=search_keyword))
    return render_template("add.html", form=form)


@app.route("/edit/<target_id>", methods=["GET", "POST"])
def edit(target_id):
    form = EditForm()
    if form.validate_on_submit():
        target_movie = Movie.query.get(target_id)
        target_movie.rating = form.rating_form.data
        target_movie.review = form.review_form.data
        db.session.commit()

        return redirect(url_for('home'))
    return render_template("edit.html", form=form, target_id=target_id)


@app.route("/select", methods=["GET", "POST"])
def select():
    search_keyword = request.args.get("search_keyword")
    movie_list = search_movie.search(search_keyword)
    return render_template("select.html", movies=movie_list)


@app.route("/insert")
def insert_movie():
    movie_title = request.args.get("movie_title")
    img_url = "https://image.tmdb.org/t/p/w500" + str(request.args.get("img_url"))
    release_date = request.args.get("release_date")[0:4]
    movie_description = request.args.get("movie_description")
    new_movie = Movie(title=movie_title, year=release_date, description=movie_description, img_url=img_url)
    db.session.add(new_movie)
    db.session.flush()
    db.session.refresh(new_movie)
    new_movie_id = new_movie.id

    db.session.commit()
    return redirect(url_for('edit', target_id=new_movie_id))


@app.route("/delete")
def delete_movie():
    target_id = request.args.get("target_id")
    target_movie = Movie.query.get(target_id)
    db.session.delete(target_movie)
    db.session.commit()

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
