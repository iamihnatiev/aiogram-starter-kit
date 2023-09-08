.PHONY: run
run:
	poetry run python -m src.bot

# Run Alembic to generate a new migration script
.PHONY: migration
migration:
	. .env && poetry run alembic revision --autogenerate -m "$(NAME)"

# Run Alembic to apply database migrations
.PHONY: migrate-up
migrate-up:
	. .env && poetry run alembic upgrade head

# Run Alembic to revert the database by one step
.PHONY: migrate-down
migrate-down:
	. .env && poetry run alembic downgrade -1

# Use Docker Compose to start the project
.PHONY: project-start
project-start:
	docker-compose up --force-recreate $(OPTIONS)

# Use Docker Compose to stop the project
.PHONY: project-stop
project-stop:
	docker-compose down --remove-orphans $(OPTIONS)
