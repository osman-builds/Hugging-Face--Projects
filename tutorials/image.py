import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Initialize Gemini API
client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))

# Generate image
response = client.models.generate_images(
    model="imagen-4.0-fast-generate-001",
    prompt="A cute alien creature in a spaceship",
    config=genai.types.GenerateImagesConfig(
        number_of_images=1,
        aspect_ratio="16:9"
    )
)

# Save the image
if response.images:
    image = response.images[0]
    image.save("generated_image.png")
    print("✓ Image saved as 'generated_image.png'")
else:
    print("✗ Failed to generate image")