.PHONY: project-start
project-start:
	docker-compose up --force-recreate

.PHONY: project-stop
project-stop:
	docker-compose down --remove-orphans
