from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

def create_app():
    app = Flask(__name__)
    PrometheusMetrics(app)

    from app.routes import main
    from app.health import health
    app.register_blueprint(main)
    app.register_blueprint(health)

    return app
