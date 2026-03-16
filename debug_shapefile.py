import geopandas as gpd
import pandas as pd
from pathlib import Path
import sys
import os

print("=" * 50)
print("SHAPEFILE DEBUGGING TOOL (FIXED PATH)")
print("=" * 50)

# Correct path based on your files
shp_path = Path("DATA/U/Export_Output_9.shp")
print(f"\n1. Checking shapefile at: {shp_path}")
print(f"   Absolute path: {shp_path.absolute()}")

# Check if file exists
if not shp_path.exists():
    print(f"   ❌ ERROR: Shapefile NOT found!")
    print(f"   Please check if the file exists in this location")
    
    # Let's search for any .shp files to help
    print(f"\n🔍 Searching for shapefiles in current directory...")
    for shp_file in Path(".").rglob("*.shp"):
        print(f"   Found: {shp_file}")
    sys.exit(1)
else:
    print(f"   ✅ Shapefile found")
    
    # Check file size
    size = shp_path.stat().st_size
    print(f"   📊 File size: {size:,} bytes ({size/1024:.2f} KB)")

# Check for required accompanying files
print(f"\n2. Checking accompanying files:")
required_extensions = ['.shx', '.dbf', '.prj']
for ext in required_extensions:
    file_path = shp_path.with_suffix(ext)
    if file_path.exists():
        size = file_path.stat().st_size
        print(f"   ✅ {ext}: found ({size:,} bytes)")
    else:
        print(f"   ⚠️  {ext}: MISSING - This may cause issues!")

# Try to read the shapefile
print(f"\n3. Attempting to read shapefile with geopandas...")
try:
    gdf = gpd.read_file(shp_path)
    print(f"   ✅ Successfully read shapefile!")
    print(f"   📊 Number of features: {len(gdf)}")
    print(f"   📊 Columns: {list(gdf.columns)}")
    print(f"   📊 Coordinate system: {gdf.crs}")
    
    # Show first few rows of data
    print(f"\n4. Sample data (first 3 rows):")
    for idx, row in gdf.head(3).iterrows():
        print(f"   Row {idx}:")
        for col in gdf.columns:
            if col != 'geometry':
                val = row[col]
                print(f"     {col}: {val} (type: {type(val)})")
    
    # Check geometry types
    print(f"\n5. Geometry types:")
    geom_types = gdf.geometry.geom_type.value_counts()
    for geom_type, count in geom_types.items():
        print(f"   {geom_type}: {count}")
    
    # Look for zone values (1-9)
    print(f"\n6. Looking for zone values (1-9):")
    found_zones = set()
    zone_columns = []
    
    for col in gdf.columns:
        if col != 'geometry':
            # Try to convert to string and look for numbers 1-9
            unique_vals = gdf[col].astype(str).unique()
            for val in unique_vals:
                if pd.isna(val) or val == 'None' or val == 'nan':
                    continue
                clean_val = str(val).strip().replace('.0', '')
                if clean_val.isdigit() and 1 <= int(clean_val) <= 9:
                    found_zones.add(clean_val)
                    if col not in zone_columns:
                        zone_columns.append(col)
                    print(f"   ✅ Found zone {clean_val} in column '{col}'")
    
    if not found_zones:
        print(f"   ⚠️  No zone values 1-9 found in any column!")
        print(f"   Please check what columns contain zone information")
    else:
        print(f"\n   📊 Found zones: {sorted(list(found_zones))}")
        print(f"   📊 Zone columns: {zone_columns}")
    
    # Test with sample coordinates for Uzbekistan
    print(f"\n7. Testing with sample coordinates:")
    
    # Sample coordinates for major Uzbek cities
    test_points = [
        ("Tashkent", 41.2995, 69.2401),
        ("Samarkand", 39.6542, 66.9597),
        ("Bukhara", 39.7744, 64.4286),
        ("Fergana", 40.3735, 71.7978),
        ("Nukus", 42.4619, 59.6167),
    ]
    
    from shapely.geometry import Point
    
    for city, lat, lon in test_points:
        point = Point(lon, lat)
        
        found = False
        zone_value = None
        for idx, row in gdf.iterrows():
            if row.geometry.contains(point):
                print(f"   ✅ {city} ({lat:.4f}, {lon:.4f}): FOUND")
                # Print zone values
                for col in gdf.columns:
                    if col != 'geometry':
                        val = row[col]
                        str_val = str(val).strip().replace('.0', '')
                        if str_val.isdigit() and 1 <= int(str_val) <= 9:
                            print(f"      Zone: {str_val} (from column '{col}')")
                            zone_value = str_val
                found = True
                break
        
        if not found:
            print(f"   ❌ {city} ({lat:.4f}, {lon:.4f}): NOT FOUND")
    
except Exception as e:
    print(f"   ❌ ERROR reading shapefile: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 50)
print("\n🔧 Next steps:")
print("1. Update config.py with the correct path:")
print("   SHAPEFILE_PATH = BASE_DIR / 'DATA' / 'U' / 'Export_Output_9.shp'")
print("2. If zone values are found, the bot should work!")
print("3. If no zone values found, we need to identify which column contains the zone numbers")