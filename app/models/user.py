from .. import db
from flask_login import UserMixin 

class User(db.Model, UserMixin):
 __tablename__ = 'users'
 id = db.Column(db.Integer, primary_key = True)
 Username = db.Column(db.String(255), unique=True, nullable=False)
 email = db.Column(db.String(255), unique=True, nullable=False)
 Phone = db.Column(db.Integer, unique=True, nullable=False)
 password = db.Column(db.String(255),nullable=False)

 def __repr__(self):
  return f'<User: {self.email}>'
 
 def get_id(self):
  return self.id