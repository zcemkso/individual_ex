from flask import render_template, Blueprint, flash, redirect, url_for, request
from sqlalchemy.exc import IntegrityError
from app import db
from app.main.forms import SignupForm
from app.models import User, Forecast, City

bp_main = Blueprint('main', __name__)


@bp_main.route('/', )
def index():
    return render_template('index.html')


@bp_main.route('/signup', methods=['POST', 'GET'])
def sign_up():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        try:
            db.session.add(user)
            db.session.commit()
            flash('You are now a registered user!')
            return redirect(url_for('main.index'))
        except IntegrityError:
            db.session.rollback()
        flash(f'ERROR! Unable to register {user.username}. Please check your details are correct and try again.')
    return render_template('signup.html', form=form)


@bp_main.route('/forecast', methods=['GET'])
def forecast():
    forecasts = Forecast.query.join(User).join(City).add_columns(User.username, City.city).all()
    return render_template('forecast.html', forecast=forecasts)


@bp_main.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        term = request.form['search_term']
        if term == "":
            flash("Enter a name to search for")
            return redirect('/')
        results = City.query.filter(City.city.like(term)).join(Forecast).add_columns(Forecast.forecast, Forecast.comment, Forecast.forecast_datetime).all()
        if not results:
            flash("No city found with that name.")
            return redirect('/')
        return render_template('search_results.html', results=results)
    else:
        return redirect(url_for('main.index'))
