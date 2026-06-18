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


def generate_final_report(
    topic,
    research_content,
    fact_check_report
):

    prompt = f"""
    Create a professional research report.

    Topic:
    {topic}

    Research Content:
    {research_content}

    Fact Check Report:
    {fact_check_report}

    Format:

    Executive Summary

    Introduction

    Main Findings

    Verified Insights

    Challenges

    Recommendations

    Conclusion

    Write in a professional report style.
    """

    response = model.generate_content(prompt)

    return response.text
