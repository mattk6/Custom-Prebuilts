"""
refresh_gpus.py
Matthew Kruse
2025-05-04

 generated scripts to populate database
"""



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
from customPrebuilts.models import PartsGPU

CSV_FILE_PATH = 'data/gpus.csv'

def refresh_gpu_data():
    try:
        with transaction.atomic():  # Ensures atomicity of the operation
            # Step 1: Delete all existing GPUs
            print("Deleting all GPU records...")
            PartsGPU.objects.all().delete()

            # Step 2: Insert data from the CSV
            print("Inserting new GPU data...")
            with open(CSV_FILE_PATH, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                gpus = []
                for row in reader:
                    print(f"{row}")
                    gpus.append(PartsGPU(
                        id=row['id'],
                        name=row['name'],
                        manufacturer=row['manufacturer'],
                        msrp=row['msrp'] if row['msrp'] else None,
                        photo=row['photo'] if 'photo' in row else None,
                        fps_1080p_medium=row['fps_1080p_medium'] if row['fps_1080p_medium'] else None,
                        fps_1080p_ultra=row['fps_1080p_ultra'] if row['fps_1080p_ultra'] else None,
                        fps_1440p_ultra=row['fps_1440p_ultra'] if row['fps_1440p_ultra'] else None,
                        fps_4k_ultra=row['fps_4k_ultra'] if row['fps_4k_ultra'] else None,
                        gpu_chip_model=row['gpu_chip_model'],
                        cuda_cores=row['cuda_cores'],
                        boost_clock=float(row['boost_clock']),
                        memory=row['memory'],
                        memory_bandwidth=float(row['memory_bandwidth']),
                        power_consumption=row['power_consumption'],
                    ))
                PartsGPU.objects.bulk_create(gpus)  # Bulk insert for efficiency
            print("GPU data refresh complete!")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Starting GPU data refresh...")
    refresh_gpu_data()

if __name__ == '__main__':
    main()