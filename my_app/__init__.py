from flask import Flask
app = Flask(__name__)

import my_app.source.views

from my_app.source.views import my_view
app.register_blueprint(my_view)


