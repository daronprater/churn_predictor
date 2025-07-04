# Use a base image with Python
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything else
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# Build the Docker image with: docker build -t fastapi-churn-app .
# Run the Docker container with: docker run -p 8000:8000 fastapi-churn-app
# Stop the container with: docker stop <container_id>
# Remove the container with: docker rm <container_id>
# Enter into the container with: docker exec -it <container_id> bash
# To run the FastAPI app, navigate to http://localhost:8000/docs in your browser
# read file with cat predictions_log.csv
# Move file to local machine with: docker cp <container_id>:/app/predictions_log.csv .