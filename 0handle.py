import urllib.request
import zipfile
import os

# Step 1: Download the Sysinternals Suite ZIP file
url = "https://download.sysinternals.com/files/SysinternalsSuite.zip"
download_path = "SysinternalsSuite.zip"
urllib.request.urlretrieve(url, download_path)

# Step 2: Extract the ZIP file
with zipfile.ZipFile(download_path, 'r') as zip_ref:
    zip_ref.extractall("sysinternals")

# Step 3: Locate handle.exe
handle_path = os.path.join("sysinternals", "handle.exe")

if os.path.exists(handle_path):
    print(f"handle.exe extracted to: {handle_path}")
else:
    print("handle.exe not found.")
