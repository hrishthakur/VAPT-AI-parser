import pandas as pd
import logging
import os

logger = logging.getLogger(__name__)


def parse_file(file):
    """
    Parse uploaded file and return a pandas DataFrame
    """
    try:
        file_ext = os.path.splitext(file.filename)[1].lower()

        if file_ext == ".csv":
            return pd.read_csv(file)
        elif file_ext == ".json":
            return pd.read_json(file)
        elif file_ext == ".xlsx":
            return pd.read_excel(file, engine="openpyxl")
        elif file_ext == ".pdf":
            # Add PDF parsing logic here
            return pd.DataFrame()
        else:
            raise ValueError(f"Unsupported file type: {file_ext}")

    except Exception as e:
        logger.error(f"Error parsing file: {str(e)}")
        raise


def validate_dataframe(df):
    """
    Validate that the DataFrame has the required columns
    """
    required_columns = {"issue_name", "severity", "tech_stack"}

    current_columns = set(df.columns)
    missing_columns = required_columns - current_columns

    if missing_columns:
        logger.error(f"Missing columns: {missing_columns}")
        logger.error(f"Current columns: {current_columns}")
        raise ValueError(f"Missing required columns: {missing_columns}")

    return df
