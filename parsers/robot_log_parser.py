import numpy as np
import pandas as pd

from .base_parser import BaseParser


class RobotLogParser(BaseParser):
    def __init__(self, file):
        super().__init__(file)
        self.data = self.__parse_data(self.data)

    def __parse_data(self, data: pd.DataFrame) -> pd.DataFrame:
        return data.assign(
            liveseconds=lambda df: pd.to_timedelta(df["liveseconds"], unit="seconds"),
            wm_self_confidence=lambda df: (df["wm.self.confidence"] * 100)
            .bfill()
            .astype(np.uint8),
            wm_ball_confidence=lambda df: (df["wm.ball.confidence"] * 100)
            .bfill()
            .astype(np.uint8),
            wm_decision_selected_strategy=lambda df: pd.Categorical(
                df["wm.decision.selected_strategy"]
            ),
            hw_omni_robot_fc0_pos_x=lambda df: df["hw.omni.robot_fc0.pos.x"]
            .bfill()
            .astype(np.float32)
            .round(3),
            hw_omni_robot_fc0_pos_y=lambda df: df["hw.omni.robot_fc0.pos.y"]
            .bfill()
            .astype(np.float32)
            .round(3),
            hw_omni_robot_fc0_pos_r=lambda df: df["hw.omni.robot_fc0.pos.r"]
            .bfill()
            .astype(np.float32)
            .round(3),
            wm_local_pass_request_data_valid=lambda df: df[
                "wm.local.pass_request_data.valid"
            ]
            == 1,
            tm_skills_interceptball_task_active=lambda df: df[
                "tm.skills.interceptball.task.active"
            ]
            == 1,
            wm_ball_pos_x=lambda df: df["wm.ball.pos.x"]
            .bfill()
            .astype(np.short)
            .round(3),
            wm_ball_pos_y=lambda df: df["wm.ball.pos.y"]
            .bfill()
            .astype(np.short)
            .round(3),
            hw_io_input_kick_trigger=lambda df: pd.Categorical(
                df["hw.io.input.kick.trigger"]
            ),
            wm_self_pos_x=lambda df: df["wm.self.pos.x"]
            .bfill()
            .round(3)
            .astype(np.float32),
            wm_self_pos_y=lambda df: df["wm.self.pos.y"]
            .bfill()
            .round(3)
            .astype(np.float32),
            wm_self_pos_r=lambda df: df["wm.self.pos.r"]
            .bfill()
            .round(3)
            .astype(np.float32),
            wm_ball_vel_x=lambda df: df["wm.ball.vel.x"]
            .bfill()
            .round(3)
            .astype(np.float32),
            wm_ball_vel_y=lambda df: df["wm.ball.vel.y"]
            .bfill()
            .round(3)
            .astype(np.float32),
            wm_self_vel_x=lambda df: df["wm.self.vel.x"]
            .bfill()
            .round(3)
            .astype(np.float32),
            wm_self_vel_y=lambda df: df["wm.self.vel.y"]
            .bfill()
            .round(3)
            .astype(np.float32),
            wm_self_vel_r=lambda df: df["wm.self.vel.r"]
            .bfill()
            .round(3)
            .astype(np.float32),
            hw_motion_cur_pos_ec_x=lambda df: df["hw.motion.cur_pos_ec.x"]
            .bfill()
            .round(3)
            .astype(np.float32),
            hw_motion_cur_pos_ec_y=lambda df: df["hw.motion.cur_pos_ec.y"]
            .bfill()
            .round(3)
            .astype(np.float32),
            hw_motion_cur_pos_ec_r=lambda df: df["hw.motion.cur_pos_ec.r"]
            .bfill()
            .round(3)
            .astype(np.float32),
            hw_motion_cur_vel_ec_x=lambda df: df["hw.motion.cur_vel_ec.x"]
            .bfill()
            .round(3)
            .astype(np.float32),
            hw_motion_cur_vel_ec_y=lambda df: df["hw.motion.cur_vel_ec.y"]
            .bfill()
            .round(3)
            .astype(np.float32),
            hw_motion_cur_vel_ec_r=lambda df: df["hw.motion.cur_vel_ec.r"]
            .bfill()
            .round(3)
            .astype(np.float32),
            hw_omni_nr_balls=lambda df: df["hw.omni.nr_balls"].bfill().astype(np.uint8),
            hw_omni_found_balls_rc0_pos_x=lambda df: df["hw.omni.found_balls_rc0.pos.x"]
            .bfill()
            .round(3)
            .astype(np.float32),
            hw_omni_found_balls_rc0_pos_y=lambda df: df["hw.omni.found_balls_rc0.pos.y"]
            .bfill()
            .round(3)
            .astype(np.float32),
            wm_local_pass_request_data_target_pos_x=lambda df: df[
                "wm.local.pass_request_data.target_pos.x"
            ]
            .bfill()
            .round(3)
            .astype(np.float32),
            wm_local_pass_request_data_target_pos_y=lambda df: df[
                "wm.local.pass_request_data.target_pos.y"
            ]
            .bfill()
            .round(3)
            .astype(np.float32),
            tm_skills_fsm_state_nr_current=lambda df: pd.Categorical(
                df["tm.skills.fsm.state_nr_current"]
            ),
            sm_stereo_process_out_imu_heading=lambda df: df[
                "sm.stereo_process.out.imu.heading"
            ]
            .bfill()
            .round(3)
            .astype(np.float32),
            tm_skills_teamplanner_result_path0_game_state=lambda df: pd.Categorical(
                df["tm.skills.teamplanner.result_path0.game_state"]
            ),
            tm_skills_teamplanner_result_path0_dynamic_role=lambda df: pd.Categorical(
                df["tm.skills.teamplanner.result_path0.dynamic_role"]
            ),
            tm_skills_interceptball_debug_new_heading=lambda df: df[
                "tm.skills.interceptball.debug.new_heading"
            ]
            .bfill()
            .round(3)
            .astype(np.float32),
            tm_skills_interceptball_debug_new_speed=lambda df: df[
                "tm.skills.interceptball.debug.new_speed"
            ]
            .bfill()
            .round(3)
            .astype(np.float32),
            tm_skills_interceptball_debug_intercept_distance=lambda df: df[
                "tm.skills.interceptball.debug.intercept_distance"
            ]
            .bfill()
            .round(3)
            .astype(np.float32),
        ).drop(
            columns=[
                "wm.self.confidence",
                "wm.ball.confidence",
                "wm.decision.selected_strategy",
                "hw.omni.robot_fc0.pos.x",
                "hw.omni.robot_fc0.pos.y",
                "wm.local.pass_request_data.valid",
                "tm.skills.interceptball.task.active",
                "wm.ball.pos.x",
                "wm.ball.pos.y",
                "hw.io.input.kick.trigger",
                "wm.local.pass_request_data.eta",
                "wm.self.pos.x",
                "wm.self.pos.y",
                "wm.self.pos.r",
                "wm.self.vel.x",
                "wm.self.vel.y",
                "wm.self.vel.r",
                "hw.motion.cur_pos_ec.x",
                "hw.motion.cur_pos_ec.y",
                "hw.motion.cur_pos_ec.r",
                "hw.motion.cur_vel_ec.x",
                "hw.motion.cur_vel_ec.y",
                "hw.motion.cur_vel_ec.r",
                "hw.omni.robot_fc0.pos.r",
                "wm.ball.vel.x",
                "wm.ball.vel.y",
                "wm_decision_selected_strategy",
                "hw.omni.nr_balls",
                "hw.omni.found_balls_rc0.pos.x",
                "hw.omni.found_balls_rc0.pos.y",
                "wm.local.pass_request_data.target_pos.x",
                "wm.local.pass_request_data.target_pos.y",
                "tm.skills.fsm.state_nr_current",
                "sm.stereo_process.out.imu.heading",
                "tm.skills.teamplanner.result_path0.game_state",
                "tm.skills.teamplanner.result_path0.dynamic_role",
                "tm.skills.interceptball.debug.new_heading",
                "tm.skills.interceptball.debug.new_speed",
            ]
        )
