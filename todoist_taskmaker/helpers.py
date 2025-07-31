from todoist_api_python.api import TodoistAPI
from itertools import cycle

def POST_tasks(access_token, task_list):
    """Takes a todoist access token (see settings > Integrations > Developer),
        and sends an "add_task" request to the TodoistAPI with parameters
        for each task in task_list, which also should contain values for some
        parameter: content, labels, priority, due_string."""
    
    api = TodoistAPI(access_token)

    # CREATE TASKS
    for task in task_list:
        try:
            # Put together and send a POST request
            #task_object = api.add_task(content=task[0], labels=task[1], priority=task[2], due_string=task[3])
            task_object = api.add_task(content=task["task"], labels=task["labels"])#, priority=task["priority"], due_string=task["due"])

            for subtask in task["subtasks"]:
                api.add_task(content=subtask["task"], parent_id=task_object.id)#, labels=subtask["labels"], priority=subtask["priority"], due_string=subtask["due"], parent_id = task_object.id)

        except Exception as error:
            print(error)

def zip_recycle(iterable):
    """Takes an iterable, where each element is an iterable of elements.
    The iterables are zipped (by zip), but shorter elements are recycled.
    The longest element in fill_values will be gone through once."""
    
    # Handle zero-length iterable
    if len(iterable) == 0: return([])

    # Regulate zip_recycle to stop once the longest element in fill_values has been passed once
    longest = max([len(x) for x in iterable])
    count = 0

    # Unpack list of recycled iterables.
    zipped_elements = zip(*[cycle(sublist) for sublist in iterable])
    for element in zipped_elements:
        yield element
        
        count += 1
        if count >= longest: break