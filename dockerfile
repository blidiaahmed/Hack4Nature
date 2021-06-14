FROM python:3.8.6-buster

COPY model.joblib /model.joblib
COPY Hack4Nature /Hack4Nature
COPY api /api
COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

CMD uvicorn api.fast:app --host 0.0.0.0
