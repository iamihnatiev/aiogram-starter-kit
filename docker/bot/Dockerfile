# Define the base Python image with a specific tag
FROM python:3.11-slim as python-base

# Set environment variables for Poetry
ENV POETRY_VERSION=1.6.1 \
    POETRY_HOME=/opt/poetry \
    POETRY_VENV=/opt/poetry-venv

# Set the location for Poetry's cache
ENV POETRY_CACHE_DIR=/opt/.cache

# Create a stage for Poetry installation
FROM python-base as poetry-base

# Install Poetry in a virtual environment dedicated to it
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

# Create a new stage for the application
FROM python-base as app

# Copy the Poetry virtual environment from the poetry-base stage
COPY --from=poetry-base ${POETRY_VENV} ${POETRY_VENV}

# Add Poetry to the PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"

# Set the working directory for the application
WORKDIR /app

# Copy only the Pyproject files initially to leverage Docker layer caching
COPY poetry.lock pyproject.toml /app/

# Validate the project's configuration with Poetry
RUN poetry check

# Install project dependencies without creating a virtualenv (no-root option)
RUN poetry install --no-interaction --no-cache --no-root

# Copy the entire application code into the container
COPY . /app/

# Define the command to run the application
CMD ["poetry", "run", "python", "-m", "src.bot"]
