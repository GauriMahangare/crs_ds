# -*- coding: utf-8 -*-
import os
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import psycopg2
import sys
import petl as etl


def get_connection_parameter(parameter):
    """
    Get environment parameters
    """
    return os.getenv(parameter)


def main():
    """ Runs data processing scripts to create CSV file from the DB (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    # host, port, database, user, password = ""
    logger = logging.getLogger(__name__)
    logger.info('making connection to postgres')

    host = get_connection_parameter("POSTGRES_HOST")
    port = get_connection_parameter("POSTGRES_PORT")
    database = get_connection_parameter("POSTGRES_DB")
    user = get_connection_parameter("POSTGRES_USER")
    password = get_connection_parameter("POSTGRES_PASSWORD")


# establishing the connection
    conn = psycopg2.connect(
        database=database, user=user, password=password, host=host, port=port
    )
# Creating a cursor object using the cursor() method
    cursor = conn.cursor()

# Executing an POSTGRES function using the execute() method
    cursor.execute("select version()")

# Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    print("Connection established to: ", data)

# Extract Intent and Intent welcome files
    join_sql = """
        SELECT intent_intent.id, intent_intent.name,intent_intentexample.example_text,intent_intentexample.id
            FROM intent_intent
            INNER JOIN intent_intentexample ON intent_intent.id=intent_intentexample.intent_id
    """

    download_sql = "COPY ({0}) TO STDOUT WITH CSV DELIMITER ';' HEADER".format(
        join_sql)

    with open("/Users/gauridhumal/Development Projects/UOL-PROJECTs/CRS/DS/crs_ds/data/raw/intent/intentExamples.csv", "w") as file:
        cursor.copy_expert(download_sql, file)

# Closing the connection
    print("Connection closed")
    conn.close()


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
