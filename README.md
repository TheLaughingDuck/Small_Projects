# Small_Projects
Small, cool projects that I work on from time to time. Kind of a staging area before I invest more time in a project.

## [ML Tools](https://github.com/TheLaughingDuck/Small_Projects/ml_tools)
Functions and classes that I find useful to me when working with machine learning.

* **[TrainingTracker](https://github.com/TheLaughingDuck/Small_Projects/ml_tools/training.py)**: A custom class for tracking metrics such as accuracy, loss, and time throughout model training. Usage is as simple as

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

* **[unique](https://github.com/TheLaughingDuck/Small_Projects/ml_tools/discovery.py)**: A custom function that identifies the uniques values in a pandas dataframe, and reports their frequencies. I found myself using this a lot in a recent project.

```
from ml_tools.discovery import unique

unique(df)
```