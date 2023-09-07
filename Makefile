# Run Alembic to generate a new migration script
.PHONY: migration
	source .env
	poetry run alembic revision --autogenerate -m "$(m)"

# Run Alembic to apply database migrations
.PHONY: migrate-up
	source .env
	poetry run alembic upgrade head

# Run Alembic to revert the database by one step
.PHONY: migrate-down
	source .env
	poetry run alembic downgrade -1

# Use Docker Compose to start the project
.PHONY: project-start
project-start:
	docker-compose up --force-recreate

# Use Docker Compose to stop the project
.PHONY: project-stop
project-stop:
	docker-compose down --remove-orphans
