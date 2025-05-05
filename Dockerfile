FROM python:3.10-slim

WORKDIR /model-service

COPY . /model-service

RUN apt-get update && apt-get install -y git && apt-get clean
RUN pip install --no-cache-dir -r requirements.txt

ENV MODEL_PATH=model.pkl
ENV PORT=5010

EXPOSE 5010

CMD ["python", "model_service.py"]