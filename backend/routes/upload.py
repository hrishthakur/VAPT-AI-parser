from flask import Blueprint, request, jsonify
from utils.parser import parse_file, validate_dataframe
from database import SessionLocal
from models import Vulnerability
import logging
import os

logger = logging.getLogger(__name__)
upload_blueprint = Blueprint("upload", __name__)


@upload_blueprint.route("/api/upload", methods=["POST"])
def upload_file():
    try:
        if "file" not in request.files:
            logger.error("No file part in request")
            return jsonify({"error": "No file part"}), 400

        file = request.files["file"]
        if file.filename == "":
            logger.error("No selected file")
            return jsonify({"error": "No selected file"}), 400

        # Log file details
        logger.info(f"Processing file: {file.filename}")

        # Check file extension
        allowed_extensions = {".csv", ".json", ".pdf", ".xlsx"}
        file_ext = os.path.splitext(file.filename)[1].lower()
        if file_ext not in allowed_extensions:
            logger.error(f"Invalid file extension: {file_ext}")
            return jsonify(
                {
                    "error": f"File type not supported. Allowed types: {', '.join(allowed_extensions)}"
                }
            ), 400

        try:
            # Parse file
            logger.info("Starting file parsing")
            df = parse_file(file)
            logger.info(f"File parsed successfully. Found {len(df)} rows")

            # Validate DataFrame
            try:
                df = validate_dataframe(df)
                logger.info("DataFrame validation successful")
            except ValueError as e:
                logger.error(f"DataFrame validation failed: {str(e)}")
                return jsonify({"error": str(e)}), 400

            # Process rows
            session = SessionLocal()
            try:
                processed_count = 0
                for index, row in df.iterrows():
                    try:
                        logger.info(f"Processing row {index + 1}")

                        # Convert DataFrame row to dict and clean None values
                        row_dict = row.to_dict()
                        row_dict = {k: v for k, v in row_dict.items() if v is not None}

                        # Create vulnerability object
                        vuln = Vulnerability(**row_dict)
                        session.add(vuln)
                        processed_count += 1
                        logger.info(f"Row {index + 1} processed successfully")

                    except Exception as e:
                        logger.error(f"Error processing row {index + 1}: {str(e)}")
                        raise ValueError(f"Error processing row {index + 1}: {str(e)}")

                session.commit()
                logger.info(f"All rows processed. Total: {processed_count}")
                return jsonify(
                    {
                        "message": "File processed successfully",
                        "rows_processed": processed_count,
                    }
                ), 200

            except Exception as e:
                session.rollback()
                logger.error(f"Database error: {str(e)}")
                return jsonify({"error": f"Database error: {str(e)}"}), 500
            finally:
                session.close()

        except Exception as e:
            logger.error(f"File processing error: {str(e)}")
            return jsonify({"error": f"File processing error: {str(e)}"}), 500

    except Exception as e:
        logger.error(f"Upload error: {str(e)}")
        return jsonify({"error": str(e)}), 500
