"""
Created on Wed May  8 12:10:54 2024

@author: Brent Thompson, Dylan Colvin

This module provides functions for managing the PVMCF module databases.

Key functionalities include:
* Reading database files
* Creating module IDs
* Copying module information
* Adding new entries
* Updating existing entries
* Saving database changes

The module interacts with LabVIEW to perform basic CRUD database operations
based on command-line arguments sent from LabVIEW VIs.
"""
import sys
import numpy as np
import pandas as pd
import file_management as fm
from datetime import datetime


def get_date():  # Get the current date in YYMM format
    """
    Returns the current date in YYMM format.

    Returns:
        str: The current date in YYMM format.
    """
    today = datetime.now()
    today = datetime.strftime(today, '%y%m')
    return today


def read_database(path=None):  # Open the database to be used
    """
    Reads a database file in CSV, Excel, or text format.

    Args:
        path (str, optional): The path to the database file. If None,
        prompts the user to select a file.

    Returns:
        pandas.DataFrame: The loaded database as a DataFrame.
    """
    if path is None:
        path = fm.get_files("Select the proper database to read")[0]

    if path.endswith('.txt') or path.endswith('.csv'):
        database = pd.read_csv(path, sep='\t', encoding='latin-1')
    elif path.endswith('.xlsx') or path.endswith('.xls'):
        database = pd.read_excel(path)
    else:
        print("You did not select the proper database.")

    return database


def create_module_id(database):  # Creates Module ID for use with add_entry
    """
    Creates a new module ID based on the contents of the database.

    This function generates a unique module ID with format "FYYMM-####" where:
    - F: is a fixed prefix
    - YYMM: represents the current year and month
    - ####: is a sequential number

    The function filters out control modules (VCAD, PSEL) and increments the
    sequential number based on the most recent FSEC-ID in the database.

    Args:
        database (pandas.DataFrame): Database containing module information.

    Returns:
        str: The newly generated module ID.
    """
    today = get_date()

# Selects the most recent FSEC-ID with the standard FYYMM format
    database['module-id'] = database['module-id'].astype(str)
    fsec_id_field = database[['module-id']]

    fsec_id_field = [
        entry for entry in fsec_id_field['module-id'] if (
            entry[0] == "F") and (entry[1] != "P") and (entry[1] != "9")]

    most_recent_id = sorted(fsec_id_field)[-1]

# Strip prefix and suffix for processing
    fsec_prefix = most_recent_id.split('-')[0].strip('F')
    fsec_suffix = int(most_recent_id.split('-')[1]) + 1
    fsec_suffix = (f'{fsec_suffix:04}')

# Run check to determine module id, create the id and alert user
    new_module_id = (f"F{today}-0001")
    if today == fsec_prefix:
        new_module_id = (f"F{today}-{fsec_suffix}")
        print(f'{most_recent_id} found in database, {new_module_id} created.')

    return new_module_id


def get_model_info(database, model_number):
    """
    Copies information from an existing model to a new row in the database.

    This function creates a new row based on the most recent occurrence of the
    specified model number. The new row's `module-id` is set to `new_module_id`
    (assumed to be defined in the calling scope). The `serial-number` column is
    cleared if it exists in the database.

    Args:
        database (pandas.DataFrame): Database containing module information.
        model_number (str): The model number to copy information from.

    Returns:
        pandas.DataFrame: The updated database with the new row.

    Raises:
        IndexError: If no model matching the specified model number is found.
    """
    try:
        new_row = database.loc[database['model'] == model_number]
        new_row = pd.DataFrame([new_row.iloc[-1]])
        new_row.loc[:, 'module-id'] = new_module_id

        if 'serial-number' in database:
            new_row.loc[:, 'serial-number'] = ''
        database = pd.concat([database, new_row], ignore_index=True)

    except IndexError:
        print(f'No model exists that matches {model_number}, use manual add.')
        sys.exit()

    return database


def add_serial_number(database, serial_number, new_module_id):
    """
    Adds a serial number to the specified module in the database.

    If the module ID exists, updates the serial number for that module.
    Otherwise, adds the serial number to the last entry in the database.

    Args:
        database (pandas.DataFrame): Database containing module information.
        serial_number (str): The serial number to add.
        new_module_id (str): The module ID to associate with the serial number.

    Returns:
        pandas.DataFrame: The updated database with the added serial number.
    """
    if not serial_number:
        print("No serial number entered.")
        sys.exit()
    else:
        try:
            idx = database[database['module-id'] == new_module_id].index[0]
            print('Try triggered for add serial number')

        except ValueError:
            idx = len(database) - 1
            print('Except triggered for add serial number')

        database.loc[idx, 'serial-number'] = serial_number
        print(f'{serial_number} added to {new_module_id}')

    return database


def add_new_entry(database, new_values, parameters):
    """
    Adds a new row to the database with the specified values and parameters.

    This function creates a new row at the end of the database and populates it
    with the provided values and parameters. It also adds the `new_module_id`
    to the 'module-id' column if it exists in the database.

    Args:
        database (pandas.DataFrame): Database to add the new entry to.
        new_values (list): Values to populate the new row.
        parameters (list): Column names corresponding to the new values.

    Returns:
        pandas.DataFrame: The updated database with the new row.
    """
    idx = len(database)
    database.loc[idx] = None

# Update values for new entry in database on each key
    for key, value in zip(parameters, new_values):
        database.loc[idx, key] = value.upper()

# Add branching to add to different databases
    if 'module-id' in database:
        database.loc[idx, 'module-id'] = new_module_id
    else:
        pass

    return database


def update_entry(database, new_values, parameters):
    """
    Updates an existing entry in the database with
    the specified values and parameters.

    This function finds the row with the matching `new_module_id` and
    updates the specified columns with the provided values.

    Args:
        database (pandas.DataFrame): The database to update.
        new_values (list): A list of values to update the entry with.
        parameters (list): A list of column names corresponding to the values.

    Raises:
        IndexError: If the module with `new_module_id` is not found.

    Returns:
        pandas.DataFrame: The updated database.
    """
    try:
        idx = database[database['module-id'] == new_module_id].index[0]
        # Update values for entry in database on each key
        for key, value in zip(parameters, new_values):
            database.loc[idx, key] = value.upper()

    except IndexError:
        print('Module not found in database.')
        sys.exit()

    return database


def save_database(database, file_path):
    """
    Saves database to the specified file path in both CSV and Excel formats.

    Args:
        database (pandas.DataFrame): The database to save.

    file_path (str): The base file path for saving the database. The function
        will create both a CSV and Excel file with the same base name.
    """
    ext = file_path.split('.')[-1]

    database.to_csv(file_path, sep='\t', index=False)
    database.to_excel(file_path.replace(ext, 'xlsx'), index=False)
    return print(f'{database} txt and xlsx saved at {file_path}.')


##########################
# Start of Main Program #
if __name__ == "__main__":
    print("Main program started...make sure files are closed")
    """
    Main entry point for the photovoltaic module database management script.

    This script interacts with LabVIEW to perform various operations on
    PVMCF databases.

    Args:
        sys.argv: Command-line arguments.

    """

    database_root = "E:/University of Central Florida/UCF_Photovoltaics_GRP - \
        Documents/General/FSEC_PVMCF/module_databases/"

    module_filepath = f"{database_root}module-metadata.txt"
    settings_filepath = f"{database_root}measurement-settings.txt"
    status_filepath = f"{database_root}module-status.txt"

    module_database = read_database(module_filepath)
    settings_database = read_database(settings_filepath)
    status_database = read_database(status_filepath)

    command = sys.argv[1].replace('"', '')

    new_values = sys.argv[2].replace('"', '')
    new_values = [value for value in new_values.split(' ')]

    parameters = sys.argv[3].replace('"', '')
    parameters = [parameter for parameter in parameters.split(' ')]

    new_module_id = create_module_id(module_database)

    if len(sys.argv) > 4:
        new_module_id = sys.argv[4]
        print(f'{new_module_id} loaded from Labview')

# Branch depending on sys.argv[1] from LabVIEW

    if command == 'add_new_entry':
        print("Add new entry started.")
        try:
            module_database = add_new_entry(
                module_database, new_values, parameters)

            save_database(module_database, module_filepath)
        except ValueError:
            print('Error adding new entry. Run manual addition.')
        print("Add new entry finished.")

    elif command == 'copy_module_information':
        print("Copy module information started.")
        model_number = sys.argv[2]

        module_database = get_model_info(module_database, model_number)
        settings_database = get_model_info(settings_database, model_number)

        save_database(module_database, module_filepath)
        save_database(settings_database, settings_filepath)

        print("Copy module information finished")

    elif command == 'write_measurement_settings':
        print("Write measurement setting started.")

        if not np.isin(new_module_id, settings_database['module-id']):
            settings_database = add_new_entry(settings_database,
                                              new_values=[new_module_id],
                                              parameters=['module-id'])

        settings_database = update_entry(
            settings_database, new_values, parameters)

        save_database(settings_database, settings_filepath)
        print("Write measurement settings finished")

    elif command == 'add_serial_number':
        print("Adding serial number")
        serial_number = sys.argv[2]
        print(f'{serial_number} sent from Labview to python')
        add_serial_number(module_database, serial_number, new_module_id)
        save_database(module_database, module_filepath)
        print(f'{serial_number} added')

    elif command == 'write_status_event':
        add_new_entry(status_database, new_values, parameters)
        save_database(status_database, status_filepath)

    elif command == 'create_module_id':
        new_module_id = create_module_id(module_database)
        print(f'{new_module_id} created')
    else:
        print('Something went wrong... Script did not run properly')

    print('Script finished running, check that data was added correctly')

# End of Main Program #
##########################
