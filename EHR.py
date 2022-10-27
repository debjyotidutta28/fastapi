from pydantic import BaseModel

class ehr(BaseModel):
        Pregnancies: int
        Glucose: int
        BloodPressure: int
        SkinThickness: int
        Insulin: int
        BMI : int
        DiabetesPedigreeFunction: int

    
        Age : int
