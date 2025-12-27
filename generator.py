import json
from llm_client import call_llm

SYSTEM_PROMPT = """
You are a task-planning AI
Break goals into realistic subtasks
Return ONLY valid JSON
"""

def generate_tasks(goals:str,duration_days:int):
    user_prompt = f"""
    Goal: {goals}
    Duration: {duration_days} days

    Break this into list of high level tasks
    Return in format:
    {{"tasks":["task1","task2","..."]}}
    """
    raw = call_llm(SYSTEM_PROMPT,user_prompt)
    return json.loads(raw)["tasks"]