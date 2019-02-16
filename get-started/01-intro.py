# Import azure ml packages


# py -m pip install azureml.core
from azureml.core import Workspace, Experiment, Run
import math, random, pickle

# the following will get an azure ML workspace instance, requires login 
# need to login to the correct azure tenant using az cli before running the next lime
ws = Workspace.from_config(r'.\get-started\config.json')

# get or create experimentexperiement from workspace 
experiment = Experiment(workspace = ws, name = "my-first-experiment")

# in this part of the code we will simulate running an experiment 
# this code extimats Pi\

#create a run object 
run = experiment.start_logging() 

pi_counter = 0 
n = 10000000 # try n number of times to estimate pi 
pi_estimate = 0

run.log("Number of iterations", n)

# estiamte pi 
for i in range(1,n):
    # Monte Carlo step to update estimate
    x = random.random()
    y = random.random()
    if x*x + y*y < 1.0:
        pi_counter += 1
    pi_estimate = 4.0*pi_counter / i
    
    # Log convergence every 10000 iterations
    if i%10000==0:
        error = math.pi-pi_estimate
        run.log("Pi estimate",pi_estimate)
        run.log("Error",error) 


# Log final results
run.log("Final estimate",pi_estimate)
run.log("Final error",math.pi-pi_estimate)
run.log("test metric", 123) # first time a metric is logged, it appears in "tracked metric" section in the portal as a single value 
run.log("test metric", 1234) # once additional value is logged against the metric, it will start showing as a line chart of logged values 


# write the "model" to a pickle file, in this example we will write the pi_estimate to pickle
# Write file containing pi value into run history
with open(r".\get-started\pi_estimate.txt","wb") as f:
    pickle.dump(str(pi_estimate),f)

# upload the pickle file (the model) to the experiment run 
run.upload_file(name="outputs/pi_estimate.txt", 
    path_or_stream = r".\get-started\pi_estimate.txt")
#upload other artefacts! 
# files that are uploaded to folders other than "outputs"  will not show in the portal when looking
# at the experiment run outputs, but they will still be uploaded to the storage account under the 
# experiment run folder 


run.upload_file(name="outputs1/config123.json", 
    path_or_stream = r".\get-started\config.json")

# you can use the run id below to locate the files in the storage account 
run.id

run.log("run id", run.id)

# now complete the run, this will calculate the run time in the portal 
# and change the run states from "running" to "completed"
run.complete()

