FROM ubuntu:latest


COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3","calculator.py"]

