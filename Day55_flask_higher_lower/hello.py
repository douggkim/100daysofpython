from flask import Flask, request
from TextStyling import *

app = Flask(__name__)
textstyling = TextStyling()


@app.route('/')
def hello_world():
    return "<h1 style='text-align:center'>hello world</h1><p style='text-align: center'" \
           ">is a greeting</p>" \
           "<img src='https://ninjatune.net/images/artists/mr-oizo-main.jpg'>"


@app.route('/bye')
@make_bold
@make_underlined
@make_em
def bye():
    return "Bye"


@app.route("/name/<string:username>")
def greet(username):
    return f"Hello {username}!"


if __name__ == "__main__":
    app.run(debug=True)
