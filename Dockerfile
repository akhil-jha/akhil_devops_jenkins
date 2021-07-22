FROM python:3

ADD api_requests.py /

RUN pip install forex_python

CMD [ "python", "./api_requests.py" ]
