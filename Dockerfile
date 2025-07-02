FROM python:3.10-slim

WORKDIR /

# Install pip and requirements
COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Copy handler
COPY handler.py /

# Start the container
CMD ["python", "-u", "/handler.py"]
