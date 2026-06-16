import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Initialize Gemini API
client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))

# List all available models
print("Available models:")
for model in client.models.list():
    print(f"  - {model.name}")
