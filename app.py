from flask import Flask, request, render_template
from flask import g
from flask.ext.babel import Babel, gettext as _

AVAILABLE_LOCALES = ['en', 'ca', 'es']

app = Flask(__name__)
babel = Babel(app)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'

from contact import contact
app.register_blueprint(contact, url_prefix='/<lang>/contact')

@babel.localeselector
def get_locale():
    lang = request.path[1:].split('/', 1)[0]
    if lang in AVAILABLE_LOCALES:
        return lang
    else:
        return 'en'

@app.before_request
def func():
    g.babel = babel
    g.language = get_locale()

@app.route("/")
@app.route("/ca/", endpoint="ca")
@app.route("/es/", endpoint="es")
@app.route("/en/", endpoint="en")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
