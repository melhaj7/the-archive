from typing import Optional
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy.types import Boolean

from app import db, login


class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(
        sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(
        sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    is_admin: so.Mapped[bool] = so.mapped_column(Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User: {self.username}'


class Book(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    title: so.Mapped[str] = so.mapped_column(sa.String(255), index=True)
    author: so.Mapped[str] = so.mapped_column(sa.String(120), index=True)
    publication_year: so.Mapped[int] = so.mapped_column()
    status: so.Mapped[str] = so.mapped_column(
        sa.String(120), nullable=False, default='available')

    @classmethod
    def get_all_books(cls):
        return cls.query.all()

    @classmethod
    def get_book_by_id(cls, book_id):
        return cls.query.get(book_id)

    @classmethod
    def add_book(cls, title, author, publication_year):
        book = cls(
            title=title,
            author=author,
            publication_year=publication_year
        )
        db.session.add(book)
        db.session.commit()
        return book

    @classmethod
    def update_book(cls, book_id, title=None, author=None, publication_year=None):
        book = cls.query.get(book_id)

        if not book:
            return {'error': 'Book not found'}

        is_updated = False
        if title:
            book.title = title
            is_updated = True
        if author:
            book.author = author
            is_updated = True
        if publication_year:
            book.publication_year = publication_year
            is_updated = True

        if is_updated:
            db.session.commit()
            return {'success': 'Changes applied successfully',
                    'book': {'id': book_id, 'title': title,
                             'author': author, 'publication_year': publication_year}}
        else:
            return {'error': 'No changes made'}

    @classmethod
    def delete_book(cls, book_id):
        book = cls.query.get(book_id)
        if book:
            db.session.delete(book)
            db.session.commit()
            return {'success': 'Book deleted successfully'}
        else:
            return {'error': 'Book not found'}


@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))
