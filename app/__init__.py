import os
from flask import Flask
from dotenv import load_dotenv

def create_app():
    load_dotenv()

    app = Flask(__name__)

    app.config["S3_BUCKET"] = os.getenv("S3_BUCKET", "")
    app.config["AWS_REGION"] = os.getenv("AWS_REGION", "")

    from .routes import bp as core_bp
    app.register_blueprint(core_bp)

    return app