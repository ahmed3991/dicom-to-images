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

# Prepare results list
results = []

# Process each DICOM path
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
            continue

        # Extract only selected DICOM metadata
        info = {"md5": md5_hash}
        for tag in selected_tags:
            if tag == "md5":
                continue
            try:
                value = getattr(ds, tag)
                info[tag] = str(value)
            except AttributeError:
                info[tag] = None  # missing tag

        # Append metadata
        results.append(info)

    except Exception as e:
        print(f"❌ Error processing {dcm_path}: {e}")

# Save all metadata to CSV
if results:
    info_df = pd.DataFrame(results)
    info_df.to_csv(output_info_csv, index=False)
    print(f"✅ Selected DICOM metadata saved to {output_info_csv}")
else:
    print("⚠️ No new images processed.")
