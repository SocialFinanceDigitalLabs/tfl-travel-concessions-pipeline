import click as click
from tfl_travel_concessions_pipeline.tfl import pipeline as data_pipeline

import pandas as pd
import glob
import os


@click.group()
def tfl():
    """Functions for parsing and processing TfL travel concession data"""
    pass


@tfl.command()
@click.option(
    "--input",
    "-i",
    type=click.Path(exists=True, file_okay=False, readable=True),
)
def pipeline(input):
    files = glob.glob(input + "/*.csv")

    file_list = []

    for filename in files:
        df = pd.read_csv(filename, index_col=None, header=0)
        file_list.append(df)

    data_pipeline(file_list)
