import glob
from datetime import datetime
import click

import pandas as pd

from tfl_travel_concessions_pipeline.tfl import pipeline as data_pipeline
from tfl_travel_concessions_pipeline.logger import (
    save_empty_csv_error,
)
from tfl_travel_concessions_pipeline.file_process import process_file
from tfl_travel_concessions_pipeline.file_creator import create_csv


@click.group()
def tfl():
    """Functions for parsing and processing TfL travel concession data"""
    pass


@tfl.command()
@click.option(
    "--input",
    "-i",
    type=click.Path(exists=True, file_okay=False, readable=True),
    help="A string specifying the input file location",
)
def pipeline(input):
    """
    Run the data processing pipeline on a set of Excel files.

    :param input: The directory containing the Excel files.
    :return: None
    """

    start_time = f"{datetime.now():%Y-%m-%dT%H%M%SZ}"
    log_filename = f"{input}/Care_leavers_processing_error_log_{start_time}.txt"

    # process input Excel files
    files = glob.glob(input + "/*.xlsx")
    df_list = [process_file(filename, log_filename) for filename in files]
    df_list = [df for df in df_list if df is not None]

    all_data = pd.concat(df_list, ignore_index=True)

    # Output processed data to csv file
    if not all_data.empty:
        now = datetime.now()
        timestamp_str = now.strftime("%d%m%yT%H%M")
        create_csv(input, all_data, timestamp_str)
        data_pipeline(all_data)
    else:
        save_empty_csv_error(log_filename)
