from app import app
from flask import redirect, render_template, url_for

from app.models import Task
from app.forms import TaskForm
from app import db

@app.route('/', methods=['GET', 'POST'])
def home():
    task = Task.query.all()
    form = TaskForm()
    context = {}
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('home'))

    return render_template('index.html', tasks=task, form=form, context=context)

@app.route('/concluir/<int:id>', methods=['POST'])
def complete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()

    return redirect(url_for('home'))
