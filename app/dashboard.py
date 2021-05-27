import json
from random import randint

import flask_login
from flask import Blueprint, render_template, redirect, url_for

from db import session_scope, Device

dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/')
@dashboard_bp.route('/devices')
@flask_login.login_required
def index():
    with session_scope() as session:
        devs = session.query(Device).all()
        return render_template('dashboard/dashboard.html', devs=devs)


@dashboard_bp.route('/devices/<int:id>', methods=['GET'])
@flask_login.login_required
def device(id):
    redirect(url_for('dashboard.index'))
    with session_scope() as session:
        dev = session.query(Device).get(id)
        if dev is None:
            redirect(url_for('dashboard.index'))
        data = [{'data': i, 'value': randint(0, 10) * i} for i in range(10)]
        data = json.dumps(data)
        return render_template('dashboard/device.html', device=dev, data=data, type="Active energy")


@dashboard_bp.route('/devices/add')
@flask_login.login_required
def add():
    return 'not implemented'
