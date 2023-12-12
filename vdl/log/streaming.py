from .robotLogs import RobotLogs, BaseLog

class Streaming(BaseLog):
    def __init__(self, file):
        super().__init__(file)

    def read_stream(self):
        pass