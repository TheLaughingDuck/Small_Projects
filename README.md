# Small_Projects
Small, cool projects that I work on from time to time. Kind of a staging area before I invest more time in a project.

## [Work Clock](https://github.com/TheLaughingDuck/Small_Projects/tree/main/Work_clock)
A widget for tracking time during workdays. Can be paused for breaks, and it saves information such as start time, end time and total hours worked for the whole workday as well as the individual work sessions in a local sqlite database, which can be inspected by running "inspect_data.py". I suggest you create a desktop shortcut to "clock_v2.pyw", and then just click it at the start of each day. Close the application when you are finished for the day. I consider 5 hours of actual focused, deep work a workday, so it shows the percentage done below the timer.

![Clock demonstration](https://github.com/TheLaughingDuck/Small_Projects/blob/main/Work_clock/clock.png)

## [ML Tools](https://github.com/TheLaughingDuck/Small_Projects/tree/main/ml_tools)
Functions and classes that I find useful to me when working with machine learning.

* **[TrainingTracker](https://github.com/TheLaughingDuck/Small_Projects/blob/main/ml_tools/training.py)**: A custom class for tracking metrics such as accuracy, loss, and time throughout model training. Usage is as simple as

```
from ml_tools.training import TrainingTracker
T = TrainingTracker(logdir=".", filename="data.json")

# The epoch loop
T.start()
for epoch in range(10):
    T.update(epoch=epoch, metric="loss", value=0.2)
T.stop()

# Then inspect the data in "./data.json" 
```

* **[unique](https://github.com/TheLaughingDuck/Small_Projects/blob/main/ml_tools/discovery.py)**: A custom function that identifies the uniques values in a pandas dataframe, and reports their frequencies. I found myself using this a lot in a recent project.

```
from ml_tools.discovery import unique

unique(df)
```

## [Todoist Taskmaker](https://github.com/TheLaughingDuck/Small_Projects/tree/main/todoist_taskmaker)
A python tool I built for automatically creating many todoist tasks of a similar structure, for example "Review lecture 1", "Review lecture 2" etc. Provide your todoist access key an environment variable in a local .env file, and then run `main.py` and follow the instructions.

## [Game of Life](https://github.com/TheLaughingDuck/Small_Projects/tree/main/Game-of-Life)
Implementations of Convways game of life. One running directly in the command line interface, and one in a tkinter window.
