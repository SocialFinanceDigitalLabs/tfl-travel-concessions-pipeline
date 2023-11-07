import pandas as pd

from tfl_travel_concessions_pipeline.logger import (
    save_worksheet_name_error,
    save_worksheet_columns_error,
    save_dropped_rows_error,
)

EXPECTED_WORKSHEET_NAME = "Care Leavers"
EXPECTED_COLUMN_NAMES = [
    "First Name",
    "Surname",
    "Date of Birth",
    "Responsible Borough",
]


def process_file(filename, log_filename):
    """
    Process an Excel file and extract data from a specific worksheet.

    :param filename: Location and name of the Excel file.
    :param log_filename: Location and name of error log file
    :return: df: A DataFrame containing the extracted data, or None if an error occurred.
    """
    xls = pd.ExcelFile(filename)
    if EXPECTED_WORKSHEET_NAME in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=EXPECTED_WORKSHEET_NAME)
        if set(EXPECTED_COLUMN_NAMES).issubset(df.columns):
            df = df[EXPECTED_COLUMN_NAMES]
            df = df.dropna(how="all")  # remove completely blank rows
            initial_row_count = len(df)
            df = df.dropna(
                subset=EXPECTED_COLUMN_NAMES
            )  # Drop rows with missing values in required columns
            final_row_count = len(df)
            dropped_rows_count = initial_row_count - final_row_count
            if dropped_rows_count > 0:
                save_dropped_rows_error(log_filename, filename, dropped_rows_count)
            df["Date of Birth"] = (
                pd.to_datetime(df["Date of Birth"]).dt.strftime("%d-%b-%y").str.upper()
            )
            return df
        else:
            save_worksheet_columns_error(log_filename, filename)
    else:
        save_worksheet_name_error(log_filename, filename, EXPECTED_WORKSHEET_NAME)
    return None
