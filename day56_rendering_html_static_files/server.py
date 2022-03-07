from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello(name=None):
    # html files will have to be inside a folder called 'templates'
    # images for html files will have to be inside a folder called 'static' -> static/photo.img
    return render_template('index.html')

@app.route("/doug")
def doug(name=None):
    return render_template("introduction.html")

if __name__ == "__main__":
    app.run(debug=True)
