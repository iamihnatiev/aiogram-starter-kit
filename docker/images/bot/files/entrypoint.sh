#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -o errexit

# Prevent errors in pipelines from being masked
set -o pipefail

# Treat unset variables as an error
set -o nounset

python << END
import os
import sys
import time

import asyncpg


# Maximum time to wait for PostgreSQL (in seconds)
timeout=60

# Record the start time
start = time.time()

while True:
    try:
        # Retrieve PostgreSQL connection details from environment variables
        db_user = os.environ.get('POSTGRES_USER')
        db_password = os.environ.get('POSTGRES_PASSWORD')
        db_host = os.environ.get('POSTGRES_HOST')
        db_port = os.environ.get('POSTGRES_PORT')
        db_name = os.environ.get('POSTGRES_DB')

        # Construct the connection string using environment variables
        conn_str = f"postgres://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

        # Attempt to connect to the PostgreSQL database
        conn = asyncpg.connect(conn_str)
    except asyncpg.PostgresError as error:
        sys.stderr.write("Waiting for the PostgreSQL database to become available. This may take a moment...\n")

        # Check if it's taking longer than expected
        if time.time() - start > timeout:
            sys.stderr.write(
              f"Timed out waiting for PostgreSQL to become available after {timeout} seconds. Error details: '{error}'\n"
            )
    else:
        # Close the connection and break out of the loop if successful
        conn.close()
        break
    # Wait for 1 second before retrying
    time.sleep(1)
END

# Indicate that PostgreSQL is now available
>&2 echo 'PostgreSQL is now available.'

# Execute the provided command (if any)
exec "$@"
