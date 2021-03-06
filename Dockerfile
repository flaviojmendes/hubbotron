FROM python:3.7.4

RUN git clone https://github.com/flaviojmendes/hubbotron.git

WORKDIR /hubbotron

RUN pip install pipenv && \
	pipenv install --system

CMD [ "python", "./main.py" ]
