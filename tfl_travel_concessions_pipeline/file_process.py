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
    :param log_filename: Location and name of error log file.
    :return: df: A DataFrame containing the extracted data, or None if an error occurred.
    """
    xls = pd.ExcelFile(filename)
    if check_expected_worksheet_exists(EXPECTED_WORKSHEET_NAME, xls.sheet_names):
        df = pd.read_excel(xls, sheet_name=EXPECTED_WORKSHEET_NAME)
        if check_expected_columns_exists(EXPECTED_COLUMN_NAMES, df.columns):
            df_processed = process_dataframe(
                df, EXPECTED_COLUMN_NAMES, filename, log_filename
            )
            return df_processed
        else:
            save_worksheet_columns_error(log_filename, filename)
    else:
        save_worksheet_name_error(log_filename, filename, EXPECTED_WORKSHEET_NAME)
    return None


def check_expected_worksheet_exists(expected_worksheet, list_sheet_names):
    """
    Check for existence of specific worksheet in an Excel file.

    :param expected_worksheet: Name of worksheet to seek in the Excel file.
    :param list_sheet_names: List of worksheet names to check.
    :return: df: True if the specific worksheet exists in the list of worksheet names, False otherwise.
    """
    if expected_worksheet in list_sheet_names:
        return True
    else:
        return False


def check_expected_columns_exists(expected_columns, df_columns):
    """
    Check for existence of specific columns in a dataframe.

    :param expected_columns: Name of columns to seek in the dataframe.
    :param list_sheet_names: List of column names to check.
    :return: df: True if the all expected columns exist in the list, False otherwise.
    """
    if set(expected_columns).issubset(df_columns):
        return True
    else:
        return False


def process_dataframe(df, columns_list, filename, log_filename):
    """
    Process a dataframe.

    :param filename: Name of the Excel file.
    :param log_filename: Location and name of error log file.
    :return: A DataFrame containing the extracted data.
    """
    df = df[columns_list]
    df = df.dropna(how="all")  # remove rows that are completely blank
    initial_row_count = len(df)
    df = df.dropna(
        subset=columns_list
    )  # Drop rows with missing values in any of the required columns
    final_row_count = len(df)
    dropped_rows_count = initial_row_count - final_row_count
    if dropped_rows_count > 0:
        save_dropped_rows_error(log_filename, filename, dropped_rows_count)
    df["Date of Birth"] = (
        pd.to_datetime(df["Date of Birth"]).dt.strftime("%d-%b-%y").str.upper()
    )
    return df
