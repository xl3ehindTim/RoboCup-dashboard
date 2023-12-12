import pandas as pd

from ..referee_log import RefereeLog
from ..log_parser import MSLLogparser

class MergeLogs:
    def __init__(self, referee_log: RefereeLog, team_logs: [MSLLogparser]):
        referee_merge = self.__merge_referee_team(referee_log, team_logs)
        self.data = self.__merge_msl(referee_merge).sort_values("timestamp")

    def __merge_msl(self, team_logs: [MSLLogparser]):
        return pd.concat([team for team in team_logs], axis=1)

    def __merge_referee_team(self, referee: RefereeLog, team_logs: [MSLLogparser]):
        for i, team in enumerate(team_logs):
            team_logs[i] = \
                pd.merge_asof(team.data, referee.data, left_on="timestamp", right_on="datetime", tolerance=pd.to_timedelta("1min"),)
        return team_logs