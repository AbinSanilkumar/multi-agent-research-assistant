import os
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_research_content(topic, plan):

    prompt = f"""
    You are an expert researcher.

    Topic:
    {topic}

    Research Plan:
    {plan}

    Write detailed research content
    for each section.

    Use proper headings.

    Keep the content informative
    and professional.
    """

    response = model.generate_content(prompt)

    return response.text
