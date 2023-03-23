FROM python:3.8-slim-buster

WORKDIR /app

COPY scripts/* .

RUN pip3 install requests

RUN touch last_pr_time_file.txt

CMD [ "python3", "webhook.py"]