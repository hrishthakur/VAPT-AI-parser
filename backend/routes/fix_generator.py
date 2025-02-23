from flask import Blueprint, request, jsonify
from utils.ai_handler import generate_vulnerability_details

fix_blueprint = Blueprint("fix_generator", __name__)


@fix_blueprint.route("/api/generate_fix", methods=["POST"])
def generate_fix():
    data = request.json
    issue = data.get("issue")
    tech_stack = data.get("tech_stack")

    if not issue or not tech_stack:
        return jsonify(
            {"error": "Both 'issue' and 'tech_stack' are required fields."}
        ), 400

    # Use the correct function to generate vulnerability details
    details = generate_vulnerability_details(issue, tech_stack)

    return jsonify({"details": details})
