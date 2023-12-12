import pandas as pd
import os

class BaseParser(object):
    """
    BaseParser property for MSL robot logs. Can be used to analyze behavior pre- and post-game.

    :param load_files: list of str - the list of files to load

    :except ValueError: File does not exist
    """
    def __init__(self, load_files: list):
        self.data = self.__load_files(load_files)

    @staticmethod
    def __file_check(func):
        """
        Checks if the file is valid

        :return:
            func: method - method to execute if the file is valid
            file: str - file to load into memory
        """
        def file_check(self, file):
            if os.path.relpath(file) and os.path.isfile(file):
                return func(self, file)
            raise ValueError("File does not exist")
        return file_check

    def __load_files(self, files: list) -> pd.DataFrame:
        """
        Loads multiple files into a single Pandas DataFrame

        :param files: list of str
        :return: pandas.DataFrame
        """
        temp_list = []
        for file in files:
            temp_list.append(self.__load_data(file))
        return pd.concat(temp_list, axis=0)

    @__file_check
    def __load_data(self, file: str) -> pd.DataFrame:
        """
        Loads a file as a Pandas DataFrame

        :param file: str
        :return: pandas.DataFrame
        """
        return pd.read_csv(file, skipinitialspace=True)

    def parse_data(self) -> pd.DataFrame:
        """
        Parses the DataFrame into the required format

        :return: pd.DataFrame
        """
        return self.data
