import pandas as pd
import numpy as np

class MSLLogparser:
    def __init__(self, file_location):
        data = self.__load_data(file_location)
        self.data = self.__parse_format(data).sort_values("timestamp")
        self.error = self.__error_messages(self.data)

    def __load_data(self, file_location):
        return pd.read_json(file_location)

    def __parse_format(self, dataframe: pd.DataFrame):
        data_robots = self.__parse_worldstate(dataframe)
        merged_data = dataframe.merge(data_robots, left_index=True, right_index=True)
        merged_data = (
            merged_data.drop(columns=["index"])
            .rename(columns={"id":"robot_id"})
        )

        name_var_targetPose = self.__detects_column_name(merged_data, ["target pose", "targetPose"])
        data_pose = self.__extract_position(merged_data, name_var_targetPose)
        final_data = merged_data.merge(data_pose, left_index=True, right_index=True).drop(columns=["pose", name_var_targetPose, "velocity"]).drop(columns="worldstate")
        final_data = self.__apply_datatypes(final_data)
        return final_data

    def __parse_worldstate(self, data):
        data_worldstate = pd.json_normalize(data["worldstate"])
        data_robots = pd.json_normalize(data_worldstate["robots"]).reset_index().melt(id_vars="index").dropna()
        data_robots_index = pd.json_normalize(data_robots["value"]).set_index(data_robots.index).merge(data_robots, left_index=True, right_index=True).drop(columns=["variable", "value"])
        return data_robots_index

    def __extract_position(self, data, name_var_targetPose: str,):
        robot_pose = self.__extract_cartesian(data, column="pose").add_prefix("pose_")
        robot_target = self.__extract_cartesian(data, column=name_var_targetPose).add_prefix("target_")
        robot_velocity = self.__extract_cartesian(data, column="velocity").add_prefix("velocity_")
        return pd.concat([robot_pose, robot_target, robot_velocity], axis=1)
    def __extract_cartesian(self, data, column):
        temp_df = pd.concat([data[column].str[0], data[column].str[1], data[column].str[2]], axis=1)
        temp_df.columns.values[0] = "x"
        temp_df.columns.values[1] = "y"
        temp_df.columns.values[2] = "z"
        return temp_df

    def __apply_datatypes(self, data):
        data_mod = (
            data
            .assign(
                ballEngaged=lambda df: df["ballEngaged"] == 1.0,
                robot_id = lambda df: pd.Categorical(df["robot_id"]),
                teamName = lambda df: pd.Categorical(df["teamName"]),
                intention = lambda df: pd.Categorical(df["intention"])
            )
        )
        return data_mod

    def __detects_column_name(self, dataframe: pd.DataFrame, options: [str]):
        for column in dataframe.columns:
            for option in options:
                if option == column:
                    return option
        raise ValueError("Column does not exist in format")

    def __adjust_percentage_column(self, data, column):
        data = data[column]
        data = np.where(data >= 100, 100, data)
        data = np.where(data < 0, 0, data)
        return data

    def modified_data(self):
        """
        :return: 
        """
        data = self.data
        # pct norms
        data["batteryLevel"] = self.__adjust_percentage_column(data, "batteryLevel")
        return data

    def __error_messages(self, data):
        """
        Adds an aditional dataset noting issues in the formating
        :param data:
        :return:
        """

        # check for pct values
        pct_error = data["batteryLevel"].min() < 0  or data["batteryLevel"].max() >= 100

        # check if any null values exist in the dataset
        has_null = data.isna().sum() != 0
        return {"battery_inconsistency": pct_error, "null_values":has_null}