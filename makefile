run:
	docker compose up --build
clear:
	docker compose down --remove-orphans
watch:
	docker compose up --build --watch