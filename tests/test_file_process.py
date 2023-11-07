from datetime import datetime
import pandas as pd
from unittest.mock import patch
from tfl_travel_concessions_pipeline import file_process


def test_check_expected_worksheet_exists():
    expected_worksheet = "Care Leavers"
    list_sheet_names = ["Care Leavers", "Other sheet"]
    list_sheet_names_error = ["Some worksheet"]
    list_sheet_names_empty = []
    assert file_process.check_expected_worksheet_exists(expected_worksheet, list_sheet_names) is True
    assert file_process.check_expected_worksheet_exists(expected_worksheet, list_sheet_names_error) is False
    assert file_process.check_expected_worksheet_exists(expected_worksheet, list_sheet_names_empty) is False


def test_check_expected_columns_exists():
    expected_columns = [
    "First Name",
    "Surname",
    "Date of Birth",
    "Responsible Borough",
    ]
    df_columns_ok = [
    "Extra column",
    "First Name",
    "Surname",
    "Date of Birth",
    "Responsible Borough",
    "Some other column",
    ]
    df_columns_missing = [
    "First Name",
    "Last name"
    "DOB",
    "Responsible Borough",
    ]
    df_columns_empty = []
    assert file_process.check_expected_columns_exists(expected_columns, df_columns_ok) is True
    assert file_process.check_expected_columns_exists(expected_columns, df_columns_missing) is False
    assert file_process.check_expected_columns_exists(expected_columns, df_columns_empty) is False


@patch('tfl_travel_concessions_pipeline.file_process.save_dropped_rows_error')
def test_process_dataframe(mock_save_dropped_rows_error):
    filename = "test.xlsx"
    log_filename ="test_log.txt"
    columns_list = [
    "A",
    "B",
    "Date of Birth",
    ]
    data = {
    'A': [1, 2, 3, 4, None],
    'B': [5, 6, 7, None, None],
    'Date of Birth': [datetime(2000, 2, 1), datetime(2001, 6, 12), datetime(2003, 7, 14), None, None]
    }
    df = pd.DataFrame(data)
    expected_dropped_rows_count = 1
    
    processed_df = file_process.process_dataframe(df, columns_list, filename, log_filename)
    assert len(processed_df) == 3
    assert (processed_df.iloc[0]['A']) == 1
    assert (processed_df.iloc[2]['Date of Birth'] == '14-JUL-03')
    mock_save_dropped_rows_error.assert_called_once_with(log_filename, filename, expected_dropped_rows_count)
