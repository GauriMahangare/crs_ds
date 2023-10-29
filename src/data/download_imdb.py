# -*- coding: utf-8 -*-
from gzip import GzipFile
import os
import logging
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen

from pathlib import Path


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

    imdb_db_url1 = "https://datasets.imdbws.com/name.basics.tsv.gz"
    imdb_db_url2 = "https://datasets.imdbws.com/title.akas.tsv.gz"
    imdb_db_url3 = "https://datasets.imdbws.com/title.basics.tsv.gz"
    imdb_db_url4 = "https://datasets.imdbws.com/title.crew.tsv.gz"
    imdb_db_url5 = "https://datasets.imdbws.com/title.episode.tsv.gz"
    imdb_db_url6 = "https://datasets.imdbws.com/title.principals.tsv.gz"
    imdb_db_url7 = "https://datasets.imdbws.com/title.ratings.tsv.gz"
    imdb_urls = [imdb_db_url1, imdb_db_url2, imdb_db_url3,
                 imdb_db_url4, imdb_db_url5, imdb_db_url6, imdb_db_url7]
        handle = urllib.urlopen('ftp://ftp.theseed.org/genomes/SEED/SEED.fasta.gz')





if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    main()
