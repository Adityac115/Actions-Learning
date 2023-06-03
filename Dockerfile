FROM python:3.10-slim-buster


COPY . .

RUN  pip install --no-cache-dir -r requirements.txt

CMD ["python3","calculator.py"]

