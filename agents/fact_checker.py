import os
import re
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def fact_check_content(content):

    prompt = f"""
    You are a fact checking assistant.

    Analyze the following research content.

    Return:

    Confidence Score: XX

    Verified Claims:
    - claim

    Potential Issues:
    - issue

    Content:

    {content}
    """

    response = model.generate_content(prompt)

    text = response.text

    score = 0

    match = re.search(
        r'Confidence Score:\s*(\d+)',
        text
    )

    if match:
        score = int(match.group(1))

    return {
        "report": text,
        "score": score
    }
