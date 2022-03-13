from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()


@app.route("/")
def index():
    return render_template("index.html", data=response)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<post_id>")
def see_post(post_id):
    target_post = response[int(post_id)-1]
    return render_template("post.html", data=target_post)

if __name__ == "__main__":
    app.run(debug=True)
