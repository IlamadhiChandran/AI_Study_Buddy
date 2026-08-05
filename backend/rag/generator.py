import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_answer(context, question):
    """
    Generate an answer using Gemini based only on the retrieved context.
    """

    prompt = f"""
You are an AI Study Buddy.

Answer ONLY using the context below.

If the answer is not present in the context, reply exactly:

I couldn't find that information in the uploaded PDF.

Context:
{context}

Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
    )

    return response.text