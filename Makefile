# Use a single shell for all targets
.ONESHELL:

_compose_local = cd docker/ && docker compose --env-file ../bot/.env

# Start an interactive Bash shell
shell:
	@$(_compose_local) run --rm bot bash

# Run project-specific checks
check:
	@$(_compose_local) run --rm bot make check

# Automatically fix code issues and perform checks
format:
	@$(_compose_local) run --rm bot make check-fix

# Generate or update project dependencies lock file
lock:
	@$(_compose_local) run --rm bot make lock

# Start Docker containers for local development
compose-up:
	@$(_compose_local) -f common.yml -f local.yml up -d

# Stop and remove Docker containers for local development
compose-down:
	@$(_compose_local) -f common.yml -f local.yml down

# Start Docker containers for live environment
compose-up-live:
	@$(_compose_local) -f common.yml -f live.yml up -d

# Stop and remove Docker containers for live environment
compose-down-live:
	@$(_compose_local) -f common.yml -f live.yml down

compose-config:
	$(_compose_local) -f common.yml -f local.yml config
