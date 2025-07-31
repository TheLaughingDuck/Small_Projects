from helpers import POST_tasks
from user_interaction import make_tasks
from tabulate import tabulate

print("-------------------------------------------------------------------")
print("Hear ye, hear ye: The todoist taskmaker program has been initiated.")
print("Please provide the information required to create your tasks.")
print("-------------------------------------------------------------------")

# GET TASK INFORMATION FROM USER
token, generated_tasks = make_tasks()

# FILL IN missing values
if token == "":
    from os import getenv
    from dotenv import load_dotenv #pip install python-dotenv
    load_dotenv()
    access_token = getenv("ACCESS_KEY")

# Print summary of tasks
formated_tasks = [[task["task"], ", ".join(task["labels"]), task["due"], task["priority"], len(task["subtasks"])] for task in generated_tasks]
print(tabulate(formated_tasks, ["content", "label(s)", "due", "priority", "# subtasks"], tablefmt="grid"))

# Let user review and accept/cancel the task creation
print("\nPlease review the tasks in the table above before sending them to the API.")
user_input = input("Create tasks [y/n]?>")
if user_input == "y":
    # Send task POST requests
    POST_tasks(access_token, generated_tasks)
else:
    print("\nTask creation was cancelled by user.")
    quit()