FROM python:3.10-slim

WORKDIR /app  # 변경점 1: working dir을 명확히 지정

# Install pip and requirements
COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt  # trigger rebuild

# Copy handler
COPY handler.py .

# Start the container
CMD ["python", "-u", "handler.py"]
