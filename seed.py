from models import User, Post, Tag, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add users
charlie = User(first_name='Charlie', last_name='Fan', image_url='')
jennifer = User(first_name='Jennifer', last_name='Fan', image_url='')
jerry = User(first_name='Jerry', last_name='Fan', image_url='')
db.session.add(charlie)
db.session.add(jennifer)
db.session.add(jerry)
db.session.commit()

# Add posts
post1 = Post(title='post1 apple', content='today i ate an apple',
             created_at=None, user_id=1)
post2 = Post(title='post2 dog', content='today i pet a dog',
             created_at=None, user_id=1)
db.session.add(post1)
db.session.add(post2)
db.session.commit()

# Add tags
tag1 = Tag(name='apple')
tag2 = Tag(name='dog')
tag3 = Tag(name='today')
post1.tags.append(tag1)
post1.tags.append(tag3)
post2.tags.append(tag2)
post2.tags.append(tag3)
db.session.add(tag1)
db.session.add(tag2)
db.session.add(tag3)
db.session.add(post1)
db.session.add(post2)
db.session.commit()
