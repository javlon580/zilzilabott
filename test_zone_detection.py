from shapefile_utils import get_zone_from_shapefile, test_zone_detection
from config import SHAPEFILE_PATH
import logging

logging.basicConfig(level=logging.INFO)

# Test with Tashkent coordinates
print("Testing zone detection for Tashkent...")
zone = test_zone_detection(SHAPEFILE_PATH, 41.2995, 69.2401)
print(f"\nFinal result: {zone}")

# Test with Samarkand
print("\n" + "="*50)
print("Testing zone detection for Samarkand...")
zone = test_zone_detection(SHAPEFILE_PATH, 39.6542, 66.9597)
print(f"\nFinal result: {zone}")