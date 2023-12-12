import pandas as pd
import numpy as np

class RefereeLog:
    def __init__(self, file_location):
        data = self.__load_data(file_location)
        self.data = self.__parse_format(data)
        # self.data = self.__parse_format(data)
        # self.data = self.__parse_format(data)
        # self.error = self.__error_messages(self.data)

    def __load_data(self, file_location):
        data_format = ""
        with open(file_location, "r") as file:
            for line in file.readlines():
                if line.find(",") != -1:
                    data_format += f"{line.replace(' - ', ', ,')}"

        data = pd.DataFrame([x.split(',') for x in data_format.splitlines()])
        return data

    def __parse_format(self, dataframe: pd.DataFrame):
        final_data = (
            dataframe
            .assign(
            # time = lambda df: pd.to_datetime(df[0]),
            status = lambda df: pd.Categorical(df[2]),
            event = lambda df: df[4],
                in_match_time = lambda df: df[1].str[:5],
            time_added = lambda df: df[1].str[6:-1],
            game_state =lambda df: pd.Categorical(df[2]),
                    datetime= lambda df: pd.to_datetime(pd.to_numeric(df[0]), unit="ms"))
        .drop(columns=[0, 1, 2, 3, 4, 5, 6])
        )

        final_data = (
            final_data
            .assign(
                in_match_time=lambda df: pd.to_numeric(df["in_match_time"].str[:2]) + pd.to_numeric(df["in_match_time"].str[3:]) / 60
            )
        )
        return final_data

    def __error_messages(self, data):
        """
        Adds an aditional dataset noting issues in the formating
        :param data:
        :return:
        """
        return