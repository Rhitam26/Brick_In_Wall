from brs import app , db
from datetime import datetime


class Admin(db.Model):
    with app.app_context():
        id = db.Column(db.Integer, primary_key = True, )
        name = db.Column(db.String(200), nullable =False)
        email = db.Column(db.String(100), nullable =False, unique =True)
        date_added = db.Column(db.DateTime, default= datetime.utcnow)

    def __repr__(self) -> str:
        return '<Name %r>' % self.name