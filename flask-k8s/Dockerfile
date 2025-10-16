# This Dockerfile creates a minimal Docker image for running a Flask application.
# It uses the lightweight Python 3.11-slim base image, sets the working directory to /app,
# copies the requirements and app files, installs dependencies, exposes port 5000,
# and sets the default command to run the Flask app with 'python app.py'.
# This setup is commonly used to containerize and deploy Python web applications.
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]
