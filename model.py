from flask import Flask,render_template,request,jsonify
import pandas as pd
from sklearn.linear_model import LinearRegression

app=Flask(__name__,static_folder='static',template_folder='.')

data = {
    'Study_hour': [2,3,4,5,6,7,8,9,11,1,2,9,11,2,4,5,6,8,9,10,21,3,2,21,1,1,2],
    'marks': [20,55,16,43,70,75,60,100,90,92,12,32,67,89,13,57,90,75,34,32,12,44,21,32,43,21,54],
    'final_marks': [10,13,68,70,32,100,88,99,12,50,32,54,65,21,34,21,11,23,45,67,88,99,32,66,77,88,99]
}
df=pd.DataFrame(data)
X=df[['Study_hour', 'marks']]
y=df['final_marks']
model=LinearRegression()
model.fit(X,y)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data=request.get_json()
    hours_studied=float(data['hoursStudied'])
    previous_score=float(data['previousMarks'])
    input_features=pd.DataFrame([[hours_studied, previous_score]], columns=['Study_hour', 'marks'])
    prediction=model.predict(input_features)
    return jsonify({"predictedMarks": prediction[0]})

app.run()
