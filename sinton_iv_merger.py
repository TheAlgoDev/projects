# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 09:37:25 2024

@author: Brent Thompson
"""

import database_manipulation as dm
import pandas as pd
import sqlite3 

"""
Final sinton database is the total database, containing all data

Current sinton database is the SQL file output by sinton
"""

sinton_database_filepath = 'E:/University of Central Florida/UCF_Photovoltaics_GRP - Documents/General/FSEC_PVMCF/module_databases/sinton-iv.csv'

# Load merged database
sinton_final = dm.read_database('E:/University of Central Florida/UCF_Photovoltaics_GRP - Documents/General/FSEC_PVMCF/module_databases/draft_final_sinton_iv.xlsx')

# Load the sql database by connecting to sqlite
connect = sqlite3.connect('C:/SintonInstruments/Database/MultiFlash_Database.s3db')

# Run query to collect all data in table, create a dataframe with it
sinton_current = pd.read_sql_query('SELECT * FROM Results', connect)

# Find last entry in merged database that matches current database entry
last_entry = pd.DataFrame(sinton_final.iloc[-1]).T

# Use last id to grab everything after last ID from current sinton
last_id = last_entry['ID'].iloc[0]
new_data = sinton_current[sinton_current['ID'] > last_id]

# Concat the two together

updated_database = pd.concat([sinton_final, new_data])

# Save the database

dm.save_database(updated_database, sinton_database_filepath)


"""
#  Open up each database as a dataframe
sinton_2015_2016 = dm.read_database()

sinton_2017_2019 = dm.read_database()

sinton_2019_2023 = dm.read_database()

sinton_2023_2024 = dm.read_database()


# Get list of column names to associate
a = list(sinton_2015_2016.columns)

b = list(sinton_2017_2019.columns)

c = list(sinton_2019_2023.columns)

d = list(sinton_2023_2024.columns)

# Merge each database to each other
q = pd.concat([sinton_2023_2024, sinton_2019_2023])

q = pd.concat([q, sinton_2017_2019])

q = pd.concat([q, sinton_2015_2016])

# Correct timestamp format
sinton_2015_2016['TestDate'] = sinton_2015_2016['TestDate'].astype(
    str) + " " + sinton_2015_2016['TestTime'].astype(str)


q.drop(columns={'Capacitance_Error_(percent)',
                'Software Version',
                'EL Pulse Current Delivered (Coulombs)',
                'Forward Dark IV (V)',
                'Forward Dark IV (A)',
                'Forward Dark IV Interpolated?',
                'EL Pulse Energy Delivered (J)',
                'Field1',
                'TestTime'})

sinton_2015_2016 = sinton_2015_2016.rename(columns={
    'Tester': 'User_ID',
    'LotID': 'Batch_ID',
    'Name': 'Sample_ID',
    'TestDate': 'Measurement_Date-Time',
    'IscMod': 'Isc_(A)',
    'VocMod': 'Voc_(V)',
    'ImpMod': 'Imp_(A)',
    'VmpMOd': 'Vmp_(V)',
    'Power': 'Pmp_(W)',
    'V_Isc': 'V_at_Isc_(V)',
    'EffMod': 'Efficiency_(percent)',
    'EffCells': 'Cell_Efficiency_(percent)',
    'FF': 'FF_(percent)',
    'Suns': 'Intensity_(suns)',
    'Rsh_Ohms': 'Rsh_(ohm)',
    'Rsh_OhmCm2': 'Rsh_(ohm-cm2)',
    'Rs_Ohms': 'Rs_(ohm)',
    'Rs_OhmCm2': 'Rs_(ohm-cm2)',
    'Vmp_Cell': 'Vmp_(V/cell)',
    'Voc_Cell': 'Voc_(V/cell)',
    'Jmp': 'Jmp_(A/cm2)',
    'Jsc': 'Jsc_(A/cm2)',
    'dVdt': 'dV/dt',
    'PseudoEff': 'pEfficiency_(percent)',
    'PseudoVmp': 'Pmp_(W/cm2)',
    'PseudoJmp': 'pJmp_(A/cm2)',
    'PseudoFF': 'pFF_(percent)',
    'PseudoPmp': 'pPmp_(W/cm2)',
    'Temp_C': 'Measured_Temperature_(C)',
    'TargetVload': 'VLoad_(V/cell)',
    'CellArea': 'Cell_Area_(cm2)',
    'ModuleArea': 'Total_Area_(cm2)',
    'NumCells': 'Number_of_Cells_per_String',
    'Type': 'Sample_Type',
    'Resistivity_OhmCm': 'Resistivity_(ohm-cm)',
    'Thick_cm': 'Thickness_(cm)',
    'VoltDiv': 'Voltage_Transfer',
    'dVocdC': 'Voltage_Temperature_Coefficient_(mV/C)',
    'RefCell': 'Reference_Constant_(V/sun)',
    'CurrShunt': 'Current_Transfer',
    'RsModulation': 'Rs_Modulation_(ohm-cm2)',
    'TargetRsMod': 'Rs_Modulation_Target_(ohm-cm2)',
    'TestType': 'Measurement_Type',
    'Jo': 'Jo_(fA/cm2)',
    'BRR': 'BRR_(Hz)',
    'Jo1': 'Jo1_(A/cm2)',
    'Jo2': 'Jo2_(A/cm2)',
    'n_1Sun': 'n_at_1_sun',
    'n_p1Sun': 'n_at_ 1/10_suns',
    'MaxInten': 'Max_Intensity_(suns)',
    'SWVersion': 'Software_Version',
    'AnalysisMode': 'Analysis_Type'
})

sinton_2015_2016 = sinton_2015_2016.drop(columns={
    'CalcPmp', 'CalcImp', 'CalcVmp', 'CalcFF', 'RshFit',
    'BGN', 'DeltaNFitPoint', 'AugerCoeff', 'JoeFitRange'})
"""
