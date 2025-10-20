# --- PowerShell Script (Save as .ps1) ---

# --- Configuration ---
$RootFolder  = "C:\Users\ahmed\Downloads"       # ⬅️ Set the folder to scan
$OutputFolder = "C:\Dicom_P_Files"              # ⬅️ Set the destination folder
$FileCount = 0

# 1. Create the output directory if it doesn't exist
if (-not (Test-Path $OutputFolder)) {
    Write-Host "Creating output folder: $OutputFolder" -ForegroundColor Yellow
    New-Item -Path $OutputFolder -ItemType Directory | Out-Null
}

# 2. Recursively find and filter files
# -Recurse: Scan subfolders
# -Filter *.dcm: Only process DICOM files
# Where-Object: Apply the complex string logic
Get-ChildItem -Path $RootFolder -Recurse -Filter *.dcm | Where-Object {
    # -cmatch is case-sensitive, but we'll use -match (case-INsensitive) to match the Python logic.
    $_.Name -match "_P" -and $_.Name -notmatch "_O" -and $_.Name -notmatch "_F"
} | ForEach-Object {
    # 3. Copy the file to the destination
    try {
        $_ | Copy-Item -Destination $OutputFolder -ErrorAction Stop
        $FileCount++
        Write-Host "✅ Copied: $($_.Name)" -ForegroundColor Green
    }
    catch {
        Write-Host "❌ Failed to copy $($_.Name): $($_.Exception.Message)" -ForegroundColor Red
    }
}

# 4. Display the final result
Write-Host ""
Write-Host "--- Script Finished ---"
Write-Host "✅ Found and copied $FileCount matching DICOM files to $OutputFolder."