# flask for web app.
from flask import Flask, request, redirect, abort, jsonify, render_template
# numpy for numerical work.
import numpy as np
from power2 import prediction

# Create a new web app.
app = Flask(__name__, static_url_path='', static_folder='staticpages')

# Add root route.
@app.route("/")
def home():
  return redirect ('power_prediction.html')
  
# Add route.
@app.route('/', methods= ['GET'])
def get_input():
    
    value_1 = request.json['input1']
    print(value_1)
    return jsonify(prediction(value_1))


  
if __name__ == "__main__":
    app.run(debug=True)