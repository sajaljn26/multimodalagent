import base64
import requests
import io
from PIL import Image
from dotenv import load_dotenv
import os
import logging

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("No GROQ_API_KEY set for Groq API")

def make_api_response(model, messages):
    try:
        response = requests.post(
            GROQ_API_URL,
            json={
                "model": model,
                "messages": messages,
                "max_tokens": 1000
            },
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            timeout=30
        )
        return response
    except requests.RequestException as e:
        logger.error(f"Request failed for model {model}: {str(e)}")
        return None

def process_image(image_path, query):
    try:
        with open(image_path, "rb") as image_file:
            image_content = image_file.read()
            encoded_image = base64.b64encode(image_content).decode("utf-8")

        try:
            img = Image.open(io.BytesIO(image_content))
            img.verify()
        except Exception as e:
            logger.error(f"Error opening image file: {str(e)}")
            return {"error": "Error opening image file"}

        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": query},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}}
                ]
            }
        ]

        responses = {}
        for model_name, model_id in [
            ("llama11b", "llama-3.2-11b-vision-preview"),
            ("llama90b", "llama-3.2-90b-vision-preview")
        ]:
            response = make_api_response(model_id, messages)
            if response and response.status_code == 200:
                result = response.json()
                answer = result["choices"][0]["message"]["content"]
                logger.info(f"Model {model_name} response: {answer}")
                responses[model_name] = answer
            else:
                error_msg = f"Error processing image with model {model_name}: {response.text if response else 'No response'}"
                logger.error(error_msg)
                responses[model_name] = error_msg

        return responses

    except Exception as e:
        logger.error(f"Error reading image file: {str(e)}")
        return {"error": "Error reading image file"}

if __name__ == "__main__":
    image_path = "test1.png"
    query = "What are the encoders used in the image?"
    result = process_image(image_path, query)
    print(result)
