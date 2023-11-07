import unittest
from unittest.mock import mock_open, patch
from tfl_travel_concessions_pipeline import logger


@patch("builtins.open", new_callable=mock_open)
def test_save_worksheet_name_error(mock_file):
    log_filename = "log.txt"
    filename = "test_file.xlsx"
    worksheet_name = "Sheet1"
    expected_output = "Could not process 'test_file.xlsx' because no worksheet named 'Sheet1' was found in the file\n"
    logger.save_worksheet_name_error(log_filename, filename, worksheet_name)
    # ensure the file is being opened correctly
    mock_file.assert_called_once_with(log_filename, "a")
    # ensure that the correct content is being written to the file 
    handle = mock_file()
    handle.write.assert_called_once_with(expected_output)


@patch("builtins.open", new_callable=mock_open)
def test_save_worksheet_columns_error(mock_file):
    log_filename = "log.txt"
    filename = "test_file.xlsx"
    expected_output = "Could not process 'test_file.xlsx' because not all required columns were found in the file\n"
    logger.save_worksheet_columns_error(log_filename, filename)

    mock_file.assert_called_once_with(log_filename, "a")
    handle = mock_file()
    handle.write.assert_called_once_with(expected_output)


@patch("builtins.open", new_callable=mock_open)
def test_save_dropped_rows_error(mock_file):
    log_filename = "log.txt"
    filename = "test_file.xlsx"
    dropped_row_count = 2
    expected_output = "Removed 2 rows from 'test_file.xlsx' because not all columns contained values\n"

    logger.save_dropped_rows_error(log_filename, filename, dropped_row_count)

    mock_file.assert_called_once_with(log_filename, "a")
    handle = mock_file()
    handle.write.assert_called_once_with(expected_output)


@patch("builtins.open", new_callable=mock_open)
def test_save_empty_csv_error(mock_file):
    log_filename = "log.txt"
    expected_output = "Could not create csv output because no data was found in the processed files\n"

    logger.save_empty_csv_error(log_filename)

    mock_file.assert_called_once_with(log_filename, "a")
    handle = mock_file()
    handle.write.assert_called_once_with(expected_output)
