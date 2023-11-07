from datetime import datetime


def save_worksheet_name_error(log_filename, filename, worksheet_name):
    """
    Save errors to a text file in the log directory

    :param log_filename: Location and name of the error log folder
    :param filename: The file being processed
    :param worksheet_name: Expected name of worksheet
    :return: Text file containing the error information
    """

    with open(
        log_filename,
        "a",
    ) as f:
        f.write(
            f"Could not process '{filename}' because no worksheet named '{worksheet_name}' was found in the file\n"
        )


def save_worksheet_columns_error(log_filename, filename):
    """
    Save errors to a text file in the log directory

    :param log_filename: Location and name of the error log folder
    :param filename: The file being processed
    :return: Text file containing the error information
    """

    with open(
        log_filename,
        "a",
    ) as f:
        f.write(
            f"Could not process '{filename}' because not all required columns were found in the file\n"
        )


def save_dropped_rows_error(log_filename, filename, dropped_row_count):
    """
    Save errors to a text file in the log directory

    :param log_filename: Location and name of the error log folder
    :param filename: The file being processed
    :param dropped_row_count: Number of rows dropped from processed file because one or more columns did not contain mandatory data
    :return: Text file containing the error information
    """

    with open(
        log_filename,
        "a",
    ) as f:
        f.write(
            f"Removed {dropped_row_count} rows from '{filename}' because not all columns contained values\n"
        )


def save_empty_csv_error(log_filename):
    """
    Save errors to a text file in the log directory

    :param log_filename: Location and name of the error log folder
    :return: Text file containing the error information
    """

    with open(
        log_filename,
        "a",
    ) as f:
        f.write(
            f"Could not create csv output because no data was found in the processed files\n"
        )
