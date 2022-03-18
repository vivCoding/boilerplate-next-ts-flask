from flask import Blueprint, jsonify

example_blueprint = Blueprint("example", __name__)

@example_blueprint.route("/", methods=["GET"])
def index():
	return jsonify("api example index"), 200