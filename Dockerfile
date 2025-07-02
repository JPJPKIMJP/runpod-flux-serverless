FROM python:3.10-slim

WORKDIR /

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy handler
COPY handler.py /

# Start the container
CMD ["python", "-u", "/handler.py"]
