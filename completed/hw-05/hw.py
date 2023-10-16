import pickle
from flask import Flask
from flask import request
from flask import jsonify

model_file = "./model2.bin"
dv_file = "./dv.bin"

# load model
with open(model_file, 'rb') as f_model:
    model = pickle.load(f_model)

# load dictvectorizer
with open(dv_file, 'rb') as f_dv:
    dv = pickle.load(f_dv)

'''
# score client:
new_client = {"job": "retired", "duration": 445, "poutcome": "success"}
X_new = dv.transform(new_client)
prediction = model.predict_proba(X_new)[0, 1]
print(f"Prediction: {prediction}")
'''

app = Flask('credit')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    credit = y_pred >= 0.5

    result = {
        'credit_probability': float(y_pred), # both these variables will fail if not cast to native python, they are numpy objects
        'credit': bool(credit)               # and will give error 500 not not serializable
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
