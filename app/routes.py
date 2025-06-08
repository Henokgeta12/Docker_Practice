from flask import Blueprint, render_template, redirect, request
from .models import Vote
from . import db

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        vote = request.form.get('animal')
        if vote in ['Dog', 'Cat']:
            new_vote = Vote(animal=vote)
            db.session.add(new_vote)
            db.session.commit()
        return redirect('/results')
    return render_template('index.html')

@main.route('/results')
def results():
    dog_votes = Vote.query.filter_by(animal='Dog').count()
    cat_votes = Vote.query.filter_by(animal='Cat').count()
    return render_template('results.html', dog_votes=dog_votes, cat_votes=cat_votes)
