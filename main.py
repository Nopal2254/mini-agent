from generator import generate_tasks
from evaluator import evaluate_task
from reviser import revise_tasks
from agent_logger import log

def run_agent():
    goal = input("Enter your goal: ")
    duration_days = int(input("Enter duration in days: "))

    log("GOAL",f"Received goal:'{goal}'")
    log("CONSTRAINT",f"Time limit:{duration_days} days")
    
    log("ACTION","Generating initial plan task")
    tasks = generate_tasks(goal,duration_days)

    log("OUTPUT",f"Generated tasks: {tasks}")

    log("EVALUATION","Checking if plan is fit constraints")
    evaluation = evaluate_task(tasks,duration_days)

    if not evaluation["passed"]:
        log("DECISION","Plan rejected: {evaluation['reason']}")
        log("ACTION","Revising task plan")

        tasks = revise_tasks(tasks,duration_days)

        log("OUTPUT",f"Revised tasks: {tasks}")
        log("DECISION",f"Revised plan accepted")
    else:
        log("DECISION",f"Plan accepted")

    log("OUTPUT","\n Final task plan:")
    for i,task in enumerate(tasks,1):
        log("OUTPUT",f"{i}. {task}")

if __name__ == "__main__":
    run_agent()
