def evaluate_task(tasks,duration_days:int):
    max_tasks = max(3,duration_days // 7 + 1)

    if len(tasks) > max_tasks:
        return {
            "passed":False,
            "reason":"Too many tasks for given duration"
        }

    return{
        "passed":True,
        "reason":None
    }