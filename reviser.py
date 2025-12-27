import json
from llm_client import call_llm

SYSTEM_PROMPT = """
You are a task-revision AI.
Simplyfy the task list to fit constraints.
Return ONLY valid JSON.
"""

def revise_tasks(tasks,duration_days):
    user_prompt = f"""
    Original tasks: {tasks}
    Duration: {duration_days} days

    Simplify the tasks to fit duration.
    Return in format:
    {{"tasks":["task1","task2","..."]}}
    """
    raw = call_llm(SYSTEM_PROMPT,user_prompt)
    return json.loads(raw)["tasks"]