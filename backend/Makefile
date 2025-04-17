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
	python3 data/refresh_gpus.py
	python3 data/refresh_cpus.py
	python3 data/refresh_motherboards.py
	python3 data/refresh_games.py
	python3 data/refresh_game_specs.py

 	

sql:
	sqlite3 db.sqlite3

