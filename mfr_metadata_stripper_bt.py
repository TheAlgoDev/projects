# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 10:36:50 2024
@author: Brent Thompson

This function opens each individual mfr file and pulls the metadata values.

"""
import os
import pandas as pd


IV_metadata = [
    'filename', 'date', 'time', 'serial', 'load-voltage-(mV)',
    'reference-constant-(V/sun)', 'voltage-temperature-coefficient-(mV/C)',
    'temperature-offset-(C)', 'setpoint-initial-(mV/cell)',
    'step-size-one-(mV/cell)', 'step-size-switch-(mV/cell)',
    'step-size-two-(mV/cell)', 'setpoint-isc-voltage-(mV/cell)',
    'pulse-wait-time-(ms)', 'pulse-wait-time-voc-(ms)',
    'pulse-length-(us)', 'pulse-wait-time-voc-length-(us)']

lines_to_strip = (
    'Full IV', 'Flash Wait', 'Load', 'Reference', 'Voltage Temp',
    'Temperature Offset')


def mfr_metadata_stripper():
    """
The only input is ensuring that the directory path is correct.
The only output is a CSV file that contains all the metadata and data.
Comment out line 68 to ensure the columns are correct
    """

# Set the directory path for the function to run in
    folder = 'C:/UCF/FSEC/Data/Databases/multiflash/testmfr'
    files = []
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith(".mfr"):
                file = os.path.join(dirpath, filename)
                files.append(file)
                print(file)
    print(f'{len(files)} files found ending in .MFR')
# Create array to store what is put into data list during the for loop
    stripped_folder = []
    files_processed = 0

# Open the file path to enable parsing
    for file in files:
        try:
            text_file = open(file)
            files_processed += 1

    # Create a list to save each module's metadata
            data_list = []

    # Preform splits on basename to get date, time, model-id metadata
            basename = text_file.name.split('/')[-1]
            splitname = basename.split("-")[-1].split("_")
            date, time, serial = splitname[:3]

    # Save the previous information to be added into array
            metadata = [basename, date, time, serial]
            data_list.extend(metadata)

    # Read the contents of MFR file to extract metadata
            raw_text = text_file.readlines()

    # Strip out unnessasary information from metadata ( = and " )
            for line in raw_text:
                if line.startswith(lines_to_strip):
                    line_value = line.replace('"', '').split(' = ')[1]
                    data_list.append(line_value)
            stripped_folder.append(data_list)
            text_file.close()
            print(f'{basename} processed, {files_processed} files complete')
        except:
            continue
# Create dataframe for human readable database, save it as csv
    Sinton_IV_Metadata = pd.DataFrame(stripped_folder, columns=IV_metadata)
    file_path = 'C:/UCF/FSEC/Data/Databases/Sinton_IV_Metadata.csv'
    Sinton_IV_Metadata.to_csv(file_path, index=False, mode='w')

    return Sinton_IV_Metadata

    """
def draft_IV_ripper():


    This wont work with diffrent placements of lines in the
    mfr file


    # Load MFR files in
    files = fm.get_files('Select the MRF files to process')

    # Intilize empty list to store data from MRF list of lists
    metadata_results = []

    # Loop through and pull just the desired metadata
    for file in files:
        raw_data = sinton.import_raw_data_from_file(file)
        new_entry = raw_data[1]
        new_entry = [new_entry[q] for q in [
            254, 13, 82, 83, 84, 159, 160, 161, 162, 163, 164, 165, 166, 167]]
        metadata_results.append(new_entry)

    # Convert metadata and raw_data into a dataframe
    IV_database = pd.DataFrame(metadata_results, columns=IV_metadata)

    # Go through each row and columns, and remove the redundant indetifier
    for row in IV_database.index:
        for column in IV_database.columns:
            IV_database[column] = IV_database[column].str.split(
                ' = ')[1][1].strip('""')
   """
