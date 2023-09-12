# Define phony targets
.PHONY: run install lock check check-fix migration migrate-up migrate-down project-start project-stop

# Run the Python application
run:
	poetry run python -m src.bot

# Install project dependencies with development dependencies but exclude root
install:
	poetry install --with dev --no-root

# Generate a poetry.lock file to lock dependency versions
lock:
	poetry lock

# Run code analysis on the source code
check:
	black . --check \
	&& ruff check .

# Run code analysis and fix issues
check-fix:
	black .
	ruff check --fix-only --show-fixes --statistics .

# Generate a new Alembic migration script
migration:
	poetry run alembic revision --autogenerate -m "$(NAME)"

# Apply database migrations with Alembic
migrate-up:
	poetry run alembic upgrade head

# Revert the database by one step with Alembic
migrate-down:
	poetry run alembic downgrade -1

# Start the project using Docker Compose
project-start:
	docker-compose up --force-recreate $(OPTIONS)

# Stop the project using Docker Compose
project-stop:
	docker-compose down --remove-orphans $(OPTIONS)
