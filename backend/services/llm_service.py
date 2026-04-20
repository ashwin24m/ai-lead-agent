import time
from openai import OpenAI
from backend.core.config import settings
from backend.core.logger import logger

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def generate_response(prompt: str, retries: int = 2):
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )

            output = response.choices[0].message.content
            logger.info(f"LLM response success")

            return output

        except Exception as e:
            logger.error(f"LLM error: {e}")
            time.sleep(1)

    return "Error: Unable to generate response"