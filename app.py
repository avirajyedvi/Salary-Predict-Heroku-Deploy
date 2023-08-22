from flask import Flask, render_template,request,url_for
import pickle
import numpy as np


app = Flask(__name__)
model= pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('/index.html')

@app.route('/predict',methods=["POST"])
def predict():
    experience= float(request.form.get('experience'))
    test_score = float(request.form.get('test_score'))
    interview_score = int(request.form.get('interview_score'))
    output = model.predict(np.array([experience,test_score,interview_score]).reshape(1,3))

    return render_template('index.html',prediction_text='Employee Salary should be $ {}'.format(output))
    
    
    
"""  int_features = [int(x) for x in request.form.values()]
    all_features = [np.array(int_features)]
    prediction = model.predict(all_features)
    
    output = round(prediction[0],2)
    
    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output)) """
    

if __name__ == '__main__':
    app.run(debug=True)