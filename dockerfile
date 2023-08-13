FROM python:3.7

COPY requirements.txt .
RUN cat requirements.txt
RUN pip install --no-cache-dir -r requirements.txt || (pip freeze; echo "Installation failed"; exit 1)

COPY . /connector
WORKDIR /connector

CMD ["python", "football_data_connector.py"]
