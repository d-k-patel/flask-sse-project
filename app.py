from flask import Flask, render_template
from flask_sse import sse

from db import db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    app.register_blueprint(sse, url_prefix="/stream")

    db.init_app(app)

    return app


app = create_app()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello")
def publish_hello():
    sse.publish({"message": "Hello!"}, type="greeting")
    return "Message sent!"
