"""
refresh_cpus.py
Matthew Kruse
2025-05-04

Generated script to populate database
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
from customPrebuilts.models import PartsCPU

CSV_FILE_PATH = 'data/cpus.csv'

def refresh_cpu_data():
    try:
        with transaction.atomic():
            # Step 1: Delete all existing CPUs
            print("Deleting all CPU records...")
            PartsCPU.objects.all().delete()

            # Step 2: Insert data from the CSV
            print("Inserting new CPU data...")
            with open(CSV_FILE_PATH, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                cpus = []
                for row in reader:
                    cpus.append(PartsCPU(
                        name=row['name'],
                        manufacturer=row['manufacturer'],
                        series=row['series'],
                        msrp=float(row['msrp']) if row['msrp'] else None,
                        core_count=int(row['core_count']) if row['core_count'] else None,
                        core_speed=float(row['core_speed']) if row['core_speed'] else None,
                        boost_speed=float(row['boost_speed']) if row['boost_speed'] else None,
                        socket=row['socket'],
                        photo=row['photo'] if 'photo' in row else None,
                    ))
                PartsCPU.objects.bulk_create(cpus)
            print("CPU data refresh complete!")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Starting CPU data refresh...")
    refresh_cpu_data()

if __name__ == '__main__':
    main()