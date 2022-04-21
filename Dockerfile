FROM python:3
# Set application working directory
WORKDIR /
# Install requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
# Install application
COPY src/ src/
# Run application
CMD python src/app.py