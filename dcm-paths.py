import os
import pandas as pd
from tqdm import tqdm

# Root folder containing DICOM files (update this as needed)
root_folder = "/Users/ahmed/Downloads"       # Example: "C:/XWaruViewPro/ImageData"
output_csv = "input/dicom_paths.csv"   # Output CSV file

# List to store found DICOM paths
dcm_paths = []

# Recursively scan for DICOM files
for dirpath, _, filenames in tqdm(os.walk(root_folder), desc="Scanning folders"):
    for filename in filenames:
        name_lower = filename.lower()

        # Keep only .dcm files that contain '_p' but not '_o' or '_f'
        if (
            name_lower.endswith(".dcm")
            and "_p" in name_lower
            and "_o" not in name_lower
            and "_f" not in name_lower
        ):
            full_path = os.path.join(dirpath, filename)
            dcm_paths.append(full_path)

# Write collected paths to CSV
if dcm_paths:
    df = pd.DataFrame({"dcm_path": dcm_paths})
    df.to_csv(output_csv, index=False)
    print(f"✅ Found {len(dcm_paths)} DICOM files containing '_P'")
    print(f"📄 Saved paths to {output_csv}")
else:
    print("⚠️ No matching DICOM files found.")
