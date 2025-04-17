import os
import django
import csv
import sys

# Add the backend directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # Adds 'backend'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # Adds parent

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

django.setup()

from django.db import transaction
from customPrebuilts.models import Game

CSV_FILE_PATH = 'data/games.csv'

def refresh_game_data():
    try:
        with transaction.atomic():
            # Step 1: Delete all existing Games
            print("Deleting all Game records...")
            Game.objects.all().delete()

            # Step 2: Insert data from the CSV
            print("Inserting new Game data...")
            with open(CSV_FILE_PATH, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                print("CSV Headers:", reader.fieldnames)  # Log headers to debug mismatches

                reader = csv.DictReader(csvfile, fieldnames=["steam_store_id", "name"])
                games = []
                for row in reader:
                    try:
                        print("Processing row:", row)

                        row = {key.strip(): value.strip() for key, value in row.items()}

                        steam_store_id = int(row['steam_store_id'])
                        games.append(Game(
                            steam_store_id=steam_store_id,
                            name=row['name'],
                        ))
                    except ValueError:
                        print(f"Skipping invalid row: {row}")
                Game.objects.bulk_create(games)
            print("Game data refresh complete!")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Starting Game data refresh...")
    refresh_game_data()

if __name__ == '__main__':
    main()
 