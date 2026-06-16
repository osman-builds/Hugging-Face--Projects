import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Initialize Gemini API
client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))

# Generate a poem
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Generate a poem about the sea."
)
print(response.text)