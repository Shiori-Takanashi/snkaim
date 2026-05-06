from flask import Flask

from .routes.items import items_bp
from .routes.sample import sample_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(sample_bp)
    app.register_blueprint(items_bp)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
