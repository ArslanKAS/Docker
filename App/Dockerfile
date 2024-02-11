# Define Python version: Using 'Latest' for now since I'm Lazy
FROM python:latest

# Set the Working Directory
WORKDIR /app

# Install Dependencies | Copying it separately because we don't want Docker to always install all dependencies whenever we change code
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the Scripts to the Folder
COPY . /app

# Start the Server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]