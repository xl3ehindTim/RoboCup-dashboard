FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install packages
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8050

# Run app.py when the container launches
CMD ["python", "app.py"]