# Use the official Python image from Docker Hub as a base
FROM python:3.9-slim

# Install the necessary python libraries on the environnement
RUN apt update && apt install -y \
    libgl1 \
    tesseract-ocr \
    poppler-utils \
    libmagic1 \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the entire project into the working directory inside the container
COPY . /app/

# Install the necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port FastAPI will run on
EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Start the FastAPI app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]