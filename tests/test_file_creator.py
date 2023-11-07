from unittest.mock import patch
import pandas as pd
from tfl_travel_concessions_pipeline import file_creator


@patch('pandas.DataFrame.to_csv')
def test_create_csv(mock_to_csv):
    file_location = '/some_folder'
    timestamp_str = '07112023T0958'
    all_data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    expected_filename = "/some_folder/Care_Leavers_07112023T0958.csv"
    file_creator.create_csv(file_location, all_data, timestamp_str)
    mock_to_csv.assert_called_once_with(expected_filename, index=False, encoding="ascii", errors="ignore")
