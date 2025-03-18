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

##GROQ_API_KEY = "curl https://api.groq.com/openai/v1/chat/completions"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("No GROQ_API_KEY set for Groq API")

def process_image(image_path, query):
    try:
       with open(image_path,"rb") as image_file:
        image_content = image_file.read()
        ##base64.b64decode(image_content).decode("utf-8")
        encoded_image = base64.b64encode(image_content).decode("utf-8")
    except Exception as e:
        logger.error(f"Error reading image file: {str(e)}")
        return {"error": "Error reading image file"}
    
if __name__ == "__main__":
    image_path = "test1.png"
    query = "what are the encoders used in the image?"
    result = process_image(image_path, query)
    print(result)