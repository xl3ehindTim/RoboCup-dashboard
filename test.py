import msl
import pandas as pd

import json

msl_log = [
    # msl.MSLLogparser("test/match_1/20160630_085459.A.msl"),
    msl.MSLLogparser("test/match_2/20190707_141600.A.msl")
]

msl_referee = msl.RefereeLog("test/match_2/20190707_141600.msl")
merge = msl.MergeLogs(referee_log=msl_referee, team_logs=msl_log)
merge.data.to_json("viz_robocup.json")
