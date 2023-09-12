# Use a single shell for all targets
.ONESHELL:

# Install project dependencies with development dependencies but exclude root
install:
	poetry install --with dev --no-root

# Generate a poetry.lock file to lock dependency versions
lock:
	poetry lock

# Format code using Black
black:
	poetry run black src/

# Perform code analysis and fix issues using Ruff
ruff:
	poetry run ruff check src/ --fix-only --show-fixes --statistics

# Combined target to run code formatting and analysis fixes
check-fix: black ruff

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
	cd docker/ && docker compose up

# Stop the project using Docker Compose
project-stop:
	cd docker/ && docker compose down
