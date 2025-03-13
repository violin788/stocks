import edgar
import os

# Define the CIK for General Mills (GIS)
cik = '0000040704'  # CIK for General Mills (GIS)

# Create a directory to store the downloaded filings
output_dir = f"filings_{cik}"
os.makedirs(output_dir, exist_ok=True)

# Download filings of type '8-K' for General Mills
# The filings will be saved in the output directory
edgar.download(cik=cik, filing_type="8-K", output_dir=output_dir)

# Print out the list of downloaded 8-K filings
for file_name in os.listdir(output_dir):
    if file_name.endswith('.xml'):  # Filter for XML filings (SEC filing format)
        print(f"Downloaded filing: {file_name}")
