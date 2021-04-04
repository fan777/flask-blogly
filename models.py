"""Models for Blogly."""
import datetime
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
                           default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        """Show info about post"""
        return f'<Post {self.title} {self.created_at}>'

    @property
    def friendly_date(self):
        return self.created_at.strftime('%a %b %d %Y, %I:%M %p')


class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text(), nullable=False, unique=True)
    posts = db.relationship('Post', secondary="posts_tags", backref='tags')

    def __repr__(self):
        """Show info about tag"""
        return f'<Post {self.name}>'


class PostTag(db.Model):
    __tablename__ = 'posts_tags'

    post_id = db.Column(db.Integer, db.ForeignKey(
        'posts.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)
