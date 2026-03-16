import geopandas as gpd
from shapely.geometry import Point
from pathlib import Path
import logging
import pandas as pd

logger = logging.getLogger(__name__)

# Cache for shapefile to avoid reading every time
_shapefile_cache = None
_shapefile_path_cache = None

# Possible column names that might contain zone values
ZONE_COLUMNS = ['ball', 'ball_value', 'Ball_fit', 'bal_value', 'zone', 'level', 'ball_', 'ball_1']

def get_zone_from_shapefile(lat: float, lon: float, shp_path: Path) -> str:
    """
    Find which seismic zone the point belongs to using shapefile
    
    Args:
        lat: Latitude
        lon: Longitude
        shp_path: Path to shapefile
    
    Returns:
        Zone number as string if found, None otherwise
    """
    global _shapefile_cache, _shapefile_path_cache
    
    try:
        # Validate inputs
        if not isinstance(lat, (int, float)) or not isinstance(lon, (int, float)):
            logger.error(f"Invalid coordinates: lat={lat}, lon={lon}")
            return None
            
        # Load shapefile (cached)
        if _shapefile_cache is None or _shapefile_path_cache != shp_path:
            if not shp_path.exists():
                logger.error(f"Shapefile not found: {shp_path}")
                return None
            
            logger.info(f"Loading shapefile from: {shp_path}")
            try:
                _shapefile_cache = gpd.read_file(shp_path)
                _shapefile_path_cache = shp_path
                logger.info(f"✅ Shapefile loaded successfully")
                logger.info(f"   Number of features: {len(_shapefile_cache)}")
                logger.info(f"   Columns: {list(_shapefile_cache.columns)}")
                
                # Log which zone columns are available
                available_zone_cols = [col for col in ZONE_COLUMNS if col in _shapefile_cache.columns]
                if available_zone_cols:
                    logger.info(f"   Zone columns found: {available_zone_cols}")
                else:
                    logger.warning("   No standard zone columns found!")
                    
            except Exception as e:
                logger.error(f"Error reading shapefile: {e}")
                return None
        
        gdf = _shapefile_cache
        
        # Create point
        point = Point(lon, lat)
        logger.debug(f"Checking point: ({lat:.6f}, {lon:.6f})")
        
        # Check each geometry
        for idx, row in gdf.iterrows():
            geometry = row.geometry
            if geometry is None:
                continue
                
            # Check if point is in this polygon
            if geometry.contains(point) or geometry.covers(point):
                logger.debug(f"Point found in feature {idx}")
                
                # Try to find zone value in various columns
                zone = extract_zone_from_row(row)
                if zone:
                    logger.info(f"✅ Found zone {zone} for coordinates ({lat:.6f}, {lon:.6f})")
                    return zone
                else:
                    # Log available values for debugging
                    logger.debug(f"No zone value found in feature {idx}. Available values:")
                    for col in gdf.columns:
                        if col != 'geometry' and col in ZONE_COLUMNS:
                            val = row[col]
                            logger.debug(f"   {col}: {val} (type: {type(val)})")
        
        logger.info(f"No zone found for coordinates ({lat:.6f}, {lon:.6f}) - point outside all polygons or no zone data")
        return None
        
    except Exception as e:
        logger.error(f"Shapefile processing error: {str(e)}")
        import traceback
        logger.error(traceback.format_exc())
        return None

def extract_zone_from_row(row):
    """Extract zone number from a row of data by checking possible columns"""
    
    # Try each possible zone column in order of preference
    for col in ZONE_COLUMNS:
        if col in row.index:
            val = row[col]
            
            # Skip None/NaN values
            if pd.isna(val):
                continue
                
            # Convert to string and clean
            try:
                str_val = str(val).strip().replace('.0', '')
                
                # Check if it's a number between 1-9
                if str_val.isdigit() and 1 <= int(str_val) <= 9:
                    logger.debug(f"Found zone {str_val} in column '{col}'")
                    return str_val
            except:
                continue
    
    # If no standard columns work, try all columns as fallback
    for col in row.index:
        if col == 'geometry':
            continue
            
        val = row[col]
        if pd.isna(val):
            continue
            
        try:
            str_val = str(val).strip().replace('.0', '')
            if str_val.isdigit() and 1 <= int(str_val) <= 9:
                logger.debug(f"Found zone {str_val} in fallback column '{col}'")
                return str_val
        except:
            continue
    
    return None

# Optional: Function to test zone detection
def test_zone_detection(shp_path: Path, lat: float, lon: float):
    """Test function to see what zone would be detected"""
    gdf = gpd.read_file(shp_path)
    point = Point(lon, lat)
    
    for idx, row in gdf.iterrows():
        if row.geometry.contains(point):
            print(f"\n✅ Point found in feature {idx}")
            print("Available data:")
            for col in gdf.columns:
                if col != 'geometry':
                    val = row[col]
                    print(f"  {col}: {val} (type: {type(val)})")
            
            zone = extract_zone_from_row(row)
            print(f"\n🎯 Detected zone: {zone}")
            return zone
    
    print("❌ Point not found in any feature")
    return None