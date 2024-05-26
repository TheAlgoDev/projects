# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 13:42:04 2024

@author: Brent Thompson

This script contains the nessasary loading and edits to manipulate the
files and databases that contain all module data. More of a collection of
random scripts at this point

To be done:
    Complete the status and measurement databases
    Find and import any other data on modules
    Create pipeline to ingest data from access to here
"""

import pandas as pd
import sys
import solarbase_v2 as sb


"""

logistics.rename(columns={'FSEC_ID': 'fsec-id', 'Serial_Number': 'serial-number'}, inplace=True)

logistics.rename(columns={'FSEC_ID': 'fsec-id', 'SERIAL_NUMBER': 'serial-number'}, inplace=True)

excel = excel.rename(columns={'Mod_ID': 'mod-id'})

access = access.rename(columns={'FSEC_ID': 'fsec-id'})

a = access[['fsec-id', 'Initial_Project_Affiliation', 'Current_Use', 'Responsible_Party', 'Notes']]

e = excel[['mod-id', 'Exposure_Step', 'IV_Date', 'IV_Time', 'High_EL_Date', 'High_EL_Time']]

m = module_metadata[['fsec-id', 'mod-id', 'serial-number']]

l = logistics[['fsec-id', 'DATE_YYYYMMDD', 'COMMENT']]

q = m.merge(l, how='left', left_on='fsec-id', right_on='fsec-id')

q = q.merge(a, how='left', left_on='fsec-id', right_on='fsec-id')

q = q.merge(e, how='left', left_on='mod-id', right_on='mod-id')

# For Splitting the column into two

q[['wafer-doping-polarity', 'wafer-crystallinity']] = q[
    'wafer-doping-polarity'].str.split(' ', expand=True)

status_db = complete_db[
    ["fsec-id", "Previous_ID", "Responsible_Party",
     "Initial_Project_Affiliation", "Site_ID",  "notes"
     ]]






complete_db.to_csv('master_module_database_csv.csv')


# This is subsetting from the complete_db above
module_db = complete_db[
    ["fsec-id", "make_x", "model_x", "serial-number", "pmax", "vmp", 
     "imp", "voc", "isc", "temperature-coefficient-voltage",
     "module-packaging", "interconnection-scheme", "number-parallel-strings",
     "cells-per-string", "module-arc", "connector-type", "junction-box-locations",
     "number-junction-box", "number-busbars", "cell-area", "module-area",
     "cell-technology", "wafer-doping-polarity", "encapsulant", "backsheet",
     "frame-material"
     ]]
module_db.to_json('module_db.json')

master_database.rename(columns={'Make': 'make',
                                'Model': 'model',
                                'Serial_Number': 'serial-number',
                                'Interconnect_Tech': 'interconnection-scheme',
                                'Num_Busbars': 'number-busbars',
                                'Num_Cells_Series': 'cells-per-string',
                                'Parallel_Substrings': 'number-parallel-strings',
                                'Module_Frame': 'frame-material',
                                'Module_Package': 'module-packaging',
                                'Encapsulation_Mat': 'encapsulant',
                                'Backsheet_Mat': 'backsheet',
                                'Module_ARC': 'module-arc',
                                'Module_Area_(cm2)': 'module-area',
                                # Module Active Area
                                'Connector_Type': 'connector-type',
                                'Junction_Box_Location': 'junction-box-locations',
                                'Junction_Box_Type': 'number-junction-box',
                                'Cell_Wafer_Type': 'wafer-doping-polarity',
                                'Cell_Tech': 'cell-technology',
                                'Cell_Area_(cm2)': 'cell-area',
                                'Voltage_Temperature_Coefficient_(mV/C)': 'temperature-coefficient-voltage'},
                       inplace=True)
master_database.to_json('master_database.json')

original_module_database.rename(columns={'FSEC_ID': 'fsec-id',
                                         'Make': 'make',
                                         'Model': 'model',
                                         'Serial_Number': 'serial-number',
                                         'Pmax': 'pmax',
                                         'Vmp': 'vmp',
                                         'Imp': 'imp',
                                         'Voc': 'voc',
                                         'Isc': 'isc',
                                         'EL_Exposure_High': 'EL-EXPOSURE-TIME',
                                         'Kepco_Voltage_DIV': 'DIV-KEPCO-VOLTAGE',
                                         'EMS_Voltage_DIV': 'DIV-EMS-VOLTAGE',
                                         'Notes': 'notes',
                                         'ISO': 'EL-ISO',
                                         'Aperture': 'EL-APERTURE'
                                         }, inplace=True)

# original_module_database = original_module_database.drop(columns='ID', axis=1)
original_module_database.to_json('original_module_database.json')
original_module_database.to_csv(
    'original_module_database.txt', index=False, sep='\t')

module_db = database[
    ["fsec_id",
     "make",
     "model",
     "serial_number",
     "pmax",
     "vmp",
     "imp",
     "voc",
     "isc",
     "voltage_tempco",
     "current_tempco",
     "power_tempco",
     "module_packaging",
     "interconnection_technology",
     "parallel_strings",
     "cells_per_string",
     "module_arc",
     "connector_type",
     "junction_box_location",
     "number_junction_boxes",
     "number_busbars",
     # "cell_x",
     # "cell_y",
     "cell_area",
     "cell_technology",
     "wafer_base_doping",
     "wafer_crystallinity",
     "encapsulant",
     "backsheet",
     "module_frame",]]

module_db.rename(columns={'fsec_id': 'fsec-id', 'serial_number': 'serial-number',
                          'voltage_tempco': 'temperature-coefficient-voltage',
                          'current_tempco': 'temperature-coefficient-current',
                          'power_tempco': 'temperature-coefficient-power',
                          'module_packaging': 'module-packaging',
                          'interconnection_technology': 'interconnection-scheme',
                          'parallel_strings': 'number-parallel-strings',
                          'cells_per_string': 'cells-per-string',
                          'module_arc': 'module-arc',
                          'connector_type': 'connector-type',
                          'junction_box_location': 'junction-box-locations',
                          'number_junction_boxes': 'number-junction-box',
                          'number_busbars': 'number-busbars',
                          'cell_area': 'cell-area',
                          'cell_technology': 'cell-technology',
                          'wafer_base_doping': 'wafer-doping-polarity',
                          'wafer_crystallinity': 'wafer-crystallinity',
                          'module_frame': 'frame-material'}, inplace=True)


module_db.to_json('module_db.json')
# module_db.to_csv('txt_module_db.txt', index=False, sep='\t')


measurement_db = database[
    ["fsec_id",
     "el_iso",
     "el_exposure_high",
     "el_isc_exposure_time",
     "el_aperture",
     "div_kepco_voltage",
     "div_ems_voltage",
     "div_max_voltage",]]

measurement_db.rename(columns={'fsec_id': 'module-id',
                               'el_iso': 'EL-ISO',
                               'el_aperture': 'EL-APERTURE',
                               'el_isc_exposure_time': 'EL-EXPOSURE-TIME',
                               'el_exposure_high': 'EL-EXPOSURE-HIGH',
                               'div_kepco_voltage': 'DIV-KEPCO-VOLTAGE',
                               'div_ems_voltage': 'DIV-EMS-VOLTAGE',
                               'div_max_voltage': 'DIV-MAX-VOLTAGE'}, inplace=True)

measurement_db = measurement_db.drop(columns='DIV-MAX-VOLTAGE')

measurement_db.to_json('measurement_db.json')
# measurement_db.to_csv('txt_measurements_db.txt', index=False, sep='\t')

status_db = {
    'fsec-id': '',
    'date(YYYYMMDD)': '',
    'time(HHMMSS)': '',
    'status': '',
    'exposure-step': '',
    'location': '',
    'system': '',
    'current-project-affiliation': '',
    'project-active': '',
    'responsible-party': '',
    'notes': ''
}
status_db = pd.DataFrame(columns=status_db)

status_db.to_json('status_db.json')
# status_db.to_csv('txt_status_db.txt', index=False, sep='\t')


# for sn in access database
for sn in original_module_database['serial-number']:
    # pull metadata from master excel database
    df_info = master_database[master_database['serial-number'] == sn]
    # check if df_info is empty - if so, then the module does not exist in
    # the master excel db
    if len(df_info):
        idx = module_db[module_db['serial-number'] == sn].index[0]
        # write parameters to final module_db
        module_db.loc[idx,
        'cells-per-string'] = df_info['cells-per-string'].values[0]



module_metadata = complete_db[["fsec-id", "Mod_ID", "make_y", "model_y", "nameplate-pmp", "nameplate-vmp",
                               "nameplate-imp", "nameplate-voc", "nameplate-isc", "temperature-coefficient-voltage_x",
                               "temperature-coefficient-power", "temperature-coefficient-current", "module-packaging_y", "interconnection-scheme_y",
                               "number-parallel-strings_y", "cells-per-string_y", "module-arc_y", "connector-type_y",
                               "junction-box-locations_y", "number-junction-box_y", "number-busbars_y", "cell-area_y", "module-area_y",
                               "cell-technology_y", "wafer-doping-polarity_y", "wafer-crystallinity", "encapsulant_y", "backsheet_y", "frame-material_y"]]

module_metadata_copy = module_metadata.copy()

for value in module_metadata.values:
    if module_metadata['Mod_ID'] == ["nan"]:
        module_metadata['Mod_ID'] = 'none'


module_metadata.reset_index()

sb.save_database(module_metadata)



master_database = sb.read_database()
master_database = master_database.drop_duplicates

module_database = sb.read_database()
database = sb.read_database()
database = database[0:0]

database_copy = database.copy()

for sn in master_database['Serial_Number'].unique():
    entry = master_database[master_database['Serial_Number'] == sn].iloc[-1, :]
    if sn in list(module_database['Serial_Number']):
        idx = module_database[module_database['Serial_Number'] == sn].index[0]
        database.loc[idx,
                     'temperature-coefficient-voltage'] = entry['Voltage_Temperature_Coefficient_(mV/C)']


for sn in master_database['serial-number'].unique():
    entry = master_database[master_database['serial-number'] == sn].iloc[-1, :]
    if sn in list(module_database['Serial_Number']):
        idx = module_database[module_database['Serial_Number'] == sn].index[0]
        module_database.loc[idx,
                            'temperature-coefficient-voltage'] = entry['temperature-coefficient-voltage']
    else:
        # create new entry
        idx = len(module_database)
        # module_database.loc[idx,'FSEC-ID']...
"""
