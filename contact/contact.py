from flask import Blueprint, render_template
from flask import g

contact = Blueprint('contact', __name__, template_folder='templates')

@contact.route("/contacto", endpoint="contact_es")
@contact.route("/contacta", endpoint="contact_ca")
@contact.route("/contact-us", endpoint="contact_en")
def detail(lang):
    return render_template('contact.html')

@contact.route("/", endpoint="contact_index")
def index(lang):
    return render_template('contact-index.html')


