FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["flask", "run", "--host", "0.0.0.0"]