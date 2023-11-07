import glob


def create_csv(file_location, all_data, timestamp_str):
    """
    Save data csv file

    :param file_location: Location to save csv file
    :param all_data: Dataframe containing all processed data
    :param timestamp_str: Timestamp to use in filename. Should be in format 'ddMMyyyThhmm'
    :return: Ascii-encoded text file containing the processed data
    """

    output_filename = f"{glob.glob(file_location)[0]}/Care_Leavers_{timestamp_str}.csv"

    all_data.to_csv(output_filename, index=False, encoding="ascii", errors="ignore")
