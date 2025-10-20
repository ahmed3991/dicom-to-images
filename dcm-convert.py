import os
import hashlib
import pandas as pd
import pydicom
from pydicom.pixel_data_handlers.util import apply_voi_lut
import numpy as np
from PIL import Image
from tqdm import tqdm

# Paths
input_csv = "input/dicom_paths.csv"              # Input CSV file with a 'dcm_path' column
output_folder = "output/extracted_images"        # Folder for extracted PNGs
output_info_csv = "output/dicom_info.csv"        # Output CSV file for metadata

# Create output folder if not exists
os.makedirs(output_folder, exist_ok=True)

# Read CSV
df = pd.read_csv(input_csv)

# DICOM attributes to extract
selected_tags = [
    "md5",
    "StudyInstanceUID",
    "Modality",
    "ImageType",
    "BodyPartExamined",
    "ViewPosition",
    "PresentationIntentType",
    "PhotometricInterpretation",
    "WindowCenter",
    "WindowWidth",
    "KVP",
    "ExposureTime",
    "XRayTubeCurrent",
    "Exposure",
    "ImagerPixelSpacing",
    "Grid",
    "ExposureIndex",
    "DeviationIndex",
    "RescaleIntercept",
    "RescaleSlope",
    "RescaleType",
    "Manufacturer",
    "ManufacturerModelName",
    "DetectorType",
    "Sensitivity",
    "SoftwareVersions",
    "Rows",
    "Columns",
    "SamplesPerPixel",
    "BitsAllocated",
    "BitsStored",
    "HighBit",
    "PixelRepresentation",
    "PixelIntensityRelationship",
    "PixelIntensityRelationshipSign",
]

# ----------------------------------------------------------------------
# 1. Initialize the output CSV with headers
# This ensures the file exists and has the correct columns.
# It uses a temporary DataFrame to get the columns.
print(f"Initializing {output_info_csv}...")
initial_df = pd.DataFrame(columns=selected_tags)
# Use 'w' mode (write) and 'header=True' for the first time
initial_df.to_csv(output_info_csv, index=False, mode='w', header=True)
# ----------------------------------------------------------------------

# Process each DICOM path
# No need for the 'results' list anymore, we save directly inside the loop.
for _, row in tqdm(df.iterrows(), total=len(df), desc="Processing DICOMs"):
    dcm_path = row["dcm_path"]

    try:
        # Load DICOM file
        ds = pydicom.dcmread(dcm_path, force=True)

        # Apply VOI LUT if available
        image = apply_voi_lut(ds.pixel_array, ds)
        if getattr(ds, "PhotometricInterpretation", "") == "MONOCHROME1":
            image = np.amax(image) - image
        image = image - np.min(image)
        image = (image / np.max(image) * 255).astype(np.uint8)

        # Convert to PIL Image
        im = Image.fromarray(image)

        # Compute MD5 hash of raw pixel data
        md5_hash = hashlib.md5(image.tobytes()).hexdigest()
        output_path = os.path.join(output_folder, f"{md5_hash}.png")

        # Attempt to save without overwriting
        try:
            with open(output_path, "xb") as f:  # exclusive creation
                im.save(f, format="PNG")
        except FileExistsError:
            # Skip both image and metadata writing
            continue # Go to the next DICOM file

        # Extract only selected DICOM metadata
        info = {"md5": md5_hash}
        for tag in selected_tags:
            if tag == "md5":
                continue
            try:
                # Use .get(tag, None) on ds for robustness if available, 
                # but since ds is a dataset object, getattr is correct.
                value = getattr(ds, tag)
                info[tag] = str(value)
            except AttributeError:
                info[tag] = None  # missing tag

        # --------------------------------------------------------------
        # 2. Convert the single record to a DataFrame
        info_df = pd.DataFrame([info], columns=selected_tags)

        # 3. Append the record to the output CSV
        # 'mode="a"' for append, 'header=False' so it doesn't write headers again
        info_df.to_csv(output_info_csv, index=False, mode='a', header=False)
        # --------------------------------------------------------------

    except Exception as e:
        print(f"❌ Error processing {dcm_path}: {e}")

print(f"\n✅ Processing complete. Metadata appended line-by-line to {output_info_csv}")