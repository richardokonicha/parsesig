FROM python:3.8-slim

# Set the default directory where CMD will execute
# WORKDIR /app

# Install dependencies from requirements file
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["python", "main.py"]
