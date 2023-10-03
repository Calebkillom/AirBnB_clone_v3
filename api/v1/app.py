#!/usr/bin/python3
""" python script that creates variable app, instance of Flask """
import os
from flask import Flask
from models import storage
from api.v1.views import app_views

"""Create a Flask instance"""
app = Flask(__name__)

""" Register the blueprint app_views to your Flask instance app """
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_storage(exception):
    """ Method that Closes the storage when the app context is torn down."""
    storage.close()


if __name__ == "__main__":
    """ Get the host and port from environment variables or use defaults """
    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(os.environ.get('HBNB_API_PORT', 5000))

    """ Run the Flask server """
    app.run(host=host, port=port, threaded=True)
