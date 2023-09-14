# Use a single shell for all targets
.ONESHELL:

# Start an interactive Bash shell
bot-bash:
	cd docker/ && docker compose run --rm bot bash

# Run project-specific checks
bot-check:
	cd docker/ && docker compose run --rm bot make check

# Automatically fix code issues and perform checks
bot-check-fix:
	cd docker/ && docker compose run --rm bot make check-fix

# Generate or update project dependencies lock file
bot-lock:
	cd docker/ && docker compose run --rm bot make lock

# Start the project
project-start:
	cd docker/ && docker compose up

# Stop the project
project-stop:
	cd docker/ && docker compose down

# Build the project
project-build:
	cd docker/ && docker compose build
