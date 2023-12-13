from .base_parser import BaseParser
import pandas as pd

class TeamParser:
    def __init__(self, team_data: [BaserParser]):
        self.data = self.__parse_data(team_data)


    def __parse_data(self, data: [BaseParser]):
        data_frame = pd.DataFrame()
        for i, player in enumerate(data):
            player["player_id"] = i
            data_frame = pd.concat(data_frame, data, axis=1)
        return data_frame.sort_values("liveseconds").reset_index(inplace=True)