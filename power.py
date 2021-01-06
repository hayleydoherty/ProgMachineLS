# flask for web app.
from flask import Flask, url_for, request, redirect, abort, jsonify, render_template
# numpy for numerical work.
import numpy as np


# Create a new web app.
app = Flask(__name__, static_url_path='', static_folder='staticpages')

# Add root route.
@app.route("/")
def home():
  return redirect ('power_prediction.html')
  
# Add route.
@app.route('/', methods= ['POST', 'GET'])
def get_input():
    
    value_1 = request.form['input1']
    print(value_1)
    return value_1


'''# Add uniform route.
@app.route('/api/uniform')
def uniform():
  return {"value": np.random.uniform()}

# Add normal route.
@app.route('/api/normal')
def normal():
  return {"value": np.random.normal()}'''
  
  
if __name__ == "__main__":
    app.run(debug=True)