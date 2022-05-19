import os

from flask import Flask, render_template

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='n3b0-zd3Cb',
        DATABASE=os.path.join(app.instance_path, 'aviandm.sqlite'),
        ENV='development',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        # flask не создает эту папку автоматически, но она нужна, потому что
        # будет создан файл базы данных sqlite 
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def mainpage():
        return render_template('index.html')
        # return '<p>mainpage</p>'

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import printer
    app.register_blueprint(printer.bp)
    # закомментировано, потому что теперь в printer.bp задан url_prefix=...
    # app.add_url_rule('/printer', endpoint='index')


    app.logger.info(app.url_map)
    return app


