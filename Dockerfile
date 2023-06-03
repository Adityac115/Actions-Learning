FROM ubuntu:latest


COPY . .

RUN pip install -r requirements.txt

CMD ["python3","calculator.py"]

