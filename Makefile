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

# Start Docker containers for local development
compose-up:
	cd docker/ && docker compose -f common.yml -f local.yml up

# Stop and remove Docker containers for local development
compose-down:
	cd docker/ && docker compose -f common.yml -f local.yml down

# Start Docker containers for live environment
compose-up-live:
	cd docker/ && docker compose -f common.yml -f live.yml up

# Stop and remove Docker containers for live environment
compose-down-live:
	cd docker/ && docker compose -f common.yml -f live.yml down
