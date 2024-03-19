# Use the specified image as the base
FROM mcr.microsoft.com/devcontainers/base:jammy

# Install AWS CLI
RUN curl "https://d1vvhvl2y92vvt.cloudfront.net/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    sudo ./aws/install

# Install Docker in Docker
RUN apt-get update && \
    apt-get install -y docker.io

# Install Python
RUN apt-get install -y python3 python3-pip

# Any other configurations can be added here