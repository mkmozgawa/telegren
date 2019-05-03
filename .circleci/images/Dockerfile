FROM python:3.7
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY *.py ~/telegren/
COPY *.txt ~/telegren/

WORKDIR ~/telegren/

CMD [ "python", "telegren.py" ]