from faker import Faker
from datetime import time
from dataclasses import dataclass
import playerLogGenerator

# Initialize Faker
fake = Faker()

match_time = time(0, 0, 0)

@dataclass
class Velocity:
    x: float
    y: float
    z: float

@dataclass
class Position:
    x: float
    y: float
    z: float

# to be used later for more accurate movement logs
def calculate_position_with_step(log_time, vel_now, vel_old, pos):
    seconds = int(log_time.hours / (60 * 60) + log_time.minutes / (60) + log_time.seconds) #amount of second since movement started
    new_x = float(pos.x + vel_old.x * seconds + (vel_now.x - vel_old.x) * seconds * seconds / 4)  #new x position
    new_y = float(pos.y + vel_old.y * seconds + (vel_now.y - vel_old.y) * seconds * seconds / 4)  #new y position
    pos_now = Position(new_x, new_y, pos.z)
    return pos_now




