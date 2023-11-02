migrate:
	docker exec inventory_backend python manage.py migrate

migrations:
	docker exec inventory_backend python manage.py makemigrations

start:
	docker compose up --build

test:
	docker exec inventory_backend python manage.py test
