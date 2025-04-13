import os
import django
import csv
import sys

# Add the backend directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # Adds 'backend'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # Adds parent


# Set up the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

# Initialize Django
django.setup()

from django.db import transaction
from customPrebuilts.models import PartsMotherboard

CSV_FILE_PATH = 'data/motherboards.csv'  # Path to the CSV file

def refresh_motherboard_data():
    try:
        with transaction.atomic():  # Ensures atomicity of the operation
            # Step 1: Delete all existing motherboards
            print("Deleting all Motherboard records...")
            PartsMotherboard.objects.all().delete()

            # Step 2: Insert data from the CSV
            print("Inserting new Motherboard data...")
            with open(CSV_FILE_PATH, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                motherboards = []
                for row in reader:
                    motherboards.append(PartsMotherboard(
                        name=row['name'],
                        manufacturer=row['manufacturer'],
                        msrp=float(row['msrp']) if row['msrp'] else None,
                        nvme_slot_count=int(row['nvme_slot_count']) if row['nvme_slot_count'] else None,
                        ethernet=float(row['ethernet']) if row['ethernet'] else None,
                        photo=row['photo'] if 'photo' in row else None,
                    ))
                PartsMotherboard.objects.bulk_create(motherboards)  # Bulk insert for efficiency
            print("Motherboard data refresh complete!")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Starting Motherboard data refresh...")
    refresh_motherboard_data()

if __name__ == '__main__':
    main()
