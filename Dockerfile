FROM python:3.12-alpine
WORKDIR /app
copy requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
copy . .
CMD ["python", "main.py"]