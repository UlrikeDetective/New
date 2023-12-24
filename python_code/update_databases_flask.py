from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///example.db"  # Adjusted database name
db = SQLAlchemy(app)  # Passed the app instance to SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)  # Added missing parenthesis

# Removed unnecessary app_context blocks

# Create tables
db.create_all()

# Add a new book
new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)
db.session.add(new_book)
db.session.commit()

# Retrieve all books ordered by title
all_books = Book.query.order_by(Book.title).all()

# Retrieve a specific book by title
book = Book.query.filter_by(title="Harry Potter").first()

# Update a specific book by title
book_to_update = Book.query.filter_by(title="Harry Potter").first()
if book_to_update:
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()

# Update a specific book by ID
book_id = 1
book_to_update_by_id = Book.query.get(book_id)
if book_to_update_by_id:
    book_to_update_by_id.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()
