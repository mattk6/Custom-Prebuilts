run:
	clear
	uv run python manage.py runserver

migrate:
	clear
	uv run python manage.py makemigrations
	uv run python manage.py migrate

shell:
	clear
	uv run python manage.py shell

reload:
	clear
	uv run python data/refresh_gpus.py
	uv run python data/refresh_cpus.py
	uv run python data/refresh_motherboards.py

sql:
	sqlite3 db.sqlite3
