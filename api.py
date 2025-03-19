from flask import Flask,jsonify,request
import pickle
import numpy as np
import pandas as pd
from feature_engg import Feature_engg
import os
from dotenv import load_dotenv
load_dotenv()
app= Flask(__name__)

model=pickle.load(open('WineQualityRed_model.pkl','rb'))
ss=pickle.load(open('scaler.pkl','rb'))

@app.route('/')
def home():
    return jsonify("Wine Quality Prediction API is running!")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data=request.get_json()
        input_array=np.array(data["features"]).reshape(1, -1)
        scaled_input=ss.transform(input_array)
        prediction=model.predict(scaled_input)
        return jsonify({"prediction": prediction.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)})



@app.route('/predict_file', methods=["POST"])
def predict_note_file():
    df_test=pd.read_csv(request.files.get("file"))
    obj=Feature_engg(df_test)
    df_test=obj.feature_selection()
    if os.getenv('output_column') in df_test.columns:
        df_test=df_test.drop(os.getenv('output_column'),axis=1)
    scaled_df=ss.transform(df_test)
    prediction=model.predict(scaled_df)
    formatted_preds = [round(float(pred), 2) for pred in prediction]
    result_text = "Predicted Wine Quality: " + ", ".join(map(str, formatted_preds))
    return result_text



if __name__=="__main__":
    app.run(debug=True)  


'''fit_transform() is used when training the model. It calculates the mean and standard deviation from the training data and scales it accordingly.
transform() is used for new, unseen data. It applies the same scaling parameters learned during training.'''