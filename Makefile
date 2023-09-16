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
compose-up:
	cd docker/ && docker compose up

# Start the project with specific profiles
compose-up-profiles:
	cd docker/ && docker compose --profile debug up

# Stop the project
compose-down:
	cd docker/ && docker compose down

# Stop the project with specific profiles
compose-down-profiles:
	cd docker/ && docker compose --profile debug down

# Build the project
compose-build:
	cd docker/ && docker compose build
