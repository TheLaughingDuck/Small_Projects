# todoist_taskmaker
A python script for automatically creating multiple todoist tasks that follow a pattern. For example with task names such as

* "Buy milk", "Buy cheese", "Buy bread". 
* "Review lecture 1", "Review lecture 2", etc.

# How to use
1) Download and run the file `main.py` in the terminal.
2) Follow the command line instructions.
3) Verify that the tasks have been created.
4) Profit.

## Example usage
Here is an example usage of the script. The user wants to create 3 tasks with the respective contents/titles "Attend lecture 1", "Attend lecture 2", "Attend lecture 3". They download the repo, and run `main.py`. They may also need to install some of the dependencies: `tabulate`, `regex`.

### Access token
The user is prompted to give an access token, which can be found under your Todoist profile settings > Integrations > Developer. The example token given below is just keysmash.
```
-------------------------------------------------------------------
Hear ye, hear ye: The todoist taskmaker program has been initiated.
Please provide the information required to create your tasks.
-------------------------------------------------------------------

Please specify your personal API token. It can be found under settings in your profile.      
If the access token is already specified in an .env variable; leave this empty (press ENTER).
Access token>91838017839718938918193
-------------------------------------------------------------------
```

### Content
The user is now prompted to specify the content (text) of the tasks. The content pattern is specified, with the numbers replaced with a "fill variable" `AAA`.
```
Please specify the content (task name) of your tasks.
If you want to make multiple tasks with varying keywords, mark the location of the keywords with 3 identical uppercase letter, like "XXX", "YYY", or "ZZZ".
You can use multiple keywords in order to cycle through different sets of values.
Content (Task name)>Atttend lecture AAA     
-------------------------------------------------------------------
```

### Fill values
The user is now prompted to specify the "fill values" that iteratively should replace the fill variable `AAA`. The user specifies the lecture numbers "1,2,3". After this, the script prints a table of the tasks, and then sends requests to the API to create the tasks. Notice that for now all tasks are given priority 1 (lowest), label `Studying`, and due date "today".
```
Please specify the values of the respective fill variables below.
Separate the values with a comma, no space, for example:
1,2,3
Milk,Cheese,Bread

Please specify what values to iteratively replace AAA with.
fill values>1,2,3
-------------------------------------------------------------------
+------------------+----------+------------+-------------+
| content          | label    |   priority | duestring   |
+==================+==========+============+=============+
| Attend lecture 1 | Studying |          1 | today       |
+------------------+----------+------------+-------------+
| Attend lecture 2 | Studying |          1 | today       |
+------------------+----------+------------+-------------+
| Attend lecture 3 | Studying |          1 | today       |
+------------------+----------+------------+-------------+
```



