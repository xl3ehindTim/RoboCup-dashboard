import app
import os

files = [f"2023-11-23 Test match/rosp-04/{file}"  for file in os.listdir("2023-11-23 Test match/rosp-04") if file[-3:] == "csv"]
robot_logs = app.log.robotLogs.RobotLogs(files)
#
# print(robot_logs.data)

server = app.server.DashApp(robot_logs)
server.run()

# game = app.server.pages.GameOverview()