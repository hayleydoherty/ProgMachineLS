# ProgMachineLS
Project for the Machine Learning and Statistics module

The aim of this project is to create a web service that makes predictions of wind turbine power based on wind speed values.

The jupyter notebook contains the method used to generate the model and an explanation of what the code does.

The power.py script contains the Flask app that connects a server and hosts a html page through which wind speed values can be input. The power2.py script file contains the code from the jupyter notebook that creates a model using keras that can predict power output from a given wind speed value. 
I was unable to figure out how to get the value from the html input into the function to predict the expected power output so as a whole the web service doesn't do what was specified however I tried to get the separate pieces of the project (the keras model, the html, the flask app) coded as best as I could. 

The Power_prediction.html page contains a form made up of input box and button into which the wind speed value can be entered and an output box in which the predicted power output should be displayed.

The dockerfile contains everything needed to create a container from which the flask app can be run. 