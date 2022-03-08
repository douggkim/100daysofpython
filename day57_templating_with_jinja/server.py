from flask import Flask, render_template
import random
import datetime
import requests
from guess_names import GuessNames

app = Flask(__name__)


@app.route("/")
def home(name=None):
    random_number = random.randint(1, 10)
    now = datetime.datetime.now().strftime("%Y")
    return render_template('index.html', num=random_number, date=now)


@app.route("/guess/<name>")
def guess(name):
    guess_names = GuessNames(name)
    guessed_age = guess_names.guess_age()
    guessed_gender = guess_names.guess_gender()
    return render_template('guess.html', name=name.title(), guessed_age=guessed_age, guessed_gender=guessed_gender)


@app.route("/blog")
def blog():
    blog_url = "https://www.npoint.io/docs/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
