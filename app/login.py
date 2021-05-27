from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user

from db import session_scope, User
from .forms import LoginPassword

login_bp = Blueprint('login', __name__)


@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginPassword(request.form)
    if request.method == 'POST' and form.validate():
        with session_scope() as session:
            user = session.query(User).filter(User.login == form.login.data).first()
            if user is None:
                flash('No such user', 'error')
            elif user.check_password(form.password.data):
                login_user(user)
                return redirect(url_for('dashboard.index'))
            else:
                flash('Invalid password', 'error')
    return render_template('login/login.html', form=form)


@login_bp.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return redirect(url_for('dashboard.index'))
