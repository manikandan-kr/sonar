# Use an official Python runtime
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application
COPY . .

# Expose the port (change if needed)
EXPOSE 8000

# Run your Python application
CMD ["python", "main.py"]
