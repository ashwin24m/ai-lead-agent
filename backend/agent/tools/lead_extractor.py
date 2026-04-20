from backend.services.llm_service import generate_response
import json


def extract_lead_info(user_input: str):
    prompt = f"""
You are an AI that extracts structured business lead information.

Extract the following fields from the user message:
- business (type of business)
- need (what they want)
- budget (number only if possible)
- urgency (low, medium, high)
- intent (just exploring, interested, ready to buy)

Return ONLY valid JSON. No explanation.

User message:
\"\"\"{user_input}\"\"\"
"""

    response = generate_response(prompt)

    try:
        return json.loads(response)
    except Exception:
        return {
            "error": "Failed to parse response",
            "raw": response
        }