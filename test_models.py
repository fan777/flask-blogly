from unittest import TestCase

from app import app
from models import db, User, Post

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()


class UserModelTestCase(TestCase):
    def setUp(self):
        User.query.delete()

    def tearDown(self):
        db.session.rollback()

    def test_property(self):
        user = User(first_name="Charlie", last_name="Fan", image_url="")
        db.session.add(user)
        db.session.commit()
        self.assertEquals("Charlie Fan", user.full_name)


class PostModelTestCase(TestCase):
    def setUp(self):
        Post.query.delete()

    def tearDown(self):
        db.session.rollback()

    def test_post(self):
        user = User(first_name="Charlie", last_name="Fan", image_url="")
        post = Post(title="post1", content="today i laughed")
        db.session.add(user)
        db.session.commit()
        db.session.add(post)
        db.session.commit()
        self.assertIn('today', self.__repr__)
