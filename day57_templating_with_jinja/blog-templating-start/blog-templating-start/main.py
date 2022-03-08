from flask import Flask, render_template
from post import Post

app = Flask(__name__)


@app.route('/')
def home():
    post = Post()
    blog_post = post.get_blog()

    return render_template("index.html", blog_post=blog_post)

@app.route('/post/<blog_id>')
def see_post(blog_id):
    post = Post()
    blog_posts = post.get_blog()
    blog_post = blog_posts[int(blog_id)-1]

    return render_template("post.html", blog_post=blog_post)


if __name__ == "__main__":
    app.run(debug=True)
