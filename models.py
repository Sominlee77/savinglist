# models.py

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Consultation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    contact_number = db.Column(db.String(20), nullable=False)
    consultation_date = db.Column(db.DateTime, default=datetime.utcnow)
    consultation_topic = db.Column(db.String(200), nullable=False)
    consultation_details = db.Column(db.Text)

    def __repr__(self):
        return f"<Consultation {self.student_name}>"
