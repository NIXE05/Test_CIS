import requests
import os

# Set your MalShare API key here (using environment variable for security)
API_KEY = "6e5d81a697355b4dda2c6047597fd523aaf971fbe31f976fc46502e367faa1ba"
OUTPUT_DIRECTORY = "Script Downloads"

# Ensure the download directory exists
os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

# Function to download sample by hash
def download_sample_by_hash(file_hash):
    url = f"https://malshare.com/api.php?api_key={API_KEY}&action=getfile&hash={file_hash}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        if "ERROR:" not in response.text:
            # Save file to the specified directory without extension
            file_path = os.path.join(OUTPUT_DIRECTORY, file_hash)
            with open(file_path, "wb") as file:
                file.write(response.content)
            print(f"Sample for {file_hash} downloaded successfully.")
        else:
            print(f"Failed to download {file_hash}: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Network error downloading {file_hash}: {e}")

# Load hashes from text file
def load_hashes(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]

# Main script execution
if __name__ == "__main__":
    hashes = load_hashes("Malware Samples TXT Docs/TA459_hashes.txt")
    for file_hash in hashes:
        download_sample_by_hash(file_hash)
