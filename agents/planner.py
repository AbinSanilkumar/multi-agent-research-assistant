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


def generate_research_plan(topic):

    prompt = f"""
    You are a professional research planner.

    Create a structured research plan for:

    {topic}

    Return only section titles.

    Example:

    1. Introduction
    2. Applications
    3. Benefits
    4. Challenges
    5. Future Scope
    6. Conclusion
    """

    response = model.generate_content(prompt)

    return response.text