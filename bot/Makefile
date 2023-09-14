# Use a single shell for all targets
.ONESHELL:

# Install project dependencies with development dependencies but exclude root
install:
	poetry install --with dev --no-root

# Generate a poetry.lock file to lock dependency versions
lock:
	poetry lock

# Check code formatting and perform project-specific checks
check:
	black . --check \
	&& ruff check . \

# Automatically fix code formatting and apply project-specific fixes
check-fix:
	black .
	ruff check . --fix-only --show-fixes --statistics

# Generate a new Alembic migration script
migration:
	python alembic revision --autogenerate -m "$(NAME)"

# Apply database migrations with Alembic
migrate-up:
	python alembic upgrade head

# Revert the database by one step with Alembic
migrate-down:
	python run alembic downgrade -1
