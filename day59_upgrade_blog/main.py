from flask import Flask, render_template, request
from send_mail import send_mail
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()


@app.route("/")
def index():
    return render_template("index.html", data=response)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = str(request.form["email"])
        phone = request.form["phone"]
        message = str(request.form["message"])

        print(name)
        print(email)
        print(phone)
        print(message)
        print(type(message))

        sendmail = send_mail()
        sendmail.send(msg=message, to_addr=email)
        return render_template("contact.html", h1_message="Message Successfully Sent.")
    return render_template("contact.html", h1_message="Contact Me")

@app.route("/post/<post_id>")
def see_post(post_id):
    target_post = response[int(post_id)-1]
    return render_template("post.html", data=target_post)

# @app.route("/form-entry", methods=["POST"])
# def receive_data():
    


if __name__ == "__main__":
    app.run(debug=True)
