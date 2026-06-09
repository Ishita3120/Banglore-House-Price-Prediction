#flask is used for backend development using python
#it is used to write a python based service
# from flask import Flask,request,jsonify
# import util
# app=Flask(__name__)

# @app.route('/hello')
# def hello():
#     return "hi"
# @app.route('/get_locations_names')
# def get_locations_names():
#     response=jsonify({
#         'locations':util.get_locations_names()

#     })
#     response.headers.add('Access-Control-Allow-Origin','*')
#     return response
# @app.route('/predict_home_price',methods=['POST'])
# def predict_home_price():
#     total_sqft=float(request.form['total_sqft'])
#     location=request.form['location']
#     bhk=int(request.form['bhk'])
#     bath=int(request.form['bath'])
#     response=jsonify({
#         'estimated_price':util.get_estimated_price(location,total_sqft,bhk,bath)
#     })
#     response.headers.add("Access-Control-Allow-Origin","*")
#     return response


# if __name__=="__main__":
#     print("Starting python flask server home price prediction")
#     util.load_saved_artifacts()
#     app.run()

# ##post mtlb hota hai aap data server ko bhej rhe ho isliye vo postman ya ajx mein hi test hoga
# ##flask server is used as a backend for a website

from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)

@app.route('/hello')
def hello():
    return "hi"

@app.route('/get_locations_names')
def get_locations_names():
    return jsonify({
        'locations': util.get_locations_names()
    })

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    return jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })

if __name__ == "__main__":
    print("Starting python flask server")
    util.load_saved_artifacts()
    app.run(debug=True)