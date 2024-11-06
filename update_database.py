# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 16:44:56 2024

@authors: Brent Thompson


Update Database: Software for updating databases at Florida Solar Energy Center PVMCF 1940-101.

Metadata is processed from the following systems:
    - Module Metadata, Measurement Settings, Module Status
    - Sinton Measurement Metadata (MFR)
    - Dark IV (DIV)
    - Module Scanner Metadata (NC)
    - V10 Metadata (V10)
    - IR Metadata (IR)
    - UVF Metadata(UVF)


The program is designed to be run on a daily basis, and can be ran whenever new data is available.
This program will use current FSEC filename standards and update FSEC database with any new data. 

Events and Errors are tracked and logged in 'database_log.log'.

"""
import logging
import sqlite3 as sq
import psycopg2
import pandas as pd
import database_manipulation as dm

import mfr_pipeline
import darkiv_pipeline


DATASETS = 'E:/University of Central Florida/UCF_Photovoltaics_GRP - Documents/General/FSEC_PVMCF/module_databases/'
database = DATASETS + "FSEC_Database.db"
database_log = DATASETS + "FSEC_Database_log.log"


def create_sqlite_record(table_name, columns, values):
    """
    Inserts a single new entry to the database

    Parameters
    ----------
    table_name : String
        Name of SQL table to insert data to
        Single quotes surround table name in double quotes '"table-name"'
    columns : List
        List of column names for respective table name.
    values : List
        List of values to enter on column names

    """
    with sq.connect(database) as connection:
        cursor = connection.cursor()

    # Generate SQL for inserting data
    columns = ', '.join(columns)
    values = ', '.join(values)
    sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
    try:
        # Execute and commit the SQL
        cursor.execute(sql)
        connection.commit()
    except Exception as e:
        print(e)
        print("Problem with SQL command: " + sql)

    connection.close()
    return "Entry added to " + table_name


def create_sqlite_records_from_dataframe(table_name, dataframe):
    """
    Inserts a new row to the database for every row in dataframe

    Parameters
    ----------
    table_name : String
        Name of SQL table to insert data to
        Single quotes surround table name in double quotes '"table-name"'.
    dataframe : Pandas Dataframe
        Output from metadata parsing modules, used as raw data to construct
        SQL statements.

    """
    with sq.connect(database) as connection:
        cursor = connection.cursor()

    # Generate SQL for inserting data
    for value, row in dataframe.iterrows():
        space = ' ', ''
        columns = ', '.join(
            [f'"{col.replace(space[0],space[1])}"' for col in row.index])
        placeholders = ', '.join([f'"{value}"' for value in row.values])
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        try:
            # Execute and commit the SQL
            cursor.execute(sql)
            connection.commit()
        except Exception as e:
            print(e)
            print(str(row[0]) + " Was not added to " + table_name)
            pass

    connection.close()
    return table_name + " Updated With " + str(len(dataframe)) + " Entries."


def create_postgres_records_from_dataframe(table_name, dataframe):
    """
    Inserts a new row to the database for every row in dataframe

    Parameters
    ----------
    table_name : String
        Name of SQL table to insert data to
        Single quotes surround table name in double quotes '"table-name"'.
    dataframe : Pandas Dataframe
        Output from metadata parsing modules, used as raw data to construct
        SQL statements.

    """
    connection = psycopg2.connect(
        database="FSEC_Database", user="postgres", password="tau", host="localhost", port=5433)
    cursor = connection.cursor()

    # Generate SQL for inserting data
    for value, row in dataframe.iterrows():
        space = ' ', ''
        columns = ', '.join(
            [f'"{col.replace(space[0],space[1])}"' for col in row.index])
        placeholders = ', '.join([f'"{value}"' for value in row.values])
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        try:
            # Execute and commit the SQL
            cursor.execute(sql)
            connection.commit()
        except Exception as e:
            print(e)
            print(str(row[0]) + " Was not added to " + table_name)
            pass

    connection.close()
    return table_name + " Updated With " + str(len(dataframe)) + " Entries."


# Function to read data from a table
def read_records(database, table_name, select='*', conditions=None):
    """
    Returns the contents of a table as a dataframe.

    Parameters
    ----------

    table_name : String
        Name of SQL table to insert data to
        Single quotes surround table name in double quotes '"table-name"'.
    select : String, optional
        Choose which columns to select, default is all
    conditions : String, optional
        WHERE, GROUP BY, ect..

    Returns
    -------
    records : Pandas Datafrane
        Results of SQL query in dataframe.

    """
    with sq.connect(database) as connection:
        cursor = connection.cursor()

    # Build SQL query
    sql = f"SELECT {select} FROM {table_name}"
    if conditions:
        sql += f" {conditions}"

    # Execute the query and fetch all records
    cursor.execute(sql)
    records = pd.read_sql_query(
        sql, connection, parse_dates='"Measurement_Date-Time"')

    connection.close()
    return records


def create_logger():
    """
    Sets up and configures a logger to keep track of errors and system events.

    Returns
    -------
    logger : Logger Object
        Records events during runtime in log file FSEC_Database_log.log.

    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(database_log)
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    if not logger.handlers:
        logger.addHandler(file_handler)
    logger.info("Main update database program started.")

    return logger


def EOD_Update_FSEC_Database(logger):
    """
    This routine goes through each dataset and updates the FSEC database

    Each dataset has an original source

    """
# Module Metadata
    module_metadata = dm.read_database(
        f'{DATASETS}module-metadata.txt')
    log = create_sqlite_records_from_dataframe(
        '"module-metadata"', module_metadata)
    logger.info(log)

# Measurement Settings
    measurement_settings = dm.read_database(
        f'{DATASETS}measurement-settings.txt')
    log = create_sqlite_records_from_dataframe(
        '"measurement-settings"', measurement_settings)
    logger.info(log)

# Module Status - Needs primary key
    """
    module_status = dm.read_database(
        f'{DATASETS}module-status.txt')
    log = create_sqlite_records_from_dataframe(
        '"module-status"', module_status)
    logger.info(log)
    
    """

# Sinton IV
    last_sinton_id = read_records(
        database, '"sinton-iv-results"', select="ID", conditions="").iloc[-1][0]
    sinton_iv = read_records(
        "C:/SintonInstruments/Database/MultiFlash/MultiFlash_Database.s3db",
        "Results", conditions=f"WHERE ID > {last_sinton_id}")
    log = create_sqlite_records_from_dataframe(
        '"sinton-iv-results"', sinton_iv)
    logger.info(log)

# Sinton MFR
    sinton_mfr = mfr_pipeline.mfr_database_updater()
    #sinton_mfr = mp.parse_mfr_metadata()
    log = create_sqlite_records_from_dataframe(
        '"sinton-iv-metadata"', sinton_mfr)
    logger.info(log)

# Dark IV
    dark_iv = darkiv_pipeline.dark_iv_database_updater()
    #dark_iv = mp.parse_darkiv_metadata()

    log = create_sqlite_records_from_dataframe('"dark-iv-metadata"', dark_iv)
    logger.info(log)

# V10
    # TODO Fix Error
    """
    v10_data = mp.parse_v10_metadata()
    log = create_sqlite_records_from_dataframe('"v10-metadata"', v10_data)
    logger.info(log)
    """

# Module Scanner
    # TODO only select the most recent scanner files

    scanner_nc = dm.read_database(f'{DATASETS}scanner-nc-metadata.txt')
    log = create_sqlite_records_from_dataframe(
        '"scanner-nc-metadata"', scanner_nc)
    logger.info(log)

    scanner_jpg = dm.read_database(
        f'{DATASETS}scanner-jpg-metadata.txt')
    log = create_sqlite_records_from_dataframe(
        '"scanner-jpg-metadata"', scanner_jpg)
    logger.info(log)

# Properly shutdown logging
    logger.info("FSEC Database Update Complete.n")
    for handler in logger.handlers:
        handler.flush()
    logging.shutdown()

    return 0


def connect_to_postgres():
    connection = psycopg2.connect(
        database="FSEC_Database", user="postgres", password="tau", host="localhost", port=5433)
    cursor = connection.cursor()
    cursor.execute("SELECT * from 'FSEC_Database.module-metadata';")


if __name__ == "__main__":
    logger = create_logger()
    EOD_Update_FSEC_Database(logger)
