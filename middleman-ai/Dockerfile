FROM python:3.11-bullseye

# RUN apk add --no-cache --virtual .build-deps gcc musl-dev cmake
# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

RUN pip install -r requirements.txt

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run the command to start the Streamlit server
CMD ["python", "-m", "streamlit", "run", "main.py"]