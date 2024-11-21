import requests
import os

MALWAREBAZAAR_API_URL = "https://mb-api.abuse.ch/api/v1/"

# Set the paths directly here
hash_file = "Malware Samples TXT Docs/TA459_hashes.txt"  # Replace with the path to your hash file
download_directory = "Script Downloads/"  # Replace with your desired download directory

def query_malware_info(hash_value):
    data = {
        'query': 'get_info',
        'hash': hash_value
    }
    response = requests.post(MALWAREBAZAAR_API_URL, data=data)
    if response.status_code == 200:
        result = response.json()
        if result.get('query_status') == 'ok':
            sha256_hash = result['data'][0]['sha256_hash']
            return sha256_hash
    return None

def download_malware_sample(sha256_hash, download_directory):
    data = {
        'query': 'get_file',
        'sha256_hash': sha256_hash
    }
    response = requests.post(MALWAREBAZAAR_API_URL, data=data)
    
    if response.status_code == 200 and response.content:
        result = response.json()
        if result.get("query_status") == "file_not_found":
            print(f"No sample available for hash: {sha256_hash}")
            return

        zip_filename = os.path.join(download_directory, f"{sha256_hash}.zip")
        with open(zip_filename, 'wb') as f:
            f.write(response.content)
        print(f"Malware sample downloaded and saved as {zip_filename}")
    else:
        print(f"Failed to download sample for hash: {sha256_hash}")

def process_hash_file(file_path, download_directory):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return
    
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)
        print(f"Created download directory: {download_directory}")
    
    with open(file_path, 'r') as f:
        hashes = [line.strip() for line in f.readlines()]
    
    for hash_value in hashes:
        print(f"Processing hash: {hash_value}")
        sha256_hash = hash_value
        if len(hash_value) != 64:
            sha256_hash = query_malware_info(hash_value)
            if not sha256_hash:
                print(f"Could not find SHA-256 for hash: {hash_value}")
                continue
        
        download_malware_sample(sha256_hash, download_directory)

if __name__ == "__main__":
    process_hash_file(hash_file, download_directory)
