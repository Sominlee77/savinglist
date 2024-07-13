# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consultations.db'

db = SQLAlchemy(app)

# 데이터베이스 모델 임포트
from models import Consultation

# 데이터베이스 테이블 생성
db.create_all()

class ConsultationForm(FlaskForm):
    student_name = StringField('Student Name', validators=[DataRequired()])
    contact_number = StringField('Contact Number', validators=[DataRequired()])
    consultation_topic = StringField('Consultation Topic', validators=[DataRequired()])
    consultation_details = TextAreaField('Consultation Details')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ConsultationForm()
    if form.validate_on_submit():
        student_name = form.student_name.data
        contact_number = form.contact_number.data
        consultation_topic = form.consultation_topic.data
        consultation_details = form.consultation_details.data

        new_consultation = Consultation(student_name=student_name, 
                                        contact_number=contact_number,
                                        consultation_topic=consultation_topic,
                                        consultation_details=consultation_details)
        db.session.add(new_consultation)
        db.session.commit()

        return redirect(url_for('index'))

    consultations = Consultation.query.order_by(Consultation.consultation_date.desc()).all()
    return render_template('index.html', form=form, consultations=consultations)

if __name__ == '__main__':
    app.run(debug=True)
