# Import azure ml packages


# py -m pip install azureml.core
from azureml.core import Workspace, Experiment, Run
import math, random, pickle

# the following will get an azure ML workspace instance, requires login 
# need to login to the correct azure tenant using az cli before running the next lime
ws = Workspace.from_config(r'.\get-started\config.json')