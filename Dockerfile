FROM apache/spark:3.5.3

USER root

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip curl

WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Add src directory to PYTHONPATH
ENV PYTHONPATH="/app/src:${PYTHONPATH}"

# Ensure SPARK_HOME is set
ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin