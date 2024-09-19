FROM python:3.12.5
WORKDIR /model
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "model.py"]

