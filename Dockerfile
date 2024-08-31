FROM python:3.10

WORKDIR /app

# Copy source code
COPY src/ /app/src/
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Run the Flask app
CMD ["python", "src/app.py"]
