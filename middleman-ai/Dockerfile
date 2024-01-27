FROM python:3.11-bullseye AS build
# Create the virtual environment.
RUN python -m venv /venv
ENV PATH=/venv/bin:$PATH

# Install Python dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt

FROM python:3.11-slim-bullseye
# Copy the virtual environment from the first stage.
COPY --from=build /venv /venv
ENV PATH=/venv/bin:$PATH

# Copy in the application (if it wasn't `pip install`ed into the venv)
WORKDIR /app
# Copy the application in.
COPY *.py *.json ./

# Make port 8501 available to the world outside this container
EXPOSE 8501
# Run the command to start the Streamlit server
CMD ["python", "-m", "streamlit", "run", "main.py"]

