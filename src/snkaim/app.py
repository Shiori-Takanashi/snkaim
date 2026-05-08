from flask import Flask

from .routes.companies_routes import companies_bp
from .routes.home_routes import home_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(home_bp)
    app.register_blueprint(companies_bp)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
