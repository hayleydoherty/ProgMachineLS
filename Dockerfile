FROM python:3.7.4 

WORKDIR \users\hayle\documents

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=power.py

CMD flask run --host=0.0.0.0