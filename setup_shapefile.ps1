# setup_shapefile.ps1
Write-Host "🔧 Setting up shapefile for Zilzila Bot" -ForegroundColor Green
Write-Host "========================================"

# Navigate to bot directory
Set-Location "C:\Users\abdul\OneDrive\Рабочий стол\zilzilabot python"

# Create directory if it doesn't exist
New-Item -ItemType Directory -Force -Path "DATA\U" | Out-Null

# Source paths where shapefile exists
$sourcePaths = @(
    "C:\Users\abdul\OneDrive\Рабочий стол\ObHavoBot\bin\Debug\net8.0\Data\U\Umumiy osr smr",
    "C:\Users\abdul\OneDrive\Рабочий стол\ObHavoBot\Umumiy osr smr"
)

$copied = $false

foreach ($source in $sourcePaths) {
    if (Test-Path "$source\Export_Output_9.shp") {
        Write-Host "✅ Found shapefile in: $source" -ForegroundColor Green
        
        # Copy all related files
        Write-Host "📋 Copying shapefile files..." -ForegroundColor Yellow
        Copy-Item "$source\Export_Output_9.*" -Destination "DATA\U\" -Force
        
        Write-Host "✅ Files copied successfully!" -ForegroundColor Green
        $copied = $true
        break
    }
}

if (-not $copied) {
    Write-Host "❌ Could not find shapefile in expected locations" -ForegroundColor Red
    Write-Host "Please check if the file exists and copy it manually to: DATA\U\" -ForegroundColor Yellow
}

# Verify files
Write-Host "`n📁 Files in DATA\U:" -ForegroundColor Cyan
Get-ChildItem -Path "DATA\U"

# Update config.py to use correct filename
$configPath = "config.py"
if (Test-Path $configPath) {
    $config = Get-Content $configPath -Raw
    
    # Update the SHAPEFILE_PATH line
    $newConfig = $config -replace 'SHAPEFILE_PATH = BASE_DIR / "Data" / "U" / "ExportOutput9.shp"', 
                                     'SHAPEFILE_PATH = BASE_DIR / "DATA" / "U" / "Export_Output_9.shp"'
    
    Set-Content $configPath $newConfig
    Write-Host "✅ Updated config.py with correct path" -ForegroundColor Green
}

Write-Host "`n✨ Setup complete! Run the bot with: python bot.py" -ForegroundColor Green