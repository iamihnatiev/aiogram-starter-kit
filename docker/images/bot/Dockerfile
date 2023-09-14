# Define the base Python image with a specific tag
FROM python:3.11-slim as python-base

# Ensure Python output is unbuffered
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    make \
    curl

# Update pip and install Poetry
RUN pip install --no-cache -U pip setuptools \
    && rm -rf /root/.cache/pip \
    && curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry binary to the PATH
ENV PATH="${PATH}:/root/.local/bin"

# Set the working directory for the application
WORKDIR /opt/bot/

# Copy only the Pyproject files initially to leverage Docker layer caching
COPY ./bot/pyproject.toml ./bot/poetry.lock /opt/bot/

# Install project dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-cache --no-ansi --no-interaction --only main \
    && poetry cache clear pypi --all

# Copy the entrypoint script to the container
COPY ./docker/images/bot/files/entrypoint.sh /opt/docker/entrypoint.sh

# Make the entrypoint script executable
RUN chmod +x /opt/docker/entrypoint.sh

# Set the entrypoint script for container initialization
ENTRYPOINT ["/opt/docker/entrypoint.sh"]

# Create a separate stage for development
FROM python-base as local

# Install development dependencies
RUN poetry install --no-root --no-cache --no-ansi --no-interaction --with dev \
    && poetry cache clear pypi --all

# Create the final production stage
FROM python-base as live

# Copy the entire application code into the container
COPY ./bot /opt/bot
