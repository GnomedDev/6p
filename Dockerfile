FROM python:3.9

COPY requirements.txt .
RUN pip install uvicorn -r requirements.txt

COPY . .
CMD ["uvicorn", "main:app"]
