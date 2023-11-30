# Utilise une image Python 3.11 de base.
FROM python:3.11

COPY src/ /src
COPY /requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /src

CMD [ "python", "main.py"]