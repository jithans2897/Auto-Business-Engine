import os
from openai import OpenAI
from app.agents.tools import get_project_data, optimize_resources

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def run_llm_agent(db, project_id):
    try:
        history = []

        for step in range(3):

            prompt = f"""
You are an AI business optimization agent.

Available tools:
1. get_project_data
2. optimize_resources

Previous steps:
{history}

Decide next action.

Respond ONLY like:
Action: <tool_name>
"""

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            action_text = response.choices[0].message.content.strip()

            # 🔍 Decide which tool to call
            if "get_project_data" in action_text:
                result = get_project_data(db, project_id)

            elif "optimize_resources" in action_text:
                result = optimize_resources(db, project_id)

            else:
                return {
                    "status": "error",
                    "message": "Invalid action from AI",
                    "ai_output": action_text
                }

            # Save step to history
            history.append({
                "step": step,
                "action": action_text,
                "result": str(result)
            })

        return {
            "status": "success",
            "steps": history
        }

    except Exception as e:
        return {
            "status": "error",
            "message": "AI agent failed",
            "details": str(e)
        }