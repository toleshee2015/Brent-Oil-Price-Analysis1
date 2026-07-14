from flask import Flask
from flask_cors import CORS

from routes.prices import prices_bp

app = Flask(__name__)

CORS(app)

app.register_blueprint(prices_bp, url_prefix="/api")


@app.route("/")
def home():
    return {
        "message": "Brent Oil Price Analysis API"
    }


if __name__ == "__main__":
    app.run(debug=True)