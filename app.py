from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from joblib import load
import pathlib
from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]

app = FastAPI(title='Heart Disease Prediction')

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

model = load(pathlib.Path('model/traffic-v1.joblib'))

class InputData(BaseModel):
    #Date:int
    CarCount: int
    BikeCount: int
    BusCount: int
    TruckCount: int
    #Total: int

class OutputData(BaseModel):
    TrafficSituation: str

@app.post('/predict', response_model=OutputData)
def predict(data: InputData):
    model_input = np.array([v for k, v in data.dict().items()]).reshape(1, -1)
    result = model.predict(model_input)

    if result>0 and result<20:
        score="low"
    
    elif result>=20 and result<30:
        score="normal"
    
    elif result>=30 and result<40:
        score="heavy"

    elif result>40:
        score="high"
    
    #{0: 'low', 1: 'medium', 2: 'high'}  # Ajusta esto según tus necesidades

    return {'TrafficSituation': score}
