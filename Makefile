# Use a single shell for all targets
.ONESHELL:

# Start the project using Docker Compose
project-start:
	cd docker/ && docker compose up

# Stop the project using Docker Compose
project-stop:
	cd docker/ && docker compose down
