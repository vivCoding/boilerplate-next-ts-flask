from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_session import Session
from flask_cors import CORS
from database.connect import Connection
from routes.api import api_blueprint
from routes.api.example import example_blueprint

load_dotenv()
Connection.init()

app = Flask(__name__)
CORS(app, methods=["OPTIONS", "GET", "POST"], supports_credentials=True)
app.config.from_object("config.Config")
Session(app)

@app.route("/")
def index():
	return jsonify("welcome to the backend!")

app.register_blueprint(api_blueprint, url_prefix="/api")
app.register_blueprint(example_blueprint, url_prefix="/api/example")

if __name__ == "__main__":
	print ("Server running on port 5000!\n", "=" * 50)
	app.run("0.0.0.0", port=5000, debug=True)