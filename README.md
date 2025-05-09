# model-service

A lightweight Flask-based REST API that wraps a pretrained sentiment analysis model. It exposes prediction and version endpoints, uses `lib-ml` for preprocessing, and is packaged as a container for easy deployment. The personal contribution can be seen from `ACTIVITY.md`.  

---

## Features

* **POST** `/api/model` — Accepts a JSON payload with a `"text"` field and returns a sentiment prediction (`0` = negative, `1` = positive).
* **GET** `/api/version` — Returns the currently deployed model/service version.
* Leverages **lib-ml** for text preprocessing.
* Configurable via environment variables (model path/URL, host/port).
* Multi-stage Docker build for small, production-ready images.
* Automatic versioning driven by Git tags (e.g. `v0.1.0`).

---

## Environment Variables

| Name         | Default     | Description                                                                                      |
| ------------ | ----------- | ------------------------------------------------------------------------------------------------ |
| `PORT`       | `5000`      | HTTP port the service listens on.                                                                |
| `MODEL_PATH` | `model.pkl` | Local path to the serialized model file.                                                         |
| `MODEL_URL`  | (unset)     | If set, the service will download the model from this URL on startup if `MODEL_PATH` is missing. |

---

## Quick Start

### 1. Build the Docker image

```bash
# From within the repo root:
docker build -t remla-model-service:v0.1.0 .
```

### 2. Run the container

```bash
docker run -d \
  -p 5010:5010 \
  -e MODEL_URL=https://your-bucket/model-v0.1.0.pkl \
  --name model-service \
  remla-model-service:v0.1.0
```

Your API will be available at `http://localhost:5010`.

---

## API Reference

### POST /api/model

Perform sentiment analysis on input text.

* **URL**

  `/api/model`

* **Method**

  `POST`

* **Headers**

  `Content-Type: application/json`

* **Request Body**

  ```json
  {
    "text": "I had a fantastic experience!"
  }
  ```

* **Response**

  ```json
  {
    "sentiment": 1
  }
  ```

* **Notes**

  * `1` indicates positive sentiment; `0` indicates negative sentiment.

---

### GET /api/version

Retrieve the current model/service version.

* **URL**

  `/api/version`

* **Method**

  `GET`

* **Response**

  ```json
  {
    "model_version": "v0.1.0"
  }
  ```

---

## Development

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run locally**

   ```bash
   export MODEL_PATH=path/to/your/model.pkl
   python app.py
   ```

3. **Browse API docs**
   If you’ve enabled Flasgger, visit `http://localhost:5010/apidocs/` to explore Swagger UI.