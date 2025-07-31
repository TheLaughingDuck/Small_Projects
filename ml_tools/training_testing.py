#%%
from ml_tools.training import TrainingTracker
import time

T = TrainingTracker(["loss", "accuracy"], logdir=".", filename="data.json")



for i in range(10):
    T.update(i, "loss", 0.2)
    time.sleep(0.1)


T.update(1, "accuracy", 2)
T.update(1, "accuracy", "hej")
T.update(1, "bugbear", "hej")
T.update("d", "accuracy", "hej")

T.stop()
# %%
