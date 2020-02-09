from flask import render_template, Blueprint, flash
from app.main.forms import SignupForm

bp_main = Blueprint('main', __name__)

@bp_main.route('/')
def index():
    return render_template('index.html')


@bp_main.route('/signup/', methods=['POST', 'GET'])
def sign_up():
    form = SignupForm()
    if form.validate_on_submit():
        flash('Sign Up requested')
        return render_template('main.index')
    return render_template('signup.html', form=form)
