from flask import Flask, jsonify, request
from flask_cors import CORS
from routes.upload import upload_blueprint
from routes.fix_generator import fix_blueprint
from routes.vulnerabilities import vuln_blueprint
from database import init_db
from dotenv import load_dotenv
import os
import logging

load_dotenv()

DATABASE_url = os.getenv("DATABASE_URL")
OPEN_API_KEY = os.getenv("OPEN_API_KEY")
# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_app():
    app = Flask(__name__)

    # Allow both localhost and 127.0.0.1
    allowed_origins = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]

    # Configure CORS
    CORS(
        app,
        resources={
            r"/api/*": {
                "origins": allowed_origins,
                "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                "allow_headers": ["Content-Type", "Authorization"],
                "supports_credentials": True,
            }
        },
    )

    # Add CORS headers to all responses
    @app.after_request
    def after_request(response):
        origin = request.headers.get("Origin")
        if origin in allowed_origins:
            response.headers.add("Access-Control-Allow-Origin", origin)
            response.headers.add(
                "Access-Control-Allow-Headers", "Content-Type,Authorization"
            )
            response.headers.add(
                "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
            )
            response.headers.add("Access-Control-Allow-Credentials", "true")
        return response

    try:
        # Initialize Database
        logger.info("Initializing database...")
        init_db()

        # Register Blueprints
        logger.info("Registering blueprints...")
        app.register_blueprint(upload_blueprint)
        app.register_blueprint(fix_blueprint)
        app.register_blueprint(vuln_blueprint)

        return app
    except Exception as e:
        logger.error(f"Error during app initialization: {str(e)}")
        raise


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
