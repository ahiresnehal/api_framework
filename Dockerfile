FROM python:3.8

WORKDIR /home/snehal/PycharmProjects

ADD . api_framework

RUN pip install requests

RUN pip install pytest

CMD ['pytest', 'test_api.py']