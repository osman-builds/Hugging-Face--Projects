import os

from ddgs import DDGS
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))

query = input("Enter your search question: ").strip()

if not query:
    raise SystemExit("No search question provided.")

with DDGS() as ddgs:
    search_results = list(ddgs.text(query, max_results=5))

context = "\n\n".join(
    f"Title: {item.get('title', '')}\nLink: {item.get('href', '')}\nSnippet: {item.get('body', '')}"
    for item in search_results
)

prompt = (
    "Answer the user's question using the web search results below. "
    "If the results do not contain enough live information, say so clearly.\n\n"
    f"Question: {query}\n\n"
    f"Search results:\n{context}"
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)

print(response.text)