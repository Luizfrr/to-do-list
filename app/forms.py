from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from app.models import Task
from app import db

class TaskForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired()])
    description = StringField('Descrição', validators=[DataRequired()])
    btnSubmit = SubmitField('Adicionar')

    def save(self):
        task = Task(
            title = self.title.data,
            description = self.description.data
        )

        db.session.add(task)
        db.session.commit()