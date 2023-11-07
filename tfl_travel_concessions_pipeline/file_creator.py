import glob
from datetime import datetime


def create_csv(file_location, all_data):
    """
    Save data csv file

    :param file_location: Location to save csv file
    :param all_data: Dataframe containing all processed data
    :return: Text file containing the processed data
    """

    now = datetime.now()
    timestamp_str = now.strftime("%d%m%y_T%H%M")

    output_filename = f"{glob.glob(file_location)[0]}/Care_Leavers_{timestamp_str}.csv"

    all_data.to_csv(output_filename, index=False, encoding="ascii", errors="ignore")
