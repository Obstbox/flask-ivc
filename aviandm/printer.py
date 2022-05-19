import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, current_app
)

from werkzeug.exceptions import abort

from aviandm.auth import login_required
from aviandm.db import get_db

bp = Blueprint('printer', __name__, url_prefix='/printer')
@bp.route('/')
def index():
    db = get_db()
    printers = db.execute(
        'SELECT id, model, cartridge, location, install_date'
        ' FROM printers ORDER BY install_date DESC'
    ).fetchall()
    return render_template('printer/index.html', printers=printers)

@bp.route('/add', methods=['POST', 'GET'])
@login_required
def add():
    if request.method == 'POST':
        model = request.form['model'] 
        cartridge = request.form['cartridge'] 
        location = request.form['location'] 
        install_date = request.form['install_date'] 
        error = None

        # but why if it handled by html-form?
        if not model or not cartridge or not location:
            error = 'model, cartridge and location are required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO printers (model, cartridge, location, install_date)'
                ' VALUES (?, ?, ?, ?)',
                (model, cartridge, location, install_date)
            )
            db.commit()
            return redirect(url_for('printer.index'))

    return render_template('printer/add.html')


# for both update() and delete()
def get_printer(id):
    printer = get_db().execute(
        'SELECT model, cartridge, location, install_date'
        ' FROM printers WHERE id = ?',
        (id,)
    ).fetchone()

    if printer is None:
        abort(404, f"Printer id {id} doesn't exist.")

    # if user_not_logged_in():
    #   abort(403)

    return printer



@bp.route('/update')
def update():
    pass




