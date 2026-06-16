import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Initialize Gemini API
client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))

# Run the agent with a task
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Calculate the sum of numbers from 1 to 10"
)
print(response.text)