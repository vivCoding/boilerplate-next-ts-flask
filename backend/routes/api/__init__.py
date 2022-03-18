from flask import Blueprint, jsonify

api_blueprint = Blueprint("/", __name__)

@api_blueprint.route("/", methods=["GET"])
def index():
	return jsonify("api index"), 200