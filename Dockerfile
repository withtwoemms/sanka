FROM python:3.9-slim

COPY examples/actionpack/example.py /
COPY examples/actionpack/requirements.txt /
RUN pip install -r requirements.txt
ENTRYPOINT python example.py
