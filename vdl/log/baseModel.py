import pandas as pd
import os

class BaseLog(object):
    """
    BaseLog property for MSL robot logs. Can be used to analyze behavior pre- and post-game.

    :param
        load_file: str - the file to load

    :except
        value error - File does not exist
    """
    def __init__(self, load_files:[str], ):
        temp_list = []
        for file in load_files:
            temp_list.append(self.__load_data(file))
        self.data = pd.concat(temp_list, axis=0)


    def __file_check(func) :
        """
        Checks if the file is valid


        :return:
            self: BaseLog(object)
            file: str - file to load into memory
        """
        def file_check(self, file) -> func:
            if os.path.relpath(file):
                if os.path.isfile(file):
                    return  func(self, file)
            raise  ValueError("File does not exist")
        return file_check
    @__file_check
    def __load_data(self, file: str) -> pd.DataFrame:
        """
        Loads a file as a Pandas DataFrame

        :param file: (str)
        :return: pandas.Dataframe
        """
        return  pd.read_csv(file, skipinitialspace=True)

    def __parse_data(self, data:pd.DataFrame)  -> pd.DataFrame:
        """
        parses the dataframe into a recquired format

        :param data: (pd.DataFrame)
        :return: pd.DataFrame
        """
        return data