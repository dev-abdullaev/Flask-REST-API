FROM python:3.11-slim

# Set the working directory in the container
ADD . /app
WORKDIR /app

# Copy the application files and requirements
COPY ./run.py /run.py
COPY requirements.txt requirements.txt

# Install the dependencies
RUN pip install -r requirements.txt

# Run app.py when the container launches
CMD ["python", "run.py"]


