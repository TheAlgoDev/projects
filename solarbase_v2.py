# -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:10:54 2024

@author: Brent Thompson

This script will be used for the functions and methods needed to interact
with LabVIEW or any other database functions. Adding new entries, displaying
information on front panel, ect...


"""

import pandas as pd
# import file_management.py as fm
import tkinter as tk
from tkinter import filedialog
from datetime import datetime


# These two lists acts as hardcoded examples to
# simulate the list coming from labview
parameters = [
    'make', 'model', 'serial-number', 'nameplate-pmp',
    'nameplate-vmp', 'nameplate-imp', 'nameplate-voc', 'nameplate-isc',
    'temperature-coefficient-voltage', 'temperature-coefficient-power',
    'temperature-coefficient-current', 'module-packaging',
    'interconnection-scheme', 'number-parallel-strings',
    'cells-per-string', 'module-arc', 'connector-type',
    'junction-box-locations', 'number-junction-box', 'number-busbars',
    'cell-area', 'module-area', 'cell-technology',
    'wafer-doping-polarity', 'wafer-crystallinity', 'encapsulant',
    'backsheet', 'frame-material']

new_values = ['toyota', 'solara', '133337', '2.11',
              '5.44', '90.1', '1.1', '3.22', '42.42', '22.1', '42.10', 'AAA',
              'Gold', '42', '84', '22', 'MC4', 'Center', '2', '4', '211',
              '22221', 'Lead', 'p-type', 'MONO', 'glass', 'tin', 'qqqqqqqqqqq']


def get_files(title='Select files.'):  # From file_management.py
    root = tk.Tk()
    files = list(filedialog.askopenfilenames(title=title))
    root.destroy()
    return files


def get_date():  # Get the current date in YYMM format
    today = datetime.now()
    today = datetime.strftime(today, '%y%m')
    return today


def read_database(path=None):  # Open the database to be used
    if path is None:
        database = get_files("Select the proper database to read")
        database = pd.read_csv(database[0], encoding='latin-1')
    return database

# FIXME condense the two serial number columns and move to [1]


def fix_database(database):  # Repairs damage done by excel
    # Load in databases from old files
    excel = pd.read_csv('excel_id_query.csv')
    access = pd.read_csv('access_id_query.csv')
    #  Merge and trim data to retain corrected serial numbers
    fixed_database = database.merge(
        access, how='left', left_on='fsec-id', right_on='fsec-id')
    fixed_database = fixed_database.drop(columns='serial-number_x')
    fixed_database.rename(
        columns={'serial-number_y': 'serial-number'}, inplace=True)
    fixed_database = fixed_database.merge(
        excel, how='left', left_on='mod-id', right_on='mod-id')
    #  Saved the database in new format
    fixed_database.to_csv('fixed_database.csv', sep=',', index=False, mode='w')
    print('somebody please find a way to stop excel from doing this')
    return None


def create_module_id(database):  # Creates Module ID for use with add_entry
    """
    This function will return a new module id based off of what is in the
    database, using the most recent FSEC-ID or making a new one.

    Filters out controls like VCAD and PSEL
    """
    # Gets the date
    today = get_date()

    # Selects the most recent FSEC-ID with the standard FYYMM format
    database['fsec-id'] = database['fsec-id'].astype(str)
    fsec_id_field = database[['fsec-id']]

    # fsec_id_field = [
    #    entry for entry in fsec_id_field["fsec-id"] if 'PCAL' not in entry]
    #  fsec_id_field = [entry for entry in fsec_id_field if 'F99' not in entry]
    # fsec_id_field = [entry for entry in fsec_id_field if 'PSEL' not in entry]
    # fsec_id_field = [entry for entry in fsec_id_field if 'VCAD' not in entry]

    fsec_id_field = [
        entry for entry in fsec_id_field["fsec-id"] if (
            entry[0] == "F") and (entry[1] != "P") and (entry[1] != "9")]

    most_recent_id = sorted(fsec_id_field)[-1]

# Strip prefix and suffix for processing
    fsec_prefix = most_recent_id.split('-')[0].strip('F')
    fsec_suffix = int(most_recent_id.split('-')[1]) + 1
    fsec_suffix = (f'{fsec_suffix:04}')

# Run check to determine module id, create the id and alert user
    if today == fsec_prefix:
        new_module_id = (f"F{today}-{fsec_suffix}")
        print(f'{most_recent_id} found in database,{new_module_id} created')
    else:
        new_module_id = (f"F{today}-0001")
        print(f'No modules found with F{today},{new_module_id} created')
    return new_module_id


def save_database(database):  # Saves the database in desired format
    database.to_csv('testing.csv', sep=',', index=False, mode='w')
    return print('Database saved as csv')


def add_new_entry(parameters, new_values):
    """
    This function automatically adds an entry to database,
    calling functions above to get_date, read_database, create_id,
    and finally save the database with changes.

    """

# Reads the database to be added to, designed for module_metadata.csv
    database = read_database()

# Create the new module ID for entry
    new_module_id = create_module_id(database)

# Initilize the next row of the database for new entry
    idx = len(database)
    database.loc[idx] = None

# Create the new entry from values passed in through CMD Prompt
    new_values.append(new_module_id)
    parameters.append('fsec-id')

# Update values for new entry in database on each key
    for key, value in zip(parameters, new_values):
        database.loc[idx, key] = value

# Save the database

    print(f'Database updated with new entry for {new_module_id}')
    save_database(database)

    return database


if __name__ == "__main__":
    add_new_entry(parameters, new_values)
