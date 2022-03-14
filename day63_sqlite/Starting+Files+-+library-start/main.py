from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

# TODO 0 : FLASK SET UP
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# TODO 1 : DB SET UP
db = SQLAlchemy(app)


# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=False, nullable=False)
    author = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)

    def __repr__(self):
        return "<Book %r>" % self.title


db.create_all()


# harry_potter = Book(title="Harry Potter", author="J.K. Rowling", rating=9.3)
# db.session.add(harry_potter)
# db.session.commit()
#
# # Query all the books
# all_books = db.session.query(Book).all()
# print(all_books)
#
# # Update a particular record by query
# book = Book.query.filter_by(title="Harry Potter").first()
# print(book)
# book.title = "Harry Potter and the Chamber of Secrets"
# db.session.commit()
#
# # Update a record by primary key
# book_id = 1
# book_to_update = Book.query.get(book_id)
# book_to_update.title = "Harry Potter and the Goblet of Fire"
# db.session.commit()
#
# # query the updated book
# updated_book = Book.query.get(book_id)
# print(updated_book)
#
# # Delete a particular record by Primary key
# book_id = 1
# book_to_delete = Book.query.get(book_id)
# db.session.delete(book_to_delete)
# db.session.commit()
#
# # try to query the deleted book
# all_books = Book.query.all()
# print(all_books)

# TODO 2 : ROUTING

@app.route('/', methods=["POST", "GET"])
def home():
    if request.method == "POST":
        new_rating = request.form["rating"]
        target_id = request.form["id"]
        book_to_update = Book.query.get(target_id)
        book_to_update.rating = new_rating
        db.session.commit()
    all_books = db.session.query(Book).all()
    print(all_books)
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # CREATE RECORD
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route('/edit/<int:id>', methods=["GET"])
def edit(id):
    target_book = Book.query.get(id)
    print(target_book)
    return render_template("edit.html", book=target_book)


@app.route('/delete/<int:id>', methods=["GET"])
def delete(id):
    target_book = Book.query.get(id)
    print(target_book)
    db.session.delete(target_book)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
