import time
from matplotlib import pyplot as plt
import json
import os

class TrainingTracker():
    '''
    A class to track the training process of a model. It can store epoch data such as
    training loss, validation loss, accuracy, precision, recall, and learning rate.
    '''
    def __init__(self, metrics:list, logdir:str, filename:str=None):
        # Timekeeping for each epoch
        self.last_time_check = None

        # Determine filename for later saves
        self.file = logdir + "/" + filename + ("" if filename.endswith(".json") else ".json")
        print("\nEpoch data is saved in\n\t", filename)

        self.epoch_data = {"epoch_time": {"epoch": [], "value": []}}
        #self.epoch_data["epoch_time"] = {"epoch": [], "value": []}
    
    def start(self):
        self.last_time_check = time.time()
    
    def time_passed(self):
        '''Every time this method is called, it returns the amount of seconds since it was last called, or since start.'''
        passed_time = time.time() - self.last_time_check
        self.last_time_check = time.time()
        return passed_time

    def update(self, epoch, metric, value):
        # Start, if user forgot to start
        if self.last_time_check == None: self.start()

        # Check if key does not already exists
        if metric not in self.epoch_data.keys():
            self.epoch_data[metric] = {"epoch": [], "value": []}

        self.epoch_data[metric]["epoch"] += [epoch]
        self.epoch_data[metric]["value"] += [value]

        self.epoch_data["epoch_time"]["epoch"] += [epoch]
        self.epoch_data["epoch_time"]["value"] += [self.time_passed()]

        self.save()
    
    def save(self):
        with open(self.file, 'w') as file:
            json.dump(self.epoch_data, file)
    
    def stop(self):
        '''Optional function that checks for issues in the data, and outputs warnings.'''

        warnings = []

        # Check if epochs are all "rising" in the data.
        if True: warnings += ["Baeee"]
        

        # Check that values are numerical
        if True: warnings += ["Aee"]

        # Save warnings along with the data
        if len(warnings) >= 1: self.epoch_data["warnings"] = warnings
        self.save()


    



    # def update_deprecated(self, data: dict):
    #     # Start, if user forgot to start
    #     if self.start_time == None: self.start()

    #     for key in data.keys():
    #         metric = data[key]

    #         self.epoch_data[key]["epoch"] += metric["step"] #epoch
    #         self.epoch_data[key]["value"] += metric["value"]
        
    #     self.save()
    

    def make_key_fig(self, keys: list = None, kwargs=None, title=""):
        '''
        Make a plot of one or more keys in self.epoch_data. Can also pass keyword arguments to specify color
        for each key.

        Example kwargs structure: {"key1": {"color": "blue"}, "key2": {"color": "orange"}}
        '''
        if type(keys) != list: keys = [keys]

        fig, axs = plt.subplots(nrows=1)
        for key in keys:
            # Process the kwargs
            if kwargs != None and key in kwargs.keys():
                color = kwargs[key]["color"] if "color" in kwargs[key].keys() else None
                label = kwargs[key]["label"] if "label" in kwargs[key].keys() else None
            else:
                color = None
                label = None
            axs.plot(self.epoch_data[key]["step"], self.epoch_data[key]["value"], color=color, label=label)
        axs.legend()
        axs.set_xlabel("Epochs")
        title += "(" + self.start_time + ")"
        fig.suptitle(title, fontsize=16)
        fig.savefig(self.args.logdir + "/" + keys[0] + "_fig")#self.args.logdir+"/key_fig")
    
