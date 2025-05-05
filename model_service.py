import os
from flask import Flask, jsonify, request
from flasgger import Swagger
import joblib
# ! TODO: Uncomment the following line to support text preprocessing
# from lib_ml.preprocessing import preprocess_text
from lib_version.version_util import VersionUtil

app = Flask(__name__)
Swagger(app)

MODEL_PATH = os.getenv("MODEL_PATH", "model.pkl")
MODEL_URL  = os.getenv("MODEL_URL", None)

# ! TODO: Uncomment the following lines to support downloading the model
# if MODEL_URL and not os.path.isfile(MODEL_PATH):
#     import requests
#     resp = requests.get(MODEL_URL)
#     resp.raise_for_status()
#     with open(MODEL_PATH, "wb") as f:
#         f.write(resp.content)
# model = joblib.load(MODEL_PATH)

model = None
SERVICE_VERSION = VersionUtil().get_version()

@app.route("/api/model", methods=["POST"])
def predict():
    """
    Sentiment Analysis Endpoint
    ---
    tags:
      - Model
    consumes:
      - application/json
    parameters:
      - in: body
        name: payload
        required: true
        schema:
          type: object
          properties:
            text:
              type: string
              description: Text to analyze for sentiment
              example: "I had a good day"
    responses:
      200:
        description: Sentiment prediction result (1 = positive, 0 = negative)
        schema:
          type: object
          properties:
            sentiment:
              type: integer
              description: Predicted sentiment label
              example: 1
    """
    # ! TODO: Uncomment and implement the following lines to support prediction
    return jsonify({"sentiment": 0})
    # data = request.get_json(force=True)
    # text = data.get("text", "")
    # features = preprocess_text(text)
    # pred = model.predict([features])[0]
    # return jsonify({"sentiment": int(pred)})

@app.route("/api/version", methods=["GET"])
def version():
    """
    Model Version Endpoint
    ---
    tags:
      - Version
    responses:
      200:
        description: Current service model version
        schema:
          type: object
          properties:
            model_version:
              type: string
              description: Semantic version of the model
              example: "v0.1.0"
    """
    return jsonify({"model_version": SERVICE_VERSION})

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5010))
    app.run(host="0.0.0.0", port=port)