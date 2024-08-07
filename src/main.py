from fastapi import FastAPI
from model import load_model, load_encoder
from pydantic import BaseModel
import pandas as pd

class Person(BaseModel):
    age: int
    job: str
    marital: str
    education: str
    balance: int
    housing: str
    duration: int
    campaign: int

app = FastAPI()


@app.get("/")
async def root():
    """
    Route to check that API is alive!
    """
    return "Model API is alive!"


@app.post("/predict")
async def predict(person: Person):
    """
    Route to make predictions!
    """
    ohe = load_encoder()
    model = load_model()

    df_person = pd.DataFrame([person.dict()])

    person_t = ohe.transform(df_person)
    pred = model.predict(person_t)[0]

    return {"prediction": str(pred)}