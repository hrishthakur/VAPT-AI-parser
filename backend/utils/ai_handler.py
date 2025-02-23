import openai
import logging
import os
import re
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

logger = logging.getLogger(__name__)

# Set the OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_vulnerability_details(issue, tech_stack):
    """Generate comprehensive vulnerability details using AI."""
    try:
        prompt = f"""
        As a cybersecurity expert, analyze this vulnerability:
        Issue: {issue}
        Technology Stack: {tech_stack}

        Provide a detailed analysis in the following format:
        1. CWE ID (if applicable)
        2. Business Impact
        3. Best secure solution
        4. Business-friendly fix with minimal impact
        5. Temporary mitigation or quick patch
               """

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a cybersecurity expert providing vulnerability analysis.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            max_tokens=1000,
        )

        # Parse the response
        response_text = response.choices[0].message.content

        # Extract CWE ID using basic pattern matching
        cwe_id = None
        if "CWE-" in response_text:
            cwe_match = re.search(r"CWE-\d+", response_text)
            if cwe_match:
                cwe_id = cwe_match.group(0)

        # Split response into sections
        sections = response_text.split("\n")

        # Extract business impact
        business_impact = ""
        for section in sections:
            if "Business Impact:" in section or "2." in section:
                business_impact = section.split(":", 1)[-1].strip()
                break

        # Extract fixes
        best_fix = ""
        business_friendly_fix = ""
        temporary_mitigation = ""

        for section in sections:
            if "Best secure solution:" in section or "3." in section:
                best_fix = section.split(":", 1)[-1].strip()
            elif "Business-friendly fix:" in section or "4." in section:
                business_friendly_fix = section.split(":", 1)[-1].strip()
            elif "Temporary mitigation:" in section or "5." in section:
                temporary_mitigation = section.split(":", 1)[-1].strip()

        return {
            "cwe_id": cwe_id,
            "business_impact": business_impact,
            "best_fix": best_fix,
            "business_friendly_fix": business_friendly_fix,
            "temporary_mitigation": temporary_mitigation,
        }

    except Exception as e:
        logger.error(f"Error generating vulnerability details: {str(e)}")
        return {
            "cwe_id": None,
            "business_impact": "Error generating business impact",
            "best_fix": "Error generating fix",
            "business_friendly_fix": "Error generating business-friendly fix",
            "temporary_mitigation": "Error generating mitigation",
    }