"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.Text())
    posts = db.relationship('Post', backref='user',
                            cascade='all, delete-orphan')

    def __repr__(self):
        """Show info about user."""
        return f'<User {self.id} {self.first_name} {self.last_name} {self.image_url}>'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text())
    created_at = db.Column(db.DateTime(), nullable=False,
                           default=db.func.current_timestamp())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        """Show info about post"""
        return f'<Post {self.title} {self.created_at}>'
