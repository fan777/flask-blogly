from models import User, db
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

# Add new objects to session, so they'll persist
db.session.add(charlie)
db.session.add(jennifer)
db.session.add(jerry)

# Commit
db.session.commit()
