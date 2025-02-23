from flask import Blueprint, jsonify
from database import SessionLocal
from models import Vulnerability
import logging

logger = logging.getLogger(__name__)
vuln_blueprint = Blueprint("vulnerabilities", __name__)


@vuln_blueprint.route("/api/vulnerabilities", methods=["GET"])
def get_vulnerabilities():
    """Fetch all stored vulnerabilities from the database."""
    session = SessionLocal()
    try:
        vulnerabilities = session.query(Vulnerability).all()

        vuln_list = [
            {
                "id": vuln.id,
                "issue_name": vuln.issue_name,
                "severity": vuln.severity,
                "tech_stack": vuln.tech_stack,
                "cwe_id": vuln.cwe_id,
                "business_impact": vuln.business_impact,
                "best_fix": vuln.best_fix,
                "business_friendly_fix": vuln.business_friendly_fix,
                "temporary_mitigation": vuln.temporary_mitigation,
            }
            for vuln in vulnerabilities
        ]

        return jsonify({"vulnerabilities": vuln_list}), 200
    except Exception as e:
        logger.error(f"Error fetching vulnerabilities: {str(e)}")
        return jsonify({"error": str(e), "vulnerabilities": []}), 500
    finally:
        session.close()
