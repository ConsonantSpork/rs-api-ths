from flask import Blueprint, render_template, request, redirect, url_for

from db import session_scope, Converter
from .forms import ConversionAdd

conversion_bp = Blueprint('conversion', __name__)


@conversion_bp.route('/conversion')
def conversions():
    with session_scope() as session:
        converters = session.query(Converter).all()
        session.expunge_all()
    return render_template('conversion/conversions.html', convs=converters)


@conversion_bp.route('/conversion/<int:id>')
def conversion(id):
    with session_scope() as session:
        conversion = session.query(Converter).filter(Converter.id == id).first()
        session.expunge(conversion)
    return render_template('conversion/conversion.html', conv=conversion)


@conversion_bp.route('/conversion/add', methods=['GET', 'POST'])
def add():
    form = ConversionAdd(request.form)
    if request.method == 'POST' and form.validate():
        with session_scope() as session:
            converter = Converter(name=form.name, source_code=form.source)
            session.add(converter)
        return redirect(url_for('conversion.conversions'))
    return render_template('conversion/add.html', form=form)
