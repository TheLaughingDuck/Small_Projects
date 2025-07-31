from regex import finditer
from helpers import zip_recycle

def make_tasks():
    """Prompts the user for information about the tasks
    """
    task_info = {"task":"", "labels":[], "due":"", "fill":{}, "priority":"", "subtasks":[]}

    # GET ACCESS TOKEN
    print("\nPlease specify your personal API token. It can be found under settings in your profile.")
    print("If the access token is already specified in an .env variable; leave this empty (press ENTER).")
    access_token = input("Access token>")
    print("-------------------------------------------------------------------")

    # GET TASK NAME
    print("\nPlease specify the task name.")
    print("For multiple tasks: mark the location(s) of the iterating keyword(s) with 3 identical uppercase letters, e.g. \"AAA\", \"YYY\".")
    print("You can use multiple keywords in order to cycle through different sets of values.")
    task_info["task"] = input("Task name>")
    print("-------------------------------------------------------------------")

    # GET SUBTASK NAMES
    print("\nPlease specify the name of a subtask. If no subtasks should be created, leave empty.")
    print("The name can contain filler variables.")
    user_input = input("Subtask name>")
    while user_input != "":
        task_info["subtasks"].append({"task":user_input})
        print("\nIf no more subtasks should be created, leave empty.")
        user_input = input("Subtask name>")
    print("-------------------------------------------------------------------")
    
    # GET LABLES
    print("\nPlease specify the labels to apply to the tasks. If multiple, separate with a comma, no space.")
    task_info["labels"] = input("Task labels>").split(",")
    print("-------------------------------------------------------------------")

    # GET DUESTRING
    print("\nPlease specify the due date of the tasks. Possible formats include:")
    print("\"2025-05-31\", \"today\", \"tomorrow\", \"next week\"")
    task_info["due"] = input("Due date>")
    print("-------------------------------------------------------------------")

    # GET PRIORITY
    print("\nPlease specify the priority of the tasks, values in [1,2,3,4] (lowest to highest).")
    task_info["priority"] = input("Priority>")
    print("-------------------------------------------------------------------")

    # GET/SET SUBTASK LABELS AND DUESTRINGS
    if task_info["subtasks"] != []:
        print("\nShould the subtask(s) inherit labels and/or duedate from their main tasks?")
        user_input = input("Inherit labels and duestring? [labels/due/both/neither]>")

        for subtask in task_info["subtasks"]:
            if user_input == "both":
                subtask["labels"] = task_info["labels"]
                subtask["due"] = task_info["due"]

            elif user_input == "labels":
                subtask["labels"] = task_info["labels"]
                print("\nPlease specify subtask due date.")
                subtask["due"] = input("Due date>")

            elif user_input == "due":
                subtask["due"] = task_info["due"]
                print("\nPlease specify subtask labels.")
                subtask["labels"] = input("Labels>")

            if user_input == "neither":
                print("\nPlease specify subtask labels.")
                subtask["labels"] = input("Labels>")
                print("\nPlease specify subtask due date.")
                subtask["due"] = input("Due date>")
    print("-------------------------------------------------------------------")

    # FIND FILL VARIABLES (3 identical uppercase letters, e.g. AAA, BBB, UUU)
    variable_pattern = r'([A-Z])\1{2}'
    all_text = " ".join([task_info["task"], *[subtask["task"] for subtask in task_info["subtasks"]]])
    fill_variables = [match.group(0) for match in finditer(variable_pattern, all_text)]
    fill_variables = {variable:None for variable in fill_variables}

    # GET FILL VALUES
    if len(fill_variables) != 0:
        print("\nPlease specify the values of the respective fill variables below.")
        print("Separate the values with a comma, no space, for example:")
        print("\"1,2,3\", \"Milk,Cheese,Bread\"")
    for variable in fill_variables:
        print("\nPlease specify what values to iteratively replace", variable, "with.")
        fill_variables[variable] = input("fill values>").split(",")
        print("-------------------------------------------------------------------")
    task_info["fill"] = fill_variables

    # Generate list of tasks, containing their respective properties
    generated_tasks = []
    for fill_values in zip_recycle(task_info["fill"].values()):
        # Make copy of content to replace variables with fill values
        content_i = task_info["task"]

        # Replace each variable with corresponding value
        for variable, value in zip(task_info["fill"].keys(), fill_values):
            content_i = content_i.replace(variable, value)
        
        # Save the generated task properties
        #generated_tasks.append([content_i, task_info["labels"], task_info["priority"], task_info["due"]])
        generated_tasks.append({"task":content_i, "labels":task_info["labels"], "due":task_info["due"], "priority":task_info["priority"], "subtasks":task_info["subtasks"]})

    return access_token, generated_tasks
