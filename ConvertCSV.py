import os
import csv

def process_opcode_files(directory, output_csv):
    # Define file name to ID mappings
    file_id_mapping = {
        "APT_18": 1,
        "WINNTI": 2,
        "TropicTrooper": 3,
        "Whitefly": 4,
        "Windshift": 5,
        "APT32": 6,
        "APTC36": 7,
        "Black_Tech": 8,
        "Darkhotel": 9,
        "DragonOK": 10,
        "DustStorm": 11,
        "Leviathan": 12,
        "LotusBlossom": 13,
        "PLATINUM": 14,
        "PoseidonGroup": 15,
        "Rancoor": 16,
        "Snowbug": 17,
        "TA459": 18,
        "Taidoor": 19,
        "TheWhiteCompany": 20,
        "Threat Group 3390": 21,
        "Thrip": 22,
        "Winnti Group": 23,
        "ZIRCONIUM": 24,
        "Threat Group 1314": 25,
        "Poesidon Group": 26,
        "FIN4": 27,
        "APT37": 28,
        "Higaisa": 29,
        "Machete": 30,
        "NEODYMIUM": 31,
        "PROMETHIUM": 32,
        "Carbank": 33,
        "Stealth Falcon": 34,
        "Equation": 35,
        "Strider": 36,
        "Kimsuky": 37,
        "Lazaras Group": 38,
        "Stolen Pencil": 39
    }
    
    # Initialize data storage
    data = []

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".opcode"):  # Check for correct file extension
            # Determine the file ID by checking if the filename starts with any prefix in file_id_mapping
            current_file_id = None
            for prefix, id_value in file_id_mapping.items():
                if filename.startswith(prefix):
                    current_file_id = id_value
                    break

            if current_file_id is None:
                print(f"Warning: No FileID mapping found for {filename}. Skipping.")
                continue  # Skip files without a predefined ID

            # Read and process the opcodes in each file
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', errors='ignore') as file:
                # Filter to keep only lines that look like opcodes
                opcodes = [line.strip() for line in file if line.strip().isalpha()]
                opcodes_combined = ",".join(opcodes)  # Combine all opcodes into a single string

            # Append the data with file ID and combined opcodes
            data.append([current_file_id, opcodes_combined])

    # Write the collected data to a CSV file
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['FileID', 'OPCodes'])  # Header
        writer.writerows(data)  # Data rows

    print(f"Data has been successfully written to {output_csv}")

# Example usage with the specified directory path
directory = r'C:\Users\Harish\Downloads\Group 16_Project 5_Submission-3\Group 16_Project 5_Submission-3\OPCODES'
output_csv = 'opcode_data.csv'
process_opcode_files(directory, output_csv)
