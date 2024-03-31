import subprocess
import sys
from flask import Flask, jsonify, request
from pydantic import BaseModel, ValidationError, conlist
from typing import List, Optional
import pandas as pd
from model import recommend, output_recommended_recipes

dataset = pd.read_csv('dataset.csv', compression='gzip')

app = Flask(__name__)

class Params(BaseModel):
    n_neighbors: int = 5
    return_distance: bool = False

class PredictionIn(BaseModel):
    nutrition_input: conlist(float, min_items=9, max_items=9)
    ingredients: List[str] = []
    params: Optional[Params]

class Recipe(BaseModel):
    Name: str
    CookTime: str
    PrepTime: str
    TotalTime: str
    RecipeIngredientParts: List[str]
    Calories: float
    FatContent: float
    SaturatedFatContent: float
    CholesterolContent: float
    SodiumContent: float
    CarbohydrateContent: float
    FiberContent: float
    SugarContent: float
    ProteinContent: float
    RecipeInstructions: List[str]

class PredictionOut(BaseModel):
    output: Optional[List[Recipe]] = None

@app.route("/", methods=["GET"])
def home():
    return jsonify({"health_check": "OK"})

@app.route("/predict/", methods=["POST"])
def update_item():
    try:
        # Parse the JSON data into a Pydantic model
        prediction_input = PredictionIn.parse_raw(request.data)
        recommendation_dataframe = recommend(dataset, prediction_input.nutrition_input, prediction_input.ingredients, prediction_input.params.dict())
        output = output_recommended_recipes(recommendation_dataframe)
        if output is None:
            return jsonify({"output": None})
        else:
            # Serialize the output using Pydantic model
            return jsonify(PredictionOut(output=output).dict())
    except ValidationError as e:
        # If the JSON data doesn't match the Pydantic model, return a 400 Bad Request response
        return jsonify({'error': str(e)}), 400
    
@app.route('/streamlit')
def streamlit_app_hello():
    streamlit_app_path = './Streamlit_Frontend/Hello.py'
    subprocess.Popen([f"{sys.executable}", "-m", "streamlit", "run", streamlit_app_path])
    return "Streamlit app is running. Please check the terminal for the URL."


if __name__ == '__main__':
    app.run(debug=True)
