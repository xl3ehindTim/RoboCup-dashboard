import json
from faker import Faker
from enum import Enum
import random

# Initialize Faker
fake = Faker()

Intention = Enum('Intention', ['move', 'follow_ball', 'get_ball', 'dribble', 'shield_ball', 'pass', 'shoot_on_target', 'keeperMove', 'self_pass'])
def generate_robot():
    return {
        "id": random.randint(1, 7),
        "pose": [random.uniform(-11.000, 11.000), random.uniform(-7.000, 7.000), random.uniform(-10.000, 10.000)],
        "targetPose": [random.uniform(-10.000, 10.000), random.uniform(-10.000, 10.000), random.uniform(-10.000, 10.000)],
        "velocity": [random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-5, 5)],
        "intention": fake.enum(Intention),
        "batteryLevel": random.uniform(0.00, 100.00),
        "ballEngaged": random.randint(0, 1)
    }

def generate_ball():
    return {
        "position": [random.uniform(-10, 10), random.uniform(-10, 10), random.uniform(-10, 10)],
        "velocity": [random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-5, 5)],
        "confidence": random.uniform(0, 1)
    }

def generate_obstacle():
    return {
        "position": [random.uniform(-10, 10), random.uniform(-10, 10)],
        "velocity": [random.uniform(-5, 5), random.uniform(-5, 5)],
        "radius": random.uniform(0.1, 2),
        "confidence": random.uniform(0, 1)
    }

def generate_world_model():
    return {
        "name": "MSLWMD",
        "description": "MSL World Model data",
        "type": "object",
        "properties": {
            "type": {"type": "string", "description": "must be worldstate"},
            "teamName": {"type": "string", "description": "name of the team"},
            "intention": {"type": "string", "description": "team intention in English e.g. [attack]"},
            "robots": [generate_robot() for _ in range(random.randint(1, 6))],
            "balls": [generate_ball() for _ in range(random.randint(1, 3))],
            "obstacles": [generate_obstacle() for _ in range(random.randint(1, 4))],
            "ageMs": random.randint(100, 10000)
        }
    }

def generate_event():
    return {
        "name": "MSLEVENT",
        "description": "MSL game event",
        "type": "object",
        "properties": {
            "type": {"type": "string", "description": "must be event"},
            "robotId": {"type": "number", "description": "robot number"},
            "event": {"type": "string", "description": "type of event in English e.g. [kick, pass, …]"}
        }
    }

# Generate Fake Data
world_model_data = generate_world_model()
event_data = generate_event()

# Output Data
print(json.dumps(world_model_data, indent=4))
print(json.dumps(event_data, indent=4))
