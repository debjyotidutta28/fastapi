from fastapi import FastAPI
import pickle
from EHR import ehr


diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

app = FastAPI()

@app.get("/")
async def ack():
    return {"message": "working"}

@app.post("/predict")
async def is_diabetic(data: ehr):
    data = data.dict()
    Pregnancies = data['Pregnancies']
    Glucose = data['Glucose']
    BloodPressure = data['BloodPressure']        
    SkinThickness = data['SkinThickness']

    Insulin = data['Insulin']
    BMI = data['BMI']
    DiabetesPedigreeFunction = data['DiabetesPedigreeFunction']


    Age = data['Age']
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if (diab_prediction[0] == 1):
        diab_diagnosis = 'The person is diabetic'
    else:

        diab_diagnosis = 'The person is not diabetic'

    return diab_diagnosis

