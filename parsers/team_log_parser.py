import pandas as pd

from .base_parser import BaseParser


class TeamLogParser:
    def __init__(self, team_data: [BaseParser]):
        self.data = self.__parse_data(team_data)

    def __parse_data(self, data: [BaseParser]):
        data_frames = []

        for i, player in enumerate(data):
            player_data = (
                player.data
            )  # Assuming there is a method to get data from BaseParser
            player_data["player_id"] = i
            data_frames.append(player_data)

        result_frame = (
            pd.concat(data_frames).sort_values("liveseconds").reset_index(drop=True)
        )
        return result_frame

    # def __parse_data(self, data: [BaseParser]):
    #     data_frame = pd.DataFrame()

    #     for i, player in enumerate(data):
    #         player["player_id"] = i
    #         data_frame = pd.concat(data_frame, data, axis=1)

    #     return data_frame.sort_values("liveseconds").reset_index(inplace=True)
