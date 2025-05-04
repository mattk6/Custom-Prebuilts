"""
refresh_game_specs.py
Matthew Kruse
2025-05-04
 generated script to populate database

"""


import os
import django
import csv
import sys

# Add the backend directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

django.setup()

from django.db import transaction
from customPrebuilts.models import Game, GameSpec

CSV_FILE_PATH = 'data/game_specs.csv'

def refresh_game_spec_data():
    try:
        with transaction.atomic():
            # Step 1: Delete all existing GameSpec records
            print("Deleting all GameSpec records...")
            GameSpec.objects.all().delete()

            # Step 2: Insert data from the CSV
            print("Inserting new GameSpec data...")
            with open(CSV_FILE_PATH, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)  # Use CSV header for field mapping
                game_specs = []

                for row in reader:
                    try:
                        print(f"Processing row: {row}")

                        # Find the corresponding Game by steam_store_id
                        game = Game.objects.get(steam_store_id=int(row['steam_store_id']))

                        # Handle blank or placeholder data
                        fps = int(row['fps']) if row['fps'] and row['fps'] != '--' else None
                        resolution = row['resolution'] if row['resolution'] and row['resolution'] != '--' else None
                        preset = row['preset'] if row['preset'] and row['preset'] != '--' else None

                        # Create and add the GameSpec object
                        game_specs.append(GameSpec(
                            game=game,
                            spec=int(row['spec']),
                            geforce_card_id=row['geforce'],
                            fps=fps,
                            resolution=resolution,
                            preset=preset
                        ))
                    except Game.DoesNotExist:
                        print(f"Skipping row due to missing Game with steam_store_id={row['steam_store_id']}")
                    except ValueError as e:
                        print(f"Skipping row due to ValueError: {e}")

                # Bulk insert GameSpec records for efficiency
                GameSpec.objects.bulk_create(game_specs)
            print("GameSpec data refresh complete!")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Starting GameSpec data refresh...")
    refresh_game_spec_data()

if __name__ == '__main__':
    main()