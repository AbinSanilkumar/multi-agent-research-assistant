from agents.planner import generate_research_plan
from agents.researcher import generate_research_content


def run_research_workflow(topic):

    plan = generate_research_plan(topic)

    research_content = generate_research_content(
        topic,
        plan
    )

    return {
        "plan": plan,
        "research_content": research_content
    }